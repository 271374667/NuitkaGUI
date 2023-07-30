import logging
import subprocess
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from conf import config
from core import globalVar
from Ui_nuitkaGUI import Ui_MainWindow
from utils import comment, log


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{config.SOFTWARE_NAME}-{config.__version__}")

    def closeEvent(self, event):
        if globalVar.isRunning:
            reply = QMessageBox.question(self, '询问', '当前程序正在运行！是否退出程序?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            elif reply == QMessageBox.StandardButton.No:
                event.ignore()


# 全局app对象和窗口对象
app = QApplication([])
globalVar.app = app
window = MyWindow()


def initWindow() -> QMainWindow:
    """初始化窗口"""
    globalVar.mainWindow = window
    initPythonexe()
    initModuleVersion()
    initWindowArgs()
    initPage()
    return window


def initLogger() -> logging.Logger:
    """初始化日志记录器"""
    # 初始化日志记录器
    globalVar.logger = log.initLogger()
    globalVar.logger.debug('日志记录器初始化完成')

    # 清除日志文件
    log.deleteLog10More()
    return globalVar.logger


def initModuleVersion():
    """检查模块版本，如果模块版本不符合要求就自动安装"""
    # 检查nuitka模块版本
    globalVar.logger.debug('正在检查nuitka模块版本...')
    try:
        from nuitka import Version
    except ModuleNotFoundError:
        globalVar.logger.info('未检测到nuitka模块,正在自动安装...')
        comment.installModule('nuitka')
        globalVar.logger.info('nuitka模块安装完成')
    finally:
        nuiktaVersion = Version.getNuitkaVersion()
        globalVar.logger.debug(f'检测到nuitka模块版本为{nuiktaVersion}')
        if nuiktaVersion < config.ModuleVersion.nuitka.value:
            globalVar.logger.info(
                f'检测到nuitka模块版本{nuiktaVersion}不符合要求,正在自动安装...')
            comment.installModule('nuitka')
            globalVar.logger.info('nuitka模块安装完成')

    # 检查PySide6模块版本
    globalVar.logger.debug('正在检查PySide6模块版本...')
    try:
        from PySide6 import __version__
    except ModuleNotFoundError:
        globalVar.logger.info('未检测到PySide6模块,正在自动安装...')
        comment.installModule('PySide6')
        globalVar.logger.info('PySide6模块安装完成')
    finally:
        pyside6Version = __version__
        globalVar.logger.debug(f'检测到PySide6模块版本为{pyside6Version}')
        if pyside6Version < config.ModuleVersion.pyside6.value:
            globalVar.logger.info(
                f'检测到PySide6模块版本{pyside6Version}不符合要求,正在自动安装...')
            comment.installModule('PySide6')
            globalVar.logger.info('PySide6模块安装完成')

    # 检查pipreqs模块版本
    globalVar.logger.debug('正在检查pipreqs模块版本...')
    try:
        from pipreqs import __version__
    except ModuleNotFoundError:
        globalVar.logger.info('未检测到pipreqs模块,正在自动安装...')
        comment.installModule('pipreqs')
        globalVar.logger.info('pipreqs模块安装完成')
    finally:
        pipreqsVersion = __version__
        globalVar.logger.debug(f'检测到pipreqs模块版本为{pipreqsVersion}')
        if pipreqsVersion < config.ModuleVersion.pipreqs.value:
            globalVar.logger.info(
                f'检测到pipreqs模块版本{pipreqsVersion}不符合要求,正在自动安装...')
            comment.installModule('pipreqs')
            globalVar.logger.info('pipreqs模块安装完成')


def initWindowArgs():
    """初始化窗口参数"""
    # 删除listUnselect里所有的item，然后添加pluginList里的所有item
    globalVar.mainWindow.ui.listUnselect.clear()
    for each in globalVar.pluginList:
        globalVar.mainWindow.ui.listUnselect.addItem(each)


def initPythonexe():
    """初始化python.exe路径"""
    # 使用 where python 命令获取python.exe路径
    # 但是在windows下where命令不是内置命令，所以需要使用subprocess模块调用
    python_path = sys.executable
    # 获取可用的python.exe路径
    result = subprocess.run(
        'where python', stdout=subprocess.PIPE, shell=True)
    # 读取一行数据
    result = result.stdout.decode().splitlines()
    for each in result:
        globalVar.logger.debug(f'寻找到一个Python路径:{each}')
        if comment.isPythonAvailable(each):
            python_path = each
            break
        globalVar.logger.debug(f'当前Python路径{each}不可用')

    globalVar.logger.debug(f"当前Python路径为:{python_path}")
    if comment.isPythonAvailable(python_path):
        globalVar.mainWindow.ui.LEPythonExePath.setText(python_path)
        globalVar.pythonExePath = python_path
        sys.path.append(Path(python_path).parent)
        globalVar.mainWindow.statusBar().showMessage("已添加python.exe路径")
    else:
        QMessageBox.warning(
            globalVar.mainWindow, '警告', '未检测到Python3.x版本，请手动选择Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)


def initPage():
    import pages
