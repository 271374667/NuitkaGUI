import sys
from typing import Optional

import loguru
from PySide6.QtWidgets import QFileDialog

from src.model.welcome_model import WelcomeModel
from src.view.welcome_view import WelcomeView


class WelcomePresenter:
    def __init__(self):
        self._current_finished: int = 0

        self._view = WelcomeView()
        self._model = WelcomeModel()
        self._bind()

    def _use_default_pip_source(self):
        self._model.use_default_pip_source()
        self._view.set_pip_status(True)
        self._update_progress()

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
