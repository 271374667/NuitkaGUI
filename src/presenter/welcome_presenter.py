import sys

import loguru

from src.model.welcome_model import WelcomeModel
from src.view.welcome_view import WelcomeView


class WelcomePresenter:
    def __init__(self):
        self._view = WelcomeView()
        self._model = WelcomeModel()
        self._bind()

    def _finished(self):
        if self._view.show_mask_dialog('完成', '您已经完成了所有的设置,请重启软件后开始使用'):
            loguru.logger.debug('配置完成,重启软件')
            sys.exit(0)

    def _bind(self):
        self._view.get_finish_btn().clicked.connect(self._finished)
