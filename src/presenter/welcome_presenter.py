import sys
from typing import Optional

import loguru
from PySide6.QtWidgets import QFileDialog, QApplication

from src.model.welcome_model import WelcomeModel
from src.utils.thread_utils import RunInThread
from src.view.welcome_view import WelcomeView


class WelcomePresenter:
    def __init__(self):
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

        self._view.show_state_tooltip("运行中……", "正在设置 pip 源,请稍等")
        self._run_in_thread = RunInThread()
        self._run_in_thread.set_start_func(start)
        self._run_in_thread.set_finished_func(finished)
        self._run_in_thread.start()

    def _get_pythonexe_path_by_hand(self) -> Optional[str]:
        """手动获取 python.exe 路径"""
        result = QFileDialog.getOpenFileName(self._view, '选择 python.exe', '', 'Python (*.exe)')
        return result[0] or None

    def _finished(self):
        if self._view.show_mask_dialog('完成', '您已经完成了所有的设置,请重启软件后开始使用'):
            loguru.logger.debug('配置完成,重启软件')
            sys.exit(0)

    def _bind(self):
        self._view.get_finish_btn().clicked.connect(self._finished)
        self._view.get_default_pip_btn().clicked.connect(self._use_default_pip_source)
        self._view.get_auto_pip_btn().clicked.connect(self._use_auto_pip_source)


if __name__ == '__main__':
    app = QApplication()
    presenter = WelcomePresenter()
    presenter.view.show()
    sys.exit(app.exec())
