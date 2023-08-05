import os
import shutil
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWhatsThis

from src.conf import config
from src.core import globalVar
from src.customWidget.processWindow import ProcessWindow
from src.utils.comment import isPythonAvailable
from src.utils.windowFunc import getArgs, updateOutputPlainText


@Slot()
def standaloneChanged():
    """当打包模式改变时，更新输出命令"""
    globalVar.argsDict['--standalone'] = True
    globalVar.argsDict['--onefile'] = False
    # self.globalVar.argsDict['--onefile-tempdir-spec=nuitkaGUITemp'] = False
    updateOutputPlainText()
    globalVar.logger.debug('已切换到多文件模式')


@Slot()
def onefileChanged():
    """当打包模式改变时，更新输出命令"""
    globalVar.argsDict['--standalone'] = False
    globalVar.argsDict['--onefile'] = True
    # self.globalVar.argsDict['--onefile-tempdir-spec=nuitkaGUITemp'] = False
    updateOutputPlainText()
    globalVar.logger.debug('已切换到单文件模式')


@Slot()
def getExecPyPath():
    """获取python入口文件路径"""
    filePath, _ = QFileDialog.getOpenFileName(
            globalVar.mainWindow, '请选择一个python入口文件', '', 'Python Files (*.py)')
    if filePath:
        globalVar.mainWindow.ui.LinePyFilePath.setText(filePath)
        globalVar.entryFilePath = filePath
        globalVar.argsDict['--main'] = filePath

        # 同时设置输出路径，输出路径默认为入口文件所在目录的 output文件夹下
        # 如果output文件夹不存在则创建
        outputPath = Path(filePath).parent.joinpath('output')
        if not outputPath.exists():
            outputPath.mkdir()
        elif outputPath.exists():
            # 如果output文件夹存在则询问是否删除内部文件
            reply = QMessageBox.question(
                    globalVar.mainWindow, '询问',
                    '检测到当前目录下已经存在output文件夹,可能是曾经的打包结果\n是否删除output文件夹内部文件?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    shutil.rmtree(outputPath)
                except PermissionError:
                    QMessageBox.critical(
                            globalVar.mainWindow,
                            '错误',
                            '删除output文件夹失败,当前可能有其他文件正在占用文件夹',
                            QMessageBox.StandardButton.Ok,
                            )
                    return
                outputPath.mkdir()
                globalVar.mainWindow.statusBar().showMessage('已删除output文件夹内部文件')
            elif reply == QMessageBox.StandardButton.No:
                globalVar.mainWindow.statusBar().showMessage(
                        f'当前工作目录:{Path.cwd()}')

        # 刷新输出命令
        updateOutputPlainText()

        # 给标签设置输出路径
        globalVar.mainWindow.ui.LEOutpuPath.setText(str(outputPath))

        # 设置嵌入式页面的根目录
        globalVar.mainWindow.ui.treeWidget.set_root_path(
                str(Path(filePath).parent))


def openOutputDir(outputexeDir):
    if outputexeDir.exists():
        os.startfile(outputexeDir)
    elif globalVar.argsDict['--onefile'] is True:
        os.startfile(str(Path('output')))
    # 创建一个 bat 来运行程序(仅在非打包单文件模式下创建)
    if globalVar.argsDict['--onefile'] is False:
        batPath = Path(globalVar.entryFilePath).parent.joinpath(
                'output').joinpath('运行.bat')
        with open(batPath, 'w', encoding='utf-8') as f:
            f.write(
                    f'@echo off\nchcp 65001\ncd {outputexeDir}\n{Path(globalVar.entryFilePath).stem}.exe')
    globalVar.isRunning = False


@Slot()
def startNuitka():
    globalVar.isRunning = True
    os.chdir(str(globalVar.homePath))

    # 开始前先判断是否有python路径以及入口文件
    if globalVar.entryFilePath == '':
        QMessageBox.warning(
                globalVar.mainWindow, '警告', '请先点击左上角选择入口文件(需要打包的py文件)!',
                QMessageBox.StandardButton.Yes)
        return

    if not isPythonAvailable(globalVar.pythonExePath):
        QMessageBox.warning(
                globalVar.mainWindow, '警告', '选择的不是Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)
        return

    os.chdir(Path(globalVar.entryFilePath).parent)
    outputexeDir = Path(globalVar.entryFilePath).parent.joinpath(
            'output').joinpath(f'{Path(globalVar.entryFilePath).stem}.dist')

    globalVar.mainWindow.process = ProcessWindow()
    globalVar.mainWindow.process.run(getArgs())
    globalVar.mainWindow.process.process.finished.connect(lambda _: openOutputDir(outputexeDir))


whatthis = QWhatsThis()

# 打包模式
globalVar.mainWindow.ui.standalone.clicked.connect(standaloneChanged)
globalVar.mainWindow.ui.onefile.clicked.connect(onefileChanged)

globalVar.mainWindow.ui.toolButton.clicked.connect(
        lambda: whatthis.enterWhatsThisMode())

globalVar.mainWindow.ui.btnGetPy.clicked.connect(getExecPyPath)
globalVar.mainWindow.ui.btnStart.clicked.connect(startNuitka)

# 菜单
globalVar.mainWindow.ui.actionAbout.triggered.connect(lambda: QMessageBox.about(
        globalVar.mainWindow, '关于',
        f'作者:Bemake\n版本:{config.__version__}\n时间:2023-04-09\nPySide6学习欢迎加群633585910'))
globalVar.mainWindow.ui.actionShowArgs.triggered.connect(
        lambda: QMessageBox.about(globalVar.mainWindow, '参数', str(getArgs())))
