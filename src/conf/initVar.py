import logging

from PySide6.QtWidgets import QMainWindow

from conf import config
from core import globalVar
from Ui_nuitkaGUI import Ui_MainWindow
from utils import download, log


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{config.SOFTWARE_NAME}-{config.__version__}")


window = MyWindow()


def initWindow() -> QMainWindow:
    globalVar.mainWindow = window
    return window


def initLogger() -> logging.Logger:
    # 初始化日志记录器
    globalVar.logger = log.initLogger()
    globalVar.logger.debug('日志记录器初始化完成')

    # 清除日志文件
    log.deleteLog10More()
    return globalVar.logger


def initModuleVersion():
    """检查模块版本，如果模块版本不符合要求就自动安装"""
    for k, v in config.moduleVersion.items():
        if download.isModuleBigger(k, v):
            globalVar.logger.debug(f'模块{k}版本符合要求')
        else:
            download.installModule(k, v)
            globalVar.logger.info(f'模块{k}版本不符合要求，已自动安装')


def initWindowArgs():
    """初始化窗口参数"""
    pass
