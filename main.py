import loguru
from PySide6.QtWidgets import QApplication

from src.common.manager.logger_manager import LoggerManager
from src.common.manager.settings_manager import SettingsManager
from src.core import JsonSettings
from src.presenter.main_presenter import MainPresenter
from src.presenter.welcom_presenter import WelcomePresenter


def start() -> None:
    # 初始化日志
    LoggerManager().initialize()

    # 初始化配置管理器
    settings_manager: SettingsManager = SettingsManager()
    settings_manager.initialize()

    is_first_run = settings_manager.get(JsonSettings.FIRST_RUN.value)
    if is_first_run:
        loguru.logger.info('第一次运行程序,启动欢迎界面')
        window: WelcomePresenter = WelcomePresenter()
        window.show()
    else:
        loguru.logger.info('主界面启动……')
        window: MainPresenter = MainPresenter()
        window.show()


if __name__ == '__main__':
    app = QApplication([])
    try:
        start()
    except Exception as e:
        loguru.logger.critical(e)
    app.exec()
