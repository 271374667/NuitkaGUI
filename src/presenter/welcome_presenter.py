import sys
from typing import Optional

import loguru
from PySide6.QtWidgets import QFileDialog, QApplication

from src.model.welcome_model import WelcomeModel
from src.utils.thread_utils import RunInThread
from src.view.welcome_view import WelcomeView


class WelcomePresenter:
    def __init__(self):
        self._is_running: bool = False

        self._view = WelcomeView()
        self._model = WelcomeModel()
        self._bind()

    @property
    def view(self) -> WelcomeView:
        return self._view

    @property
    def model(self) -> WelcomeModel:
        return self._model

    def _use_default_pip_source(self):
        self._model.pip_source = self._model.default_pip_source
        self._view.pip_source_url = self._model.default_pip_source
        self._view.show_success_infobar('成功', '已经成功设置pip源为默认源')

    def _use_auto_pip_source(self):
        def start():
            url = self._model.auto_pip_source()
            return url

        def finished(url: str):
            self._model.pip_source = url
            self._view.pip_source_url = url
            self._view.finish_state_tooltip("完成", "已经完成了 pip 源的设置")
            self._view.show_success_infobar("成功", f"已经成功设置 pip 源为: {url}")
            self._is_running = False

        if self._is_running:
            self._view.show_error_infobar("错误", "有任务正在运行,请等待其他任务完成")
            return

        self._view.show_state_tooltip("运行中……", "正在设置 pip 源,请稍等")
        self._auto_pip_thread = RunInThread()
        self._auto_pip_thread.set_start_func(start)
        self._auto_pip_thread.set_finished_func(finished)
        self._auto_pip_thread.start()
        self._is_running = True

    def _get_pythonexe_path_by_hand(self):
        """手动获取 python.exe 路径"""
        result = QFileDialog.getOpenFileName(self._view, '选择 python.exe', '', 'Python (*.exe)')
        if result[0] and self._model.is_python_available(result[0]):
            self._view.python_exe_path = result[0]
            self._model.python_exe_path = result[0]
            self._view.show_success_infobar('成功', '已经成功设置 Python 路径')
        else:
            self._view.python_exe_path = None
            self._model.python_exe_path = None
            self._view.show_error_infobar('错误', '选择的 Python 路径不可用')

    def _get_pythonexe_path_by_auto(self):
        def start():
            python_exe_path = self._model.auto_python_exe_path()
            return python_exe_path

        def finished(python_exe_path: Optional[str]):
            if python_exe_path:
                self._view.python_exe_path = python_exe_path
                self._model.python_exe_path = python_exe_path
                self._view.finish_state_tooltip("完成", "已经完成了 Python 路径的设置")
                self._view.show_success_infobar("成功", f"已经成功设置 Python 路径为: {python_exe_path}")
            else:
                self._view.python_exe_path = None
                self._model.python_exe_path = None
                self._view.finish_state_tooltip("完成", "已经完成了 Python 路径的设置")
                self._view.show_error_infobar("错误", "自动获取 Python 路径失败")
            self._is_running = False

        if self._is_running:
            self._view.show_error_infobar("错误", "有任务正在运行,请等待其他任务完成")
            return

        self._view.show_state_tooltip("运行中……", "正在设置 Python 路径,请稍等")
        self._get_pythonexe_thread = RunInThread()
        self._get_pythonexe_thread.set_start_func(start)
        self._get_pythonexe_thread.set_finished_func(finished)
        self._get_pythonexe_thread.start()
        self._is_running = True

    def _install_dependence_by_os(self):
        def start():
            return self._model.install_dependence_by_os()

        def finished(result: bool):
            if result:
                self._view.finish_state_tooltip("完成", "已经完成了系统依赖的安装")
                self._view.show_success_infobar("成功", "已经成功安装了系统依赖")
                self._view.gcc_selected = True
            else:
                self._view.finish_state_tooltip("完成", "已经完成了系统依赖的安装")
                self._view.show_error_infobar("错误", "安装系统依赖失败")
                self._view.gcc_selected = False
            self._is_running = False

        if self._is_running:
            self._view.show_error_infobar("错误", "有任务正在运行,请等待其他任务完成")
            return

        self._view.show_state_tooltip("运行中……", "正在安装系统依赖,请稍等")
        self._install_dependence_thread = RunInThread()
        self._install_dependence_thread.set_start_func(start)
        self._install_dependence_thread.set_finished_func(finished)
        self._install_dependence_thread.start()
        self._is_running = True

    def _install_dependence_by_bat(self):
        def start():
            return self._model.install_dependence_by_bat()

        def finished(result: bool):
            if result:
                self._view.finish_state_tooltip("完成", "已经完成了系统依赖的安装")
                self._view.show_success_infobar("成功", "已经成功安装了系统依赖")
                self._view.gcc_selected = True
            else:
                self._view.finish_state_tooltip("完成", "已经完成了系统依赖的安装")
                self._view.show_error_infobar("错误", "安装系统依赖失败")
                self._view.gcc_selected = False
            self._is_running = False

        if self._is_running:
            self._view.show_error_infobar("错误", "有任务正在运行,请等待其他任务完成")
            return

        self._view.show_state_tooltip("运行中……", "正在安装系统依赖,请稍等")
        self._install_dependence_thread = RunInThread()
        self._install_dependence_thread.set_start_func(start)
        self._install_dependence_thread.set_finished_func(finished)
        self._install_dependence_thread.start()
        self._is_running = True

    def _finished(self):
        if self._view.show_mask_dialog('完成', '您已经完成了所有的设置,请重启软件后开始使用'):
            self._model.finished()
            loguru.logger.debug('配置完成,重启软件')
            sys.exit(0)

    def _bind(self):
        self._view.get_finish_btn().clicked.connect(self._finished)
        self._view.get_default_pip_btn().clicked.connect(self._use_default_pip_source)
        self._view.get_auto_pip_btn().clicked.connect(self._use_auto_pip_source)
        self._view.get_hand_pythonexe_btn().clicked.connect(self._get_pythonexe_path_by_hand)
        self._view.get_auto_pythonexe_btn().clicked.connect(self._get_pythonexe_path_by_auto)
        self._view.get_install_os_dependence_btn().clicked.connect(self._install_dependence_by_os)
        self._view.get_intall_reg_dependence_btn().clicked.connect(self._install_dependence_by_bat)


if __name__ == '__main__':
    app = QApplication()
    presenter = WelcomePresenter()
    presenter.view.show()
    sys.exit(app.exec())
