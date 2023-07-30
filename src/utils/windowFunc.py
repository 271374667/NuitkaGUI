import os
import shutil
import subprocess
from pathlib import Path

from utils.comment import getArgs, isPythonAvailable, threadRun
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox

from core import globalVar


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
                globalVar.mainWindow, '询问', '检测到当前目录下已经存在output文件夹,可能是曾经的打包结果\n是否删除output文件夹内部文件?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                shutil.rmtree(outputPath)
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


@Slot()
def updateOutputPlainText():
    """通过刷新输出控件，显示新的输出命令"""
    globalVar.mainWindow.ui.PTEArgsOutput.setPlainText(' '.join(getArgs()))


@Slot()
def startNuitka():
    globalVar.isRunning = True
    os.chdir(str(globalVar.homePath))

    # 开始前先判断是否有python路径以及入口文件
    if globalVar.entryFilePath == '':
        QMessageBox.warning(
            globalVar.mainWindow, '警告', '请先点击左上角选择入口文件(需要打包的py文件)!', QMessageBox.StandardButton.Yes)
        return

    if isPythonAvailable(globalVar.pythonExePath) == False:
        QMessageBox.warning(
            globalVar.mainWindow, '警告', '选择的不是Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)
        return

    os.chdir(Path(globalVar.entryFilePath).parent)
    outputexeDir = Path(globalVar.entryFilePath).parent.joinpath(
        'output').joinpath(f'{Path(globalVar.entryFilePath).stem}.dist')

    @threadRun
    def run():
        # TODO: 使用装饰器包装兼容性的判断(现在的代码有点冗长)
        # 根据兼容性选项来下载模块
        # 这一行代码负责调用nuitka
        process = subprocess.run(
            getArgs(), creationflags=subprocess.CREATE_NEW_CONSOLE)

        # 运行结束后打开输出文件夹
        if process.returncode == 0 and outputexeDir.exists():
            os.startfile(outputexeDir)
        elif process.returncode == 0 and globalVar.argsDict['--onefile'] is True:
            os.startfile(str(Path('output')))

    run()

    # 创建一个 bat 来运行程序(仅在非打包单文件模式下创建)
    if globalVar.argsDict['--onefile'] is False:
        batPath = Path(globalVar.entryFilePath).parent.joinpath(
            'output').joinpath('运行.bat')
        with open(batPath, 'w', encoding='utf-8') as f:
            f.write(
                f'@echo off\nchcp 65001\ncd {outputexeDir}\n{Path(globalVar.entryFilePath).stem}.exe')

    globalVar.isRunning = False
