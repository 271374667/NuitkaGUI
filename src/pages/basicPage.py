import sys
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWhatsThis

from src.core import globalVar, initVar
from src.utils.comment import isPythonAvailable
from src.utils.windowFunc import updateOutputPlainText

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
    sys.path.append(str(Path(globalVar.pythonExePath).parent))
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

    # 下载依赖和重新初始化插件
    initVar.initModuleVersion()
    initVar.initPlugins()

    globalVar.mainWindow.ui.LEPythonExePath.setText(exePath)
    pythonExePathChange(exePath)


whatthis = QWhatsThis()

globalVar.mainWindow.ui.BTNPythonExePath.clicked.connect(setPythonExePath)
globalVar.mainWindow.ui.BTNSetIcon.clicked.connect(setOutPutIcon)
globalVar.mainWindow.ui.LEIcon.textChanged.connect(iconPathChange)
globalVar.mainWindow.ui.BTNSetOutputPath.clicked.connect(setOutputPath)
globalVar.mainWindow.ui.LEOutpuPath.textChanged.connect(outputPathChange)

# 打包参数页面
outputPageIndex = globalVar.mainWindow.ui.tabWidget.indexOf(
        globalVar.mainWindow.ui.tab_4)
globalVar.mainWindow.ui.tabWidget.currentChanged.connect(
        lambda x: updateOutputPlainText() if x == outputPageIndex else None)
