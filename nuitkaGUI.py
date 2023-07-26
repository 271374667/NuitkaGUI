import os
import io
import shutil
import subprocess
import sys
import zipfile
import urllib.request
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QWhatsThis)

import resource_rc
from func import identifyThirdPartyLibraries, isPythonAvailable, threadRun
from Ui_nuitkaGUI import Ui_MainWindow

__version__ = '0.0.5'


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.entryFilePath: str = ''
        self.pythonExePath: str = ''
        self.extend_cmd_list = [] # TODO: 在将来会被保存到一个全局文件中,当前是折中的垃圾写法
        self.isRunning = False
        self.homePath = Path(__file__).parent
        self.ui.setupUi(self)
        self.setWindowTitle(f'NuitkaGUI {__version__}')

        self.argsDict = {
            '--onefile': False,
            '--standalone': True,
            '--show-progress': True,
            '--show-memory': False,
            '--remove-output': True,
            '--windows-disable-console': False,
            '--mingw64': False,
            '--quiet': False,
            '--lto=no': False,
            '--disable-ccache': False,
            '--assume-yes-for-downloads': True,
            '--clang': False,
            '--jobs': 8,
            '--output-dir': '',
            '--main': '',
            '--nofollow-import-to': [],
            '--windows-icon-from-ico': '',
            '--windows-company-name': '',
            '--windows-file-version': '',
            '--windows-product-version': '',
            '--windows-file-description': '',
            '--include-package': [],
        }

        # 将插件添加到字典中
        self.pluginList = ['pyside6', 'pyside2', 'pyqt5', 'pyqt6', 'tk-inter', 'matplotlib',
                           'tensorflow', 'pywebview', 'multiprocessing', 'trio', 'kivy', 'transformers',
                           'glfw', 'gevent', 'upx'
                           ]
        for each in self.pluginList:
            self.argsDict[f'--plugin-enable={each}'] = False

        self.initGUI()
        self.bind()

    def initGUI(self):
        self.whatthis = QWhatsThis()
        # 检测是否安装nuitka
        try:
            import nuitka
        except Exception:
            subprocess.call([self.pythonExePath, '-m', 'pip',
                            'install', 'nuitka', '-U'])

        # 删除listUnselect里所有的item，然后添加pluginList里的所有item
        self.ui.listUnselect.clear()
        for each in self.pluginList:
            self.ui.listUnselect.addItem(each)

        self.getPythonExePath()

    def bind(self):
        # 打包模式
        self.ui.standalone.clicked.connect(self.argsToggle)
        self.ui.onefile.clicked.connect(self.argsToggle)

        # 基础页面
        self.ui.toolButton.clicked.connect(
            lambda: self.whatthis.enterWhatsThisMode())
        self.ui.btnGetPy.clicked.connect(self.getExecPyPath)

        self.ui.BTNPythonExePath.clicked.connect(self.setPythonExePath)
        self.ui.BTNSetIcon.clicked.connect(self.setOutPutIcon)
        self.ui.LEIcon.textChanged.connect(self.iconPathChange)
        self.ui.BTNSetOutputPath.clicked.connect(self.setOutputPath)
        self.ui.LEOutpuPath.textChanged.connect(self.outputPathChange)
        self.ui.btnStart.clicked.connect(self.startNuitka)

        # 链接信号

        # 插件页面
        self.ui.BTNAddPlugin.clicked.connect(self.addPlugin)
        self.ui.BTNRemovePlugin.clicked.connect(self.removePlugin)
        self.ui.listUnselect.itemDoubleClicked.connect(self.addPlugin)
        self.ui.listSelect.itemDoubleClicked.connect(self.removePlugin)

        # 高级页面
        self.ui.CBShowProgress.stateChanged.connect(self.argsToggle)
        self.ui.CBShowMemory.stateChanged.connect(self.argsToggle)
        self.ui.CBRemoveOutput.stateChanged.connect(self.argsToggle)
        self.ui.CBLowMemory.stateChanged.connect(self.argsToggle)
        self.ui.CBDisableCcache.stateChanged.connect(self.argsToggle)
        self.ui.CBDisableConsole.stateChanged.connect(self.argsToggle)
        self.ui.CBCleanCache.stateChanged.connect(self.argsToggle)
        self.ui.CBQuiet.stateChanged.connect(self.argsToggle)
        self.ui.jobs.valueChanged.connect(self.jobsChange)
        self.ui.CBMingw64.stateChanged.connect(self.argsToggle)
        self.ui.CBClang.stateChanged.connect(self.argsToggle)
        self.ui.CBLto.stateChanged.connect(self.argsToggle)

        # 嵌入式页面
        self.ui.BTNFlushDir.clicked.connect(self.reflushEmbed)

        # 打包参数页面
        self.ui.tabWidget.currentChanged.connect(self.updateArgs)

        # 菜单
        self.ui.actionAbout.triggered.connect(lambda: QMessageBox.about(
            self, '关于', f'作者:Bemake\n版本:{__version__}\n时间:2023-04-09\nPySide6学习欢迎加群633585910'))
        self.ui.actionShowArgs.triggered.connect(
            lambda: QMessageBox.about(self, '参数', str(self.getArgs())))

    # 公共槽函数============================================
    def getPythonExePath(self):
        # 使用 where python 命令获取python.exe路径
        # 但是在windows下where命令不是内置命令，所以需要使用subprocess模块调用
        python_path = sys.executable
        python_path = ''
        # 获取可用的python.exe路径
        result = subprocess.run(
            'where python', stdout=subprocess.PIPE, shell=True)
        print(result)
        # 读取一行数据
        result = result.stdout.decode().splitlines()
        for each in result:
            print(each)
            if isPythonAvailable(each):
                python_path = each
                break

        print(python_path)
        if isPythonAvailable(python_path):
            self.ui.LEPythonExePath.setText(python_path)
            self.pythonExePath = python_path
            self.pythonExePathChange(python_path)
        else:
            QMessageBox.warning(
                self, '警告', '未检测到Python3.x版本，请手动选择Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)

    def getExecPyPath(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self, '请选择一个python入口文件', '', 'Python Files (*.py)')
        if filePath:
            self.ui.LinePyFilePath.setText(filePath)
            self.entryFilePath = filePath
            self.argsDict['--main'] = filePath

            # 同时设置输出路径，输出路径默认为入口文件所在目录的output文件夹下
            # 如果output文件夹不存在则创建
            outputPath = Path(filePath).parent.joinpath('output')
            if not outputPath.exists():
                outputPath.mkdir()
            elif outputPath.exists():
                # 如果output文件夹存在则询问是否删除内部文件
                reply = QMessageBox.question(
                    self, '询问', '检测到当前目录下已经存在output文件夹,可能是曾经的打包结果\n是否删除output文件夹内部文件?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    shutil.rmtree(outputPath)
                    outputPath.mkdir()
                    self.statusBar().showMessage('已删除output文件夹内部文件')
                elif reply == QMessageBox.StandardButton.No:
                    self.statusBar().showMessage('当前工作目录:' + os.getcwd())

            # 清空兼容性之前的数据
            self.updateArgs()

            self.ui.LEOutpuPath.setText(str(outputPath))

    def getArgs(self) -> list:
        argsList = [self.pythonExePath, '-m', 'nuitka']
        for key, value in self.argsDict.items():
            if value != '' and isinstance(value, str):
                argsList.append(f'{key}={value}')
            elif value is True and isinstance(value, bool):
                argsList.append(key)

            # 特殊处理 --nofollow-import-to
            elif key == '--nofollow-import-to' and self.argsDict['--nofollow-import-to'] != []:
                moduleList = self.argsDict['--nofollow-import-to']
                req = ','.join([x.split('==')[0] for x in moduleList])
                argsList.append(f'{key}={req}')
        argsList.extend(self.getEmbedFile())
        argsList = [x.replace('\\', '/') for x in argsList]
        return argsList

    def argsToggle(self, value):
        sender = self.sender()
        if isinstance(value, bool):
            if sender == self.ui.standalone:
                self.argsDict['--standalone'] = True
                self.argsDict['--onefile'] = False
                # self.argsDict['--onefile-tempdir-spec=nuitkaGUITemp'] = False
            elif sender == self.ui.onefile:
                self.argsDict['--standalone'] = False
                self.argsDict['--onefile'] = True
                # self.argsDict['--onefile-tempdir-spec=nuitkaGUITemp'] = True

        elif value in [2, 0]:
            senderIntToArgs = {
                'CBShowProgress': '--show-progress',
                'CBShowMemory': '--show-memory',
                'CBRemoveOutput': '--remove-output',
                'CBDisableConsole': '--windows-disable-console',
                'CBQuiet': '--quiet',
                'CBDisableCcache': '--disable-ccache',
                'CBLowMemory': '--low-memory',
                'CBCleanCache': '--clean-cache=all',
                'CBMingw64': '--mingw64',
                'CBLto': '--lto=no',
                'CBClang': '--clang',
            }
            self.argsDict[senderIntToArgs[sender.objectName()]
                          ] = sender.isChecked() # type: ignore

    def startNuitka(self):
        self.isRunning = True
        os.chdir(str(self.homePath))

        # 开始前先判断是否有python路径以及入口文件
        if self.entryFilePath == '':
            QMessageBox.warning(
                self, '警告', '请先点击左上角选择入口文件(需要打包的py文件)!', QMessageBox.StandardButton.Yes)
            return

        if isPythonAvailable(self.pythonExePath) == False:
            QMessageBox.warning(
                self, '警告', '选择的不是Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)
            return

        os.chdir(Path(self.entryFilePath).parent)
        exeDir = Path(self.entryFilePath).parent.joinpath(
            'output').joinpath(f'{Path(self.entryFilePath).stem}.dist')

        @threadRun
        def run():
            # TODO: 使用装饰器包装兼容性的判断(现在的代码有点冗长)
            # 根据兼容性选项来下载模块
            if self.ui.RBJRTop.isChecked():
                thirdLibraries = identifyThirdPartyLibraries(
                    self.pythonExePath, self.entryFilePath)
                if thirdLibraries == []:
                    self.statusBar().showMessage('未检测到第三方库')
                    return
                self.argsDict['--nofollow-import-to'] = thirdLibraries

            # 这一行代码负责调用nuitka
            process = subprocess.run(
                self.getArgs(), creationflags=subprocess.CREATE_NEW_CONSOLE)

            if self.ui.RBJRTop.isChecked():
                self.downloadModule()
                self.unzipStandardMod2ExeDir()
            # 运行结束后打开输出文件夹
            if process.returncode == 0 and exeDir.exists():
                os.startfile(exeDir)

        run()

        # 创建一个 bat 来运行程序
        batPath = Path(self.entryFilePath).parent.joinpath(
            'output').joinpath('运行.bat')
        with open(batPath, 'w', encoding='utf-8') as f:
            f.write(
                f'@echo off\nchcp 65001\ncd {exeDir}\n{Path(self.entryFilePath).stem}.exe')

        self.isRunning = False

    def normalRun(self):
        @threadRun
        def run():
            process = subprocess.run(
                    self.getArgs(), creationflags=subprocess.CREATE_NEW_CONSOLE)
        run()

    def outputFinished(self):
        self.process = None

    # 基础页面的槽函数=============================================

    def setOutPutIcon(self):
        filePath, fileType = QFileDialog.getOpenFileName(
            self, '请选择一个icon文件', '', 'Python Files (*.ico)')
        if filePath:
            self.ui.LEIcon.setText(filePath)
            self.iconPathChange(filePath)

    @Slot(str)
    def iconPathChange(self, filePath):
        self.argsDict['--windows-icon-from-ico'] = filePath

    def setOutputPath(self):
        if filePath := QFileDialog.getExistingDirectory(self, '请选择输出路径', ''):
            self.ui.LEOutpuPath.setText(filePath)
            self.outputPathChange(filePath)

    @Slot(str)
    def outputPathChange(self, value):
        self.argsDict['--output-dir'] = value

    def setPythonExePath(self):
        exePath, _ = QFileDialog.getOpenFileName(
            self, '请选择一个python.exe文件', '', 'Python Files (python.exe)')
        if not exePath:
            self.statusBar().showMessage('未选择python.exe文件')
            return

        if not isPythonAvailable(exePath):
            QMessageBox.warning(
                self, '警告', '选择的不是Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)
            return

        self.ui.LEPythonExePath.setText(exePath)
        self.pythonExePathChange(exePath)

    def pythonExePathChange(self, value):
        self.pythonExePath = value
        sys.path.append(os.path.dirname(value))
        self.statusBar().showMessage('已添加python.exe路径')

    # 插件页面的槽函数============================================

    def addPlugin(self):
        currentSelect = self.ui.listUnselect.currentIndex().row()
        currentItem = self.ui.listUnselect.takeItem(currentSelect)
        self.ui.listSelect.addItem(currentItem)
        self.statusBar().showMessage(f'添加了一个插件{currentItem.text()}', 3000)

        # 将参数启用
        for each in self.argsDict:
            if currentItem.text() in each:
                self.argsDict[each] = True

    def removePlugin(self):
        currentSelect = self.ui.listSelect.currentIndex().row()
        currentItem = self.ui.listSelect.takeItem(currentSelect)
        self.ui.listUnselect.addItem(currentItem)
        self.statusBar().showMessage(f'移除了一个插件{currentItem.text()}', 3000)

        # 将参数停用
        for each in self.argsDict:
            if currentItem.text() in each:
                self.argsDict[each] = False

    # 高级页面槽函数============================================

    @Slot(int)
    def jobsChange(self, value):
        self.argsDict['--jobs'] = value

    # 嵌入页面的槽函数============================================

    def reflushEmbed(self) -> None:
        self.ui.treeWidget.set_root_path(Path(self.entryFilePath).parent)

    def getEmbedFile(self) -> list[str]:
        return self.ui.treeWidget.get_nuitka_cmd()

    # 曾经的兼容性的槽函数============================================

    def updateArgs(self):
        # print(self.getArgs()) # 调试用
        self.ui.PTEArgsOutput.setPlainText(' '.join(self.getArgs()))

    def downloadModule(self):
        # 获取被启用的模块并下载
        moduleList = self.argsDict['--nofollow-import-to']
        if moduleList == []:
            QMessageBox.warning(self, '警告', '当前没有启用任何模块',
                                QMessageBox.StandardButton.Yes)
            return

        # 创建在output文件夹下创建hello.dist文件夹
        exeDir = Path(self.entryFilePath).parent.joinpath(
            'output').joinpath(f'{Path(self.entryFilePath).stem}.dist')
        if not exeDir.exists():
            exeDir.mkdir(parents=True, exist_ok=True)

        self.statusBar().showMessage('正在下载模块，请稍等...')
        try:
            @threadRun
            def run():
                subprocess.Popen([self.pythonExePath, '-m', 'pip', 'install', '-t', str(
                    exeDir), *moduleList], creationflags=subprocess.CREATE_NEW_CONSOLE)
            run()
        except Exception as e:
            QMessageBox.warning(
                self, '警告', f'下载模块失败，错误信息：{e}', QMessageBox.StandardButton.Yes)

    @threadRun
    def unzipStandardMod2ExeDir(self):
        # TODO: 未来智能识别需要哪些标准库
        # 解压标准库到exeDir
        exeDir = Path(self.entryFilePath).parent.joinpath(
            'output').joinpath(f'{Path(self.entryFilePath).stem}.dist')
        if not exeDir.exists():
            exeDir.mkdir(parents=True, exist_ok=True)

        # TODO: 未来智能识别Python版本
        # TODO: 加上进度条
        url = 'https://files.cnblogs.com/files/blogs/740926/pythonStandard.zip?t=1690101477&download=true'

        # 下载文件
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
        except Exception as e:
            self.statusBar().showMessage(f'下载标准库失败，错误信息：{e}')
            return

        # 解压缩文件
        self.statusBar().showMessage('正在解压标准库，请稍等...')
        with zipfile.ZipFile(io.BytesIO(data)) as zip_ref:
            zip_ref.extractall(exeDir)

        self.statusBar().showMessage('解压完成', 3000)

    def closeEvent(self, event):
        if self.isRunning:
            reply = QMessageBox.question(self, '询问', '当前程序正在运行！是否退出程序?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            elif reply == QMessageBox.StandardButton.No:
                event.ignore()


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
