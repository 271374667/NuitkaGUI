#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Author  :   B-E-MAKE,KmBase
@Version :   1.0
@License :   (C)Copyright 2022, B-E-MAKE,KmBase
@Desc    :   None
"""
import subprocess
import os
import chardet
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QWhatsThis, QFileDialog, QMessageBox, QPlainTextEdit, QDialog, \
    QVBoxLayout
from PySide6.QtCore import Slot, QProcess, QThread, Signal
from ui.Ui_nuitkaGUI import Ui_MainWindow
from ui import resource_rc


class NewVenv(QThread):
    finished = Signal(str)

    def __init__(self, entryFilePath, basePythonExe):
        super().__init__()
        self.basePythonExe = basePythonExe
        self.pythonHome = os.path.dirname(basePythonExe)
        self.envPath = os.path.dirname(entryFilePath)

    def run(self):
        # 将外部Python解释器的路径加入到PATH环境变量中
        os.environ["PYTHONHOME"] = self.pythonHome
        # 执行命令，并将输出发送到日志窗口
        venvPath = self.envPath + "//venv//"
        p = subprocess.Popen([self.basePythonExe, "-m", "venv", venvPath], stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        return_code = p.wait()
        if return_code == 0 and os.path.exists(venvPath):
            pythonHome = self.envPath + "//venv//Scripts"
            self.finished.emit(pythonHome)
        else:
            print('创建新环境失败')


class MyWindow(QMainWindow):
    def __init__(self, pjPath):
        super().__init__()
        self.pjPath = pjPath
        self.userConfig = {}  # 配置文件
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # output
        self.outputTextEdit = QPlainTextEdit()
        self.outputTextEdit.setReadOnly(True)
        self.outputTextEdit.resize(800, 500)
        self.outputTextEdit.setWindowTitle('输出')
        # 初始化
        self.initParms()  # 初始化变量
        self.updateConfig()  # 初始化配置文件
        self.bind()

    def initParms(self):
        process = subprocess.run(['where', 'python'], stdout=subprocess.PIPE)
        result = process.stdout.decode('utf-8')
        # 获取第一个路径
        result = result.split('\r')[0]
        self.pythonHome = os.path.dirname(result)
        self.ui.lePythonPath.setText(result)
        print('当前Python路径为：' + str(result))
        self.entryFilePath = ''
        self.envFile = ''
        self.argsDict = {
            '--onefile': False,
            '--standalone': True,
            '--show-progress': False,
            '--show-memory': False,
            '--remove-output': False,
            '--nofollow-imports': False,
            '--follow-imports': False,
            '--windows-disable-console': False,
            '--quiet': False,
            '--disable-ccache': False,
            '--jobs': 8,
            '--output-dir': '',
            '--include-data-files': '',
            '--include-data-dir': '',
            '--windows-icon-from-ico': '',
            '--windows-company-name': '',
            '--windows-file-version': '',
            '--windows-product-version': '',
            '--windows-file-description': '',
        }

        # 将插件添加到字典中
        pluginList = ['pyside6', 'pyside2', 'pyqt5', 'pyqt6', 'tk-inter', 'matplotlib',
                      'tensorflow', 'pywebview', 'upx', 'multiprocessing', 'trio', 'kivy']
        for each in pluginList:
            self.argsDict[f'--plugin-enable={each}'] = False
        self.whatthis = QWhatsThis()

    def updateConfig(self):
        self.userConfig['entryFilePath'] = self.entryFilePath  # 主文件路径
        self.userConfig['pythonHome'] = self.pythonHome  # python.exe的父目录
        self.userConfig['envFile'] = self.envFile  # requirements.txt路径
        self.userConfig['userArg'] = self.getArgs()  # userArg  

    def bind(self):
        # 加载配置文件
        self.ui.btnLoadConfig.clicked.connect(self.loadConfig)  # 打开配置文件
        # 打包模式
        self.ui.standalone.clicked.connect(self.argsToggle)
        self.ui.onefile.clicked.connect(self.argsToggle)

        # 基础页面
        self.ui.toolButton.clicked.connect(
            lambda: self.whatthis.enterWhatsThisMode())
        self.ui.btnSetRequirements.clicked.connect(self.setRequirements)
        self.ui.btnGetPy.clicked.connect(self.getEntryPyPath)
        self.ui.btnModifyingPythonPaths.clicked.connect(
            self.modifyingPythonPaths)
        self.ui.btnSetIcon.clicked.connect(self.setOutPutIcon)
        self.ui.lineEdit.textChanged.connect(self.iconPathChange)
        self.ui.btnSetOutputPath.clicked.connect(self.setOutputPath)
        self.ui.lineEdit_2.textChanged.connect(self.outputPathChange)
        self.ui.btnSaveConfig.clicked.connect(self.saveConfig)
        self.ui.btnStart.clicked.connect(self.startNuitka)
        self.ui.lePythonPath.textChanged.connect(self.modifyPythonPath)
        # 链接信号
        self.ui.cbShowProgress.stateChanged.connect(self.argsToggle)
        self.ui.cbShowMemory.stateChanged.connect(self.argsToggle)

        # 插件页面
        self.ui.btnAddPlugin.clicked.connect(self.addPlugin)
        self.ui.btnRemovePlugin.clicked.connect(self.removePlugin)
        self.ui.listUnselect.itemDoubleClicked.connect(self.addPlugin)
        self.ui.listSelect.itemDoubleClicked.connect(self.removePlugin)

        # 高级页面
        self.ui.cbRemoveOutput.stateChanged.connect(self.argsToggle)
        self.ui.cbNoFollowImports.stateChanged.connect(self.argsToggle)
        self.ui.cbLowMemory.stateChanged.connect(self.argsToggle)
        self.ui.cbDisableCcache.stateChanged.connect(self.argsToggle)
        self.ui.cbFollowImports.stateChanged.connect(self.argsToggle)
        self.ui.cbDisableConsole.stateChanged.connect(self.argsToggle)
        self.ui.cbQuiet.stateChanged.connect(self.argsToggle)

        self.ui.jobs.valueChanged.connect(self.jobsChange)
        self.ui.lineEditCompanyName.textChanged.connect(self.companyNameChange)
        self.ui.lineEditFileVersion.textChanged.connect(self.fileVersionChange)
        self.ui.lineEditProductVersion.textChanged.connect(self.productVersionChange)
        self.ui.lineEditFileDescription.textChanged.connect(self.fileDescriptionChange)
        self.ui.lineEditIncludeDataFiles.textChanged.connect(self.includeDataFilesChange)
        self.ui.lineEditIncludeDataDir.textChanged.connect(self.includeDataDirChange)

        # 菜单
        self.ui.actionAbout.triggered.connect(lambda: QMessageBox.about(self, '关于',
                                                                        '作者：B-E-MAKE,KmBase\n版本：1.0.0\n时间：2023-04-09\nPySide6学习欢迎加群633585910'))
        self.ui.actionShowArgs.triggered.connect(lambda: QMessageBox.about(self, '参数', str(self.getArgs())))

    # 公共槽函数============================================
    @Slot()
    def loadConfig(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', "程序配置文件(*userConfig.json)")
        # 加载JSON文件
        try:
            with open(filename, 'r') as f:
                userConfig = json.load(f)
            self.userConfig = userConfig
            # # 打印加载的数据
            # self.input1.setText(userConfig['entryFilePath'])
            # self.input2.setText(userConfig['python_exe'])
            # self.input3.setText(userConfig['env_file'])
            # userConfig_text = "  ".join(userConfig['user_arg'])
            # self.text_edit.setText(userConfig_text)
            print("\n成功使用配置文件！")
        except Exception:
            # print("配置文件有问题")
            print("\n配置文件有问题!")

    @Slot()
    def saveConfig(self):
        print(self.getArgs())
        # 将字典保存为JSON文件
        print(self.userConfig)
        # print(userConfig)
        print(os.path.abspath(os.path.curdir))
        with open('userConfig.json', 'w') as f:
            json.dump(self.userConfig, f)
        print("\n成功保存配置文件！")

    @Slot()
    def getEntryPyPath(self):
        filePath, fileType = QFileDialog.getOpenFileName(
            self, '请选择一个python入口文件', '', 'Python Files (*.py)')
        if filePath:
            self.ui.LinePyFilePath.setText(filePath)
            self.entryFilePath = filePath

    def getArgs(self):
        argsList = ['-m', 'nuitka', self.entryFilePath]
        for key, value in self.argsDict.items():
            if value != '' and isinstance(value, str):
                argsList.append(f'{key}={value}')
            elif value is True and isinstance(value, bool):
                argsList.append(key)
        return argsList

    @Slot()
    def argsToggle(self, value):
        sender = self.sender()
        print(sender.objectName())
        if isinstance(value, bool):
            if sender == self.ui.standalone:
                self.argsDict['--standalone'] = True
                self.argsDict['--onefile'] = False
                # self.argsDict['--onefile-tempdir-spec=./temp'] = False
            elif sender == self.ui.onefile:
                self.argsDict['--standalone'] = False
                self.argsDict['--onefile'] = True
                # self.argsDict['--onefile-tempdir-spec=./temp'] = True

        elif value in [2, 0]:
            senderIntToArgs = {
                'cbShowProgress': '--show-progress',
                'cbShowMemory': '--show-memory',
                'cbRemoveOutput': '--remove-output',
                'cbNoFollowImports': '--nofollow-imports',
                'cbFollowImports': '--follow-imports',
                'cbDisableConsole': '--windows-disable-console',
                'cbQuiet': '--quiet',
                'cbDisableCcache': '--disable-ccache',
                'cbLowMemory': '--low-memory',

            }
            self.argsDict[senderIntToArgs[sender.objectName()]
            ] = sender.isChecked()

    @Slot()
    def setRequirements(self):
        # 显示文件选择对话框
        filename, _ = QFileDialog.getOpenFileName(self, self.pjPath, '选择文件', 'requirements.txt (*.txt)')
        if filename:
            # 将选择的文件路径显示在对应的输入框中
            self.userConfig['envFile'] = filename.strip()
            self.ui.lePythonPath_2.setText(filename)

    @Slot()
    def modifyingPythonPaths(self):
        filePath, fileType = QFileDialog.getOpenFileName(
            self, '请选择python.exe文件', self.pjPath, 'Python Files (*python.exe)')
        if filePath:
            self.ui.lePythonPath.setText(filePath)
            self.statusBar().showMessage(f'当前python路径为：{filePath}', 3000)
            self.pythonHome = os.path.dirname(filePath)
            self.userConfig['pythonHome'] = self.pythonHome
            os.environ['PYTHONPATH'] = self.pythonHome

    @Slot()
    def startNuitka(self):
        # 开始前先判断是否有python路径以及入口文件
        if self.pythonHome == '':
            QMessageBox.warning(
                self, '警告', '请先选择python路径！', QMessageBox.StandardButton.Yes)
            self.modifyingPythonPaths()
            return
        elif self.entryFilePath == '':
            QMessageBox.warning(
                self, '警告', '请先点击左上角选择入口文件(需要打包的py文件)！', QMessageBox.StandardButton.Yes)
            self.getEntryPyPath()
            return
        elif self.ui.lePythonPath_2.text().strip() == '':
            msg_box = QMessageBox.warning(
                self, '警告', '是否需要依赖文件requirements.txt！',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if msg_box == QMessageBox.StandardButton.Yes:
                self.setRequirements()
            else:
                pass
        self.outputTextEdit.clear()
        self.outputTextEdit.show()
        pythonHome = self.pythonHome
        entryFilePath = self.entryFilePath
        basePythonExe = pythonHome + "//python.exe"
        pythonBat = pythonHome + "//activate.bat"
        print(pythonBat)
        if os.path.exists(pythonBat):
            self.onPackage(pythonHome)
        else:
            self.new_venv = NewVenv(entryFilePath, basePythonExe)
            self.new_venv.finished.connect(self.onPackage)  # 连接信号和槽函数
            self.new_venv.start()

    @Slot()
    def logVenv(self, output):
        self.outputTextEdit.append(output)

    @Slot()
    def onPackage(self, pythonHome):
        print("开始打包",self.userConfig)
        envFile = self.userConfig['envFile']
        # 设置环境变量
        path_env = os.environ.get("PATH")
        # 将外部Python解释器的路径加入到PATH环境变量中
        os.environ["PATH"] = "{};{}".format(path_env, pythonHome)
        pipPath = pythonHome + "//pip3.exe"
        # 激活 python 环境
        python_bat = pythonHome + "//activate.bat"
        subprocess.run(python_bat, shell=True)  # 激活Python环境
        # 安装nuitka
        subprocess.call([pipPath, 'install', '-U', 'nuitka'])
        subprocess.call([pipPath, 'install', '-U', 'ordered-set'])
        try:
            env_list = []
            with open(envFile, 'r') as f:
                env_list.append(f.readline().strip())
            print(envFile)
            subprocess.call([pipPath, 'install', '-r', envFile], shell=True)
        except FileNotFoundError:
            print("\n打开requirements.txt错误，自动生成中...")
            subprocess.call([pipPath, 'freeze','>','requirements.txt'], shell=True)  # 帮你生成requirements.txt
            self.ui.lePythonPath_2.setText('requirements.txt')
        self.updateConfig()  # 更新配置
        pythonExe = pythonHome + "//python.exe"
        print("entryFilePath",pythonExe,self.getArgs())
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.readOutput)
        self.process.readyReadStandardError.connect(self.readError)
        self.process.finished.connect(lambda: self.process.deleteLater())
        self.process.finished.connect(
            lambda: QMessageBox.information(self, '提示', '运行结束！', QMessageBox.StandardButton.Yes))
        self.process.finished.connect(self.outputFinished)
        self.process.stateChanged.connect(self.processStateChanged)
        self.process.start(pythonExe,self.getArgs())

    @Slot()
    def readOutput(self):
        bytes_str = bytes(self.process.readAllStandardOutput())
        result = chardet.detect(bytes_str)
        output = bytes_str.decode(result['encoding'])
        self.outputTextEdit.appendPlainText(output)
        print(output)

    @Slot()
    def readError(self):
        bytes_str = bytes(self.process.readAllStandardError())
        result = chardet.detect(bytes_str)
        output = bytes_str.decode(result['encoding'])
        self.outputTextEdit.appendPlainText(output)
        QMessageBox.critical(self, '警告!出现一个错误', output, QMessageBox.StandardButton.Yes)
        print(output)

    @Slot(int)
    def processStateChanged(self, state):
        states = {
            QProcess.ProcessState.NotRunning: '线程未运行',
            QProcess.ProcessState.Starting: '线程正在启动',
            QProcess.ProcessState.Running: '线程正在运行',
        }
        currentState = states[state]
        self.ui.statusbar.showMessage(currentState)

    @Slot()
    def outputFinished(self):
        self.process = None

    # 基础页面的槽函数=============================================

    @Slot()
    def modifyPythonPath(self):
        pythonPath = self.ui.lePythonPath.text()
        self.ui.statusbar.showMessage(f'当前python路径为：{pythonPath}', 3000)
        self.pythonHome = os.path.dirname(pythonPath)
        self.userConfig['pythonHome'] = self.pythonHome
        os.environ['PYTHONHOME'] = self.userConfig['pythonHome']

    @Slot()
    def setOutPutIcon(self):
        filePath, fileType = QFileDialog.getOpenFileName(
            self, '请选择一个icon文件', '', 'Python Files (*.ico)')
        if filePath:
            self.ui.lineEdit.setText(filePath)
            self.iconPathChange(filePath)

    @Slot(str)
    def iconPathChange(self, filePath):
        self.argsDict['--windows-icon-from-ico'] = filePath

    @Slot()
    def setOutputPath(self):
        if filePath := QFileDialog.getExistingDirectory(self, '请选择输出路径', ''):
            self.ui.lineEdit_2.setText(filePath)
            self.outputPathChange(filePath)

    @Slot(str)
    def outputPathChange(self, value):
        self.argsDict['--output-dir'] = value

    # 插件页面的槽函数============================================
    @Slot()
    def addPlugin(self):
        currentSelect = self.ui.listUnselect.currentIndex().row()
        currentItem = self.ui.listUnselect.takeItem(currentSelect)
        self.ui.listSelect.addItem(currentItem)
        self.ui.statusbar.showMessage(f'添加了一个插件{currentItem.text()}', 3000)

        # 将参数启用
        for each in self.argsDict:
            if currentItem.text() in each:
                self.argsDict[each] = True

    @Slot()
    def removePlugin(self):
        currentSelect = self.ui.listSelect.currentIndex().row()
        currentItem = self.ui.listSelect.takeItem(currentSelect)
        self.ui.listUnselect.addItem(currentItem)
        self.ui.statusbar.showMessage(f'移除了一个插件{currentItem.text()}', 3000)

        # 将参数停用
        for each in self.argsDict:
            if currentItem.text() in each:
                self.argsDict[each] = False

    # 高级页面槽函数============================================

    @Slot(int)
    def jobsChange(self, value):
        self.argsDict['--jobs'] = value

    @Slot(str)
    def companyNameChange(self, value):
        self.argsDict['--windows-company-name'] = value

    @Slot(str)
    def fileVersionChange(self, value):
        self.argsDict['--windows-file-version'] = value

    @Slot(str)
    def productVersionChange(self, value):
        self.argsDict['--windows-product-version'] = value

    @Slot(str)
    def fileDescriptionChange(self, value):
        self.argsDict['--windows-product-name'] = value

    @Slot(str)
    def includeDataFilesChange(self, value):
        if self.ui.cbIncludeDataFiles.isChecked():
            self.argsDict['--include-data-file'] = value

    @Slot(str)
    def includeDataDirChange(self, value):
        if self.ui.cbIncludeDataDir.isChecked():
            self.argsDict['--include-data-dir'] = value


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
