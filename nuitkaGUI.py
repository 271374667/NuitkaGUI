import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QWhatsThis)

import resource_rc
from func import identifyThirdPartyLibraries, isPythonAvailable, threadRun
from Ui_nuitkaGUI import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.entryFilePath: str = ''
        self.pythonExePath: str = ''
        self.ui.setupUi(self)

        self.argsDict = {
            '--onefile': False,
            '--standalone': True,
            '--show-progress': False,
            '--show-memory': False,
            '--remove-output': False,
            '--follow-imports': False,
            '--windows-disable-console': False,
            '--mingw64': False,
            '--quiet': False,
            '--lto=no': False,
            '--disable-ccache': False,
            '--jobs': 8,
            '--output-dir': '',
            '--main': '',
            '--nofollow-import-to': [],
            '--windows-icon-from-ico': '',
            '--windows-company-name': '',
            '--windows-file-version': '',
            '--windows-product-version': '',
            '--windows-file-description': '',
        }

        # 将插件添加到字典中
        self.pluginList = ['pyside6', 'pyside2', 'pyqt5', 'pyqt6', 'tk-inter', 'matplotlib',
                           'tensorflow', 'pywebview', 'upx', 'multiprocessing', 'trio', 'kivy', 'transformers',
                           'glfw', 'gevent', 'anti-bloat'
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
        self.ui.CBShowProgress.stateChanged.connect(self.argsToggle)
        self.ui.CBShowMemory.stateChanged.connect(self.argsToggle)

        # 插件页面
        self.ui.BTNAddPlugin.clicked.connect(self.addPlugin)
        self.ui.BTNRemovePlugin.clicked.connect(self.removePlugin)
        self.ui.listUnselect.itemDoubleClicked.connect(self.addPlugin)
        self.ui.listSelect.itemDoubleClicked.connect(self.removePlugin)

        # 高级页面
        self.ui.CBRemoveOutput.stateChanged.connect(self.argsToggle)
        self.ui.CBLowMemory.stateChanged.connect(self.argsToggle)
        self.ui.CBDisableCcache.stateChanged.connect(self.argsToggle)
        self.ui.CBFollowImports.stateChanged.connect(self.argsToggle)
        self.ui.CBDisableConsole.stateChanged.connect(self.argsToggle)
        self.ui.CBCleanCache.stateChanged.connect(self.argsToggle)
        self.ui.CBQuiet.stateChanged.connect(self.argsToggle)
        self.ui.jobs.valueChanged.connect(self.jobsChange)
        self.ui.CBMingw64.stateChanged.connect(self.argsToggle)
        self.ui.CBLto.stateChanged.connect(self.argsToggle)

        # 兼容性页面
        self.ui.ListUnselectMod.itemDoubleClicked.connect(self.addMod)
        self.ui.BTNAddMod.clicked.connect(self.addMod)
        self.ui.ListSelectMod.itemDoubleClicked.connect(self.removeMod)
        self.ui.BTNRemoveMod.clicked.connect(self.removeMod)
        self.ui.ListUnselectMod.itemDoubleClicked.connect(self.updateArgs)
        self.ui.ListSelectMod.itemDoubleClicked.connect(self.updateArgs)
        self.ui.tabWidget.currentChanged.connect(self.updateArgs)
        self.ui.BTNAnalysisMod.clicked.connect(self.identificationLibrary)
        self.ui.BTNModDownload.clicked.connect(self.downloadModule)
        self.ui.BTNModStandardCopy.clicked.connect(
            self.unzipStandardMod2ExeDir)

        # 菜单
        self.ui.actionAbout.triggered.connect(lambda: QMessageBox.about(
            self, '关于', '作者:Bemake\n版本:0.0.3\n时间:2023-04-09\nPySide6学习欢迎加群633585910'))
        self.ui.actionShowArgs.triggered.connect(
            lambda: QMessageBox.about(self, '参数', str(self.getArgs())))

    # 公共槽函数============================================
    def getPythonExePath(self):
        # 使用 where python 命令获取python.exe路径
        # 但是在windows下where命令不是内置命令，所以需要使用subprocess模块调用
        python_path = sys.executable
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
            self.ui.ListUnselectMod.clear()
            self.ui.ListSelectMod.clear()
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
            elif key == '--nofollow-import-to' and self.ui.ListSelectMod.count() > 0:
                moduleList = [self.ui.ListSelectMod.item(
                    x).text() for x in range(self.ui.ListSelectMod.count())]
                reqs = [x.split('==')[0] for x in moduleList]
                argsList.append(f'{key}={",".join(reqs)}')
        argsList = [x.replace('\\', '/') for x in argsList]
        return argsList

    def argsToggle(self, value):
        sender = self.sender()
        if isinstance(value, bool):
            if sender == self.ui.standalone:
                self.argsDict['--standalone'] = True
                self.argsDict['--onefile'] = False
                self.argsDict['--onefile-tempdir-spec=./temp'] = False
            elif sender == self.ui.onefile:
                self.argsDict['--standalone'] = False
                self.argsDict['--onefile'] = True
                self.argsDict['--onefile-tempdir-spec=./temp'] = True

        elif value in [2, 0]:
            senderIntToArgs = {
                'CBShowProgress': '--show-progress',
                'CBShowMemory': '--show-memory',
                'CBRemoveOutput': '--remove-output',
                'CBFollowImports': '--follow-imports',
                'CBDisableConsole': '--windows-disable-console',
                'CBQuiet': '--quiet',
                'CBDisableCcache': '--disable-ccache',
                'CBLowMemory': '--low-memory',
                'CBCleanCache': '--clean-cache=all',
                'CBMingw64': '--mingw64',
                'CBLto': '--lto=no',
            }
            self.argsDict[senderIntToArgs[sender.objectName()]
                          ] = sender.isChecked()

    def startNuitka(self):
        # 开始前先判断是否有python路径以及入口文件
        if self.entryFilePath == '':
            QMessageBox.warning(
                self, '警告', '请先点击左上角选择入口文件(需要打包的py文件)!', QMessageBox.StandardButton.Yes)
            return

        os.chdir(Path(self.entryFilePath).parent)

        # TODO:多线程
        @threadRun
        def run():
            process = subprocess.run(' '.join(self.getArgs()), shell=True, encoding='utf-8')
            #process = subprocess.Popen(self.getArgs(), creationflags=subprocess.CREATE_NEW_CONSOLE)
                                        
            
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
            self, '请选择一个python.exe文件', '', 'Python Files (*.exe)')
        if not exePath:
            self.statusBar().showMessage('未选择python.exe文件')
            return
        
        if not isPythonAvailable(exePath):
            QMessageBox.warning(self, '警告', '选择的不是Python3.x版本的python.exe文件', QMessageBox.StandardButton.Ok)
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

    # 兼容性的槽函数============================================

    def updateArgs(self):
        # print(self.getArgs()) # 调试用
        self.ui.PTEArgsOutput.setPlainText(' '.join(self.getArgs()))

    def addMod(self):
        currentSelect = self.ui.ListUnselectMod.currentIndex().row()
        currentItem = self.ui.ListUnselectMod.takeItem(currentSelect)
        self.ui.ListSelectMod.addItem(currentItem)
        self.statusBar().showMessage(f'添加了一个模块{currentItem.text()}', 3000)

    def removeMod(self):
        currentSelect = self.ui.ListSelectMod.currentIndex().row()
        currentItem = self.ui.ListSelectMod.takeItem(currentSelect)
        self.ui.ListUnselectMod.addItem(currentItem)
        self.statusBar().showMessage(f'移除了一个模块{currentItem.text()}', 3000)

    def identificationLibrary(self):
        if self.entryFilePath == '':
            QMessageBox.warning(
                self, '警告', '请先点击左上角选择入口文件(需要打包的py文件)！', QMessageBox.StandardButton.Yes)
            return

        self.statusBar().showMessage('正在识别库文件，请稍等...')
        self.ui.ListUnselectMod.clear()
        try:
            @threadRun
            def run():
                reqs = identifyThirdPartyLibraries(
                    self.pythonExePath, self.entryFilePath)
                for each in reqs:
                    self.ui.ListUnselectMod.addItem(each)

                self.statusBar().showMessage('识别完成', 3000)
            run()
        except Exception as e:
            QMessageBox.warning(
                self, '警告', f'识别库文件失败，错误信息：{e}', QMessageBox.StandardButton.Yes)

    def downloadModule(self):
        # 获取被启用的模块并下载
        moduleList = [self.ui.ListSelectMod.item(
            i).text() for i in range(self.ui.ListSelectMod.count())]
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
        # 解压标准库到exeDir
        exeDir = Path(self.entryFilePath).parent.joinpath(
            'output').joinpath(f'{Path(self.entryFilePath).stem}.dist')
        if not exeDir.exists():
            exeDir.mkdir(parents=True, exist_ok=True)
        else:
            QMessageBox.warning(
                self, '警告', '当前目录下没有找到pythonStandard.zip文件!', QMessageBox.StandardButton.Yes
            )
            return

        self.statusBar().showMessage('正在解压标准库，请稍等...')
        with zipfile.ZipFile('./pythonStandard.zip', 'r') as zip_ref:
            zip_ref.extractall(exeDir)

        self.statusBar().showMessage('解压完成', 3000)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
