import time

import loguru
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class WorkThread(QObject):
    finished_signal = Signal()
    result = Signal(object)

    def __init__(self):
        super().__init__()
        self.kwargs = None
        self.args = None
        self.func = None

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
        self.finished_func = None
        self.worker = WorkThread()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.start)
        self.worker.finished_signal.connect(self.worker.deleteLater)
        self.worker.destroyed.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.destroyed.connect(self.deleteLater)

    def start(self):
        self.thread.start()

    def set_start_func(self, func, *args, **kwargs):
        """设置需要多线程运行的函数"""
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


class TestWindow(QWidget):
    """
    一个用来测试的窗口
    """

    def __init__(self):
        super().__init__()
        self.btn = QPushButton('按钮')
        self.btn.clicked.connect(self.b)

        self.lb = QLabel('标签')

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.btn)
        self.main_layout.addWidget(self.lb)
        self.setLayout(self.main_layout)
        loguru.logger.debug('窗口对象被创建了')

    def b(self):
        self.a = RunInThread()
        self.a.set_start_func(self.temp_func)
        self.a.set_finished_func(self.over)
        self.a.start()

    def temp_func(self):
        self.btn.setEnabled(False)
        self.lb.setText('开始等待3秒')
        loguru.logger.debug('开始等待3秒')
        time.sleep(3)
        loguru.logger.debug('等待结束')
        return '欢迎使用', '你好'

    def over(self, result):
        loguru.logger.debug(f'slot: {result}')
        self.lb.setText('线程结束')
        self.btn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec()
