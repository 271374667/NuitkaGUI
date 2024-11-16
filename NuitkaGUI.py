import importlib
import locale
import os
import sys

import loguru
from PySide6.QtNetwork import QLocalSocket, QLocalServer
from PySide6.QtWidgets import QApplication

from src.config import cfg
from src.core.paths import LOG_FILE, DEPENDENCE_DIR
from src.presenter.main_presenter import MainPresenter
from src.presenter.welcome_presenter import WelcomePresenter
from src.utils.window_dialog_utils import WindowDialogUtils

loguru.logger.add(LOG_FILE, rotation="1 day", retention="1 week", level="DEBUG")

# 设置环境变量为PYTHONIOENCODING=utf-8
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["NUITKA_CACHE_DIR"] = str(DEPENDENCE_DIR)

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

importlib.reload(sys)
loguru.logger.debug(
    f"系统默认编码: {sys.getdefaultencoding()}, 已经重新加载为UTF-8"
)

# 确保环境变量LANG设置为UTF-8
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


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
