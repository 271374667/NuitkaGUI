import sys
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWhatsThis

from core import globalVar
from conf import config
from utils.comment import isPythonAvailable, getArgs
from utils.windowFunc import getExecPyPath, startNuitka, updateOutputPlainText

"""基础页面的方法和绑定"""


@Slot(str)
def iconPathChange(filePath):
    """当图标路径改变时，更新输出命令"""
    globalVar.argsDict['--windows-icon-from-ico'] = filePath


@Slot()
def setOutPutIcon():
    """设置输出文件的图标"""
    filePath, _ = QFileDialog.getOpenFileName(
        globalVar.mainWindow, '请选择一个icon文件', '', 'Python Files (*.ico)')
    if filePath:
        globalVar.mainWindow.ui.LEIcon.setText(filePath)
        iconPathChange(filePath)


@Slot(str)
def outputPathChange(value):
    """当输出路径改变时，更新输出命令"""
    globalVar.argsDict['--output-dir'] = value


def setOutputPath():
    """设置输出路径"""
    if filePath := QFileDialog.getExistingDirectory(globalVar.mainWindow, '请选择输出路径', ''):
        globalVar.mainWindow.ui.LEOutpuPath.setText(filePath)
        outputPathChange(filePath)


@Slot(str)
def pythonExePathChange(value):
    """当python.exe路径改变时,更新输出命令"""
    globalVar.pythonExePath = value
    sys.path.append(Path(globalVar.pythonExePath).parent)
    globalVar.mainWindow.statusBar().showMessage('已添加python.exe路径')


@Slot()
def setPythonExePath():
    """设置python.exe路径"""
    exePath, _ = QFileDialog.getOpenFileName(
        globalVar.mainWindow, '请选择一个python.exe文件', '', 'Python Files (python.exe)')
    if not exePath:
        globalVar.mainWindow.statusBar().showMessage('未选择python.exe文件')
        return

    if not isPythonAvailable(exePath):
        QMessageBox.warning(
            globalVar.mainWindow, '警告', '选择的不是Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)
        return

    globalVar.mainWindow.ui.LEPythonExePath.setText(exePath)
    pythonExePathChange(exePath)


@Slot()
def standaloneChanged():
    """当打包模式改变时，更新输出命令"""
    globalVar.argsDict['--standalone'] = True
    globalVar.argsDict['--onefile'] = False
    # self.globalVar.argsDict['--onefile-tempdir-spec=nuitkaGUITemp'] = False
    globalVar.logger.debug('已切换到多文件模式')


@Slot()
def onefileChanged():
    """当打包模式改变时，更新输出命令"""
    globalVar.argsDict['--standalone'] = False
    globalVar.argsDict['--onefile'] = True
    # self.globalVar.argsDict['--onefile-tempdir-spec=nuitkaGUITemp'] = False
    globalVar.logger.debug('已切换到单文件模式')


whatthis = QWhatsThis()

# 打包模式
globalVar.mainWindow.ui.standalone.clicked.connect(standaloneChanged)
globalVar.mainWindow.ui.onefile.clicked.connect(onefileChanged)

globalVar.mainWindow.ui.toolButton.clicked.connect(
    lambda: whatthis.enterWhatsThisMode())
globalVar.mainWindow.ui.btnGetPy.clicked.connect(getExecPyPath)

globalVar.mainWindow.ui.BTNPythonExePath.clicked.connect(setPythonExePath)
globalVar.mainWindow.ui.BTNSetIcon.clicked.connect(setOutPutIcon)
globalVar.mainWindow.ui.LEIcon.textChanged.connect(iconPathChange)
globalVar.mainWindow.ui.BTNSetOutputPath.clicked.connect(setOutputPath)
globalVar.mainWindow.ui.LEOutpuPath.textChanged.connect(outputPathChange)
globalVar.mainWindow.ui.btnStart.clicked.connect(startNuitka)

# 打包参数页面
outputPageIndex = globalVar.mainWindow.ui.tabWidget.indexOf(
    globalVar.mainWindow.ui.tab_4)
globalVar.mainWindow.ui.tabWidget.currentChanged.connect(
    lambda x: updateOutputPlainText() if x == outputPageIndex else None)
# 菜单
globalVar.mainWindow.ui.actionAbout.triggered.connect(lambda: QMessageBox.about(
    globalVar.mainWindow, '关于', f'作者:Bemake\n版本:{config.__version__}\n时间:2023-04-09\nPySide6学习欢迎加群633585910'))
globalVar.mainWindow.ui.actionShowArgs.triggered.connect(
    lambda: QMessageBox.about(globalVar.mainWindow, '参数', str(getArgs())))
