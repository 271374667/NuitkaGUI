import sys

import loguru
from PySide6.QtNetwork import QLocalSocket, QLocalServer
from PySide6.QtWidgets import QApplication

from src.config import cfg
from src.presenter.main_presenter import MainPresenter
from src.presenter.welcome_presenter import WelcomePresenter
from src.utils.window_dialog_utils import WindowDialogUtils


def is_already_running() -> bool:
    socket = QLocalSocket()
    socket.connectToServer("NuitkaGUI")
    running = socket.waitForConnected(500)
    socket.close()
    return running


@loguru.logger.catch(reraise=True)
def main():
    if is_already_running():
        loguru.logger.warning("Application is already running.")
        dialog = WindowDialogUtils()
        dialog.create_warning_dialog('警告 - 来自NuitkaGUI', '一次只能运行一个NuitkaGUI')
        sys.exit(0)

    server = QLocalServer()
    server.listen("NuitkaGUI")
    app = QApplication([])
    is_first_run: bool = cfg.get(cfg.is_first_run)
    if is_first_run:
        welcome_presenter = WelcomePresenter()
        welcome_presenter.view.show()
    else:
        main_presenter = MainPresenter()
        main_presenter.view.show()
    app.exec()


if __name__ == "__main__":
    main()
