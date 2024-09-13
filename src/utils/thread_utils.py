import contextlib
import ctypes
import threading
import time
from typing import Callable, Optional

import loguru
from PySide6.QtCore import QObject, QThread, Signal


class ThreadWithTimeout:
    @staticmethod
    def __call__(timeout: int):
        """线程超时自动杀死

        通过调用底层CPython的代码将线程超时自动杀死

        Example:
            @thread_with_timeout(5)
                def target_function():
                    for i in range(10):
                        print(f"Doing task {i}")
                        time.sleep(1)  # Simulate time-consuming task
            target_function()

        Args:
            timeout: 超时时间，单位秒
        """

        def decorator(func):
            def wrapper(*args, **kwargs):
                def run_func():
                    with contextlib.suppress(SystemExit):
                        func(*args, **kwargs)

                def timer():
                    time.sleep(timeout)
                    if thread.is_alive():
                        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident),
                                                                         ctypes.py_object(SystemExit))
                        if res > 1:
                            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, 0)
                            loguru.logger.error('Error: could not terminate thread')
                        else:
                            loguru.logger.debug(f'Thread {thread.ident} forcefully terminated')

                thread = threading.Thread(target=run_func)
                thread.start()

                timer_thread = threading.Thread(target=timer)
                timer_thread.start()

            return wrapper

        return decorator


class ForceStopThread:
    def __init__(self):
        self.thread = None
        self.thread_id = None

    def start_task(self, func, *args, **kwargs):
        if self.thread:
            self.stop_task()

        def run():
            self.thread_id = threading.get_ident()
            with contextlib.suppress(SystemExit):
                func(*args, **kwargs)

        self.thread = threading.Thread(target=run)
        self.thread.start()

    def stop_task(self):
        if self.thread is not None and self.thread.is_alive():
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.thread_id),
                                                             ctypes.py_object(SystemExit))
            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(self.thread_id, 0)
                loguru.logger.error('Error: could not terminate thread')
            else:
                loguru.logger.debug(f'Thread {self.thread_id} forcefully terminated')


class WorkThread(QObject):
    finished_signal = Signal()
    result = Signal(object)

    def __init__(self):
        super().__init__()
        self.kwargs = None
        self.args = None
        self.func: Optional[Callable] = None

    def set_start_func(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def start(self):
        if self.args or self.kwargs:
            result = self.func(*self.args, **self.kwargs)
        else:
            result = self.func()
        loguru.logger.debug(f'线程函数执行完毕, 返回值为{result}')
        self.result.emit(result)
        self.finished_signal.emit()

    def __del__(self):
        loguru.logger.debug('线程对象被删除了,内存已经释放')


class RunInThread(QObject):
    def __init__(self):
        super().__init__()
        self.finished_func: Optional[Callable] = None
        self.worker = WorkThread()
        self.mythread = QThread()
        self.worker.moveToThread(self.mythread)

        self.mythread.started.connect(self.worker.start)
        self.worker.finished_signal.connect(self.worker.deleteLater)
        self.worker.destroyed.connect(self.mythread.quit)
        self.mythread.finished.connect(self.mythread.deleteLater)
        self.mythread.destroyed.connect(self.deleteLater)

    def start(self):
        """当函数设置完毕之后调用start即可"""
        self.mythread.start()

    def set_start_func(self, func, *args, **kwargs):
        """设置一个开始函数

        这部分就是多线程运行的地方，里面可以是爬虫，可以是其他IO或者阻塞主线程的函数

        """
        self.worker.set_start_func(func, *args, **kwargs)

    def set_finished_func(self, func):
        """设置线程结束后的回调函数"""
        self.finished_func = func
        self.worker.result.connect(self._done_callback)

    def _done_callback(self, *args, **kwargs):
        if args != (None,) or kwargs:
            self.finished_func(*args, **kwargs)
        else:
            self.finished_func()