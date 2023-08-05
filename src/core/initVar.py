import logging
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QMessageBox

from src.Ui_nuitkaGUI import Ui_MainWindow
from src.conf import config
from src.core import globalVar
from src.customWidget.processWindow import ProcessWindow
from src.utils import comment, log


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.process = ProcessWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{config.SOFTWARE_NAME}-{config.__version__}")

    def closeEvent(self, event):
        if globalVar.isRunning:
            reply = QMessageBox.question(self, '询问', '当前程序正在运行！是否退出程序?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
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
    initPipSource()
    initModuleVersion()
    initWindowArgs()
    initPage()
    initGcc()
    initRestart()
    return window


def initLogger() -> logging.Logger:
    """初始化日志记录器"""
    # 初始化日志记录器
    globalVar.logger = log.initLogger()
    globalVar.logger.debug('日志记录器初始化完成')

    # 清除日志文件
    log.deleteLog10More()
    return globalVar.logger


@comment.threadRun
def initModuleVersion():
    """检查模块版本，如果模块版本不符合要求就自动安装"""

    # 检查nuitka模块版本
    globalVar.logger.debug('正在检查nuitka模块版本...')
    nuitkaVersion = comment.getModuleVersion('nuitka')
    globalVar.logger.debug(f'nuitka模块版本为{nuitkaVersion}')
    if not nuitkaVersion:
        globalVar.logger.info('未检测到nuitka模块,正在自动安装...')
        comment.installModule('nuitka')
        globalVar.logger.info('nuitka模块安装完成')
        globalVar.isRestart = True

    elif nuitkaVersion < config.ModuleVersion.nuitka.value:
        globalVar.logger.info(
                f'检测到nuitka模块版本{nuitkaVersion}不符合要求,正在自动安装...')
        comment.installModule('nuitka')
        globalVar.logger.info('nuitka模块安装完成')
        globalVar.isRestart = True

    # 检查pipreqs模块版本
    globalVar.logger.debug('正在检查pipreqs模块版本...')
    pipreqsVersion = comment.getModuleVersion('pipreqs')
    globalVar.logger.debug(f'pipreqs模块版本为{pipreqsVersion}')
    if not pipreqsVersion:
        globalVar.logger.info('未检测到pipreqs模块,正在自动安装...')
        comment.installModule('pipreqs')
        globalVar.logger.info('pipreqs模块安装完成')
        globalVar.isRestart = True

    elif pipreqsVersion < config.ModuleVersion.pipreqs.value:
        globalVar.logger.info(
                f'检测到pipreqs模块版本{pipreqsVersion}不符合要求,正在自动安装...')
        comment.installModule('pipreqs')
        globalVar.logger.info('pipreqs模块安装完成')
        globalVar.isRestart = True


def initPlugins() -> list[tuple[str, str]]:
    try:
        result = subprocess.check_output([globalVar.pythonExePath, '-m', 'nuitka', '--plugin-list'])
    except TimeoutError:
        globalVar.logger.error('获取插件列表超时')
        # 将现有的插件列表返回
        result_list = [(globalVar.mainWindow.ui.listUnselect.item(x).text(), '') for x in
                range(globalVar.mainWindow.ui.listUnselect.count())]
        globalVar.pluginList = result_list
        for each in result_list:
            globalVar.argsDict[f'--plugin-enable={each[0]}'] = False
        globalVar.logger.debug('使用默认插件中,插件参数初始化完成')
        return result_list
    result_list = result.decode('utf-8').splitlines()[2:]
    result_list = [(x.split(maxsplit=1)[0], x.split(maxsplit=1)[1]) for x in result_list]
    globalVar.pluginList = result_list
    globalVar.logger.debug(f'获取到{len(globalVar.pluginList)}个插件')
    for each in result_list:
        globalVar.argsDict[f'--plugin-enable={each[0]}'] = False
    globalVar.logger.debug('插件参数初始化完成')
    return result_list


@comment.threadRun
def initWindowArgs():
    """初始化窗口参数"""
    # 获取所有可用的插件
    initPlugins()
    # 删除listUnselect里所有的item，然后添加pluginList里的所有item
    globalVar.mainWindow.ui.listUnselect.clear()
    for each in globalVar.pluginList:
        currentItem = QListWidgetItem(each[0])
        currentItem.setToolTip(each[1])
        currentItem.setStatusTip(each[1])
        globalVar.mainWindow.ui.listUnselect.addItem(currentItem)


def initPythonexe():
    """初始化python.exe路径"""
    # 使用 where python 命令获取python.exe路径
    # 但是在windows下where命令不是内置命令，所以需要使用subprocess模块调用
    python_path = sys.executable
    globalVar.systemEncoding = sys.getfilesystemencoding()

    # 获取可用的python.exe路径,顺便初始化系统编码
    try:
        result = subprocess.run(
                'where python', stdout=subprocess.PIPE, shell=True, encoding=globalVar.systemEncoding, timeout=5)
    except:
        globalVar.systemEncoding = 'gbk'
        result = subprocess.run(
                'where python', stdout=subprocess.PIPE, shell=True, encoding=globalVar.systemEncoding, timeout=5)
    globalVar.logger.debug(f'当前系统编码为:{globalVar.systemEncoding}')

    # 读取一行数据
    result = result.stdout.splitlines()
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
        globalVar.mainWindow.statusBar().showMessage("已添加python.exe路径")
    else:
        QMessageBox.warning(
                globalVar.mainWindow, '警告', '未检测到Python3.x版本，请手动选择Python3.x版本的python.exe文件',
                QMessageBox.StandardButton.Ok)


def initPage():
    import src.pages
    type(src.pages.startNuitka)  # 这一段没有任何意义就是为了防止pycharm优化import的时候把src.pages删掉
    globalVar.logger.debug('初始化页面完成')


def initPipSource():
    globalVar.defaultPipSource = comment.getDefaultPipSource()
    globalVar.logger.debug(f'设置默认pip源为{globalVar.defaultPipSource}')


def initGcc():
    globalVar.logger.debug('正在检查gcc可用性...')
    if comment.isGccAvailable():
        globalVar.logger.debug('gcc可用')
        return
    globalVar.logger.debug('gcc不可用')
    globalVar.isRestart = True

    comment.installGcc(comment.downloadGcc())
    globalVar.logger.info(f'gcc安装完成,再次检测gcc可用性:{comment.isGccAvailable()}')


def initRestart():
    if globalVar.isRestart:
        QMessageBox.warning(globalVar.mainWindow, '警告', '检测到部分设置需要重启程序才能生效,请重启程序',
                            QMessageBox.StandardButton.Ok)
        sys.exit()
