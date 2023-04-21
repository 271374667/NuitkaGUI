import subprocess
import os
import resource_rc
from PySide6.QtWidgets import QApplication, QMainWindow, QWhatsThis, QFileDialog, QMessageBox, QPlainTextEdit
from PySide6.QtCore import Slot, QProcess
from Ui_nuitkaGUI import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pythonPath = self.getPythonPath()
        self.entryFilePath = ''
        self.statusbar = self.statusBar()
        
        self.outputTextEdit = QPlainTextEdit()
        self.outputTextEdit.setReadOnly(True)
        self.outputTextEdit.resize(800, 500)
        self.outputTextEdit.setWindowTitle('输出')
        
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

        self.initGUI()
        self.bind()

    def getPythonPath(self):
        process = subprocess.run(['where', 'python'], stdout=subprocess.PIPE)
        result = process.stdout.decode('utf-8')
        # 获取第一个路径
        result = result.split('\r')[0]
        # 切换到result所在的文件夹
        os.chdir(os.path.dirname(result))
        os.environ['PYTHONPATH'] = result
        
        print('当前发现路径存在于：', result)
        print('当前工作目录：', os.getcwd())
        return result

    def initGUI(self):
        self.whatthis = QWhatsThis()
        self.ui.lePythonPath.setText(self.pythonPath)
        try:
            import nuitka
        except ImportError:
            subprocess.call(['pip', 'install', 'nuitka', '-U'])

    def bind(self):
        # 打包模式
        self.ui.standalone.clicked.connect(self.argsToggle)
        self.ui.onefile.clicked.connect(self.argsToggle)

        # 基础页面
        self.ui.toolButton.clicked.connect(
            lambda: self.whatthis.enterWhatsThisMode())
        self.ui.btnGetPy.clicked.connect(self.getExecPyPath)
        self.ui.btnModifyingPythonPaths.clicked.connect(
            self.modifyingPythonPaths)
        self.ui.btnSetIcon.clicked.connect(self.setOutPutIcon)
        self.ui.lineEdit.textChanged.connect(self.iconPathChange)
        self.ui.btnSetOutputPath.clicked.connect(self.setOutputPath)
        self.ui.lineEdit_2.textChanged.connect(self.outputPathChange)
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
        self.ui.actionAbout.triggered.connect(lambda:QMessageBox.about(self, '关于', '作者：B-E-MAKE\n版本：1.0.0\n时间：2023-04-09\nPySide6学习欢迎加群633585910'))
        self.ui.actionShowArgs.triggered.connect(lambda:QMessageBox.about(self, '参数', str(self.getArgs())))
        
    # 公共槽函数============================================

    @Slot()
    def getExecPyPath(self):
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
        if isinstance(value, bool):
            if sender == self.ui.standalone:
                self.argsDict['--standalone'] = True
                self.argsDict['--onefile'] = False
                #self.argsDict['--onefile-tempdir-spec=./temp'] = False
            elif sender == self.ui.onefile:
                self.argsDict['--standalone'] = False
                self.argsDict['--onefile'] = True
                #self.argsDict['--onefile-tempdir-spec=./temp'] = True

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
        
        # print('='*50)
        # print(f'当前修改的参数为：{sender.objectName()}, 值为：{value}')
        # print(self.argsDict)

    @Slot()
    def startNuitka(self):
        # 开始前先判断是否有python路径以及入口文件
        if self.pythonPath == '':
            QMessageBox.warning(
                self, '警告', '请先选择python路径！', QMessageBox.StandardButton.Yes)
            return
        elif self.entryFilePath == '':
            QMessageBox.warning(
                self, '警告', '请先点击左上角选择入口文件(需要打包的py文件)！', QMessageBox.StandardButton.Yes)
            return

        self.outputTextEdit.clear()
        self.outputTextEdit.show()
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.readOutput)
        self.process.readyReadStandardError.connect(self.readError)
        self.process.finished.connect(lambda:self.process.deleteLater())
        self.process.finished.connect(lambda:QMessageBox.information(self, '提示', '运行结束！', QMessageBox.StandardButton.Yes))
        self.process.finished.connect(self.outputFinished)
        self.process.stateChanged.connect(self.processStateChanged)
        self.process.start(self.pythonPath, self.getArgs())
    
    @Slot()
    def readOutput(self):
        output = bytes(self.process.readAllStandardOutput()).decode('gbk')
        self.outputTextEdit.appendPlainText(output)
        print(output)
    
    @Slot()
    def readError(self):
        output = bytes(self.process.readAllStandardError()).decode('gbk')
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
        self.statusbar.showMessage(currentState)
    
    @Slot()
    def outputFinished(self):
        self.process = None

    # 基础页面的槽函数=============================================

    @Slot()
    def modifyPythonPath(self):
        self.pythonPath = self.ui.lePythonPath.text()
        self.statusbar.showMessage(f'当前python路径为：{self.pythonPath}', 3000)
        os.chdir(os.path.dirname(self.pythonPath))
        os.environ['PYTHONPATH'] = os.path.dirname(self.pythonPath)

    @Slot()
    def modifyingPythonPaths(self):
        filePath, fileType = QFileDialog.getOpenFileName(
            self, '请选择python.exe文件', '', 'Python Files (*.exe)')
        if filePath:
            self.ui.lePythonPath.setText(filePath)
            self.pythonPath = filePath
            os.chdir(os.path.dirname(self.pythonPath))
            self.statusBar().showMessage(f'当前python路径为：{filePath}', 3000)
            print(f'切换新的python路径为：{filePath}')
            os.environ['PYTHONPATH'] = os.path.dirname(self.pythonPath)

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
        self.statusbar.showMessage(f'添加了一个插件{currentItem.text()}', 3000)

        # 将参数启用
        for each in self.argsDict:
            if currentItem.text() in each:
                self.argsDict[each] = True

    @Slot()
    def removePlugin(self):
        currentSelect = self.ui.listSelect.currentIndex().row()
        currentItem = self.ui.listSelect.takeItem(currentSelect)
        self.ui.listUnselect.addItem(currentItem)
        self.statusbar.showMessage(f'移除了一个插件{currentItem.text()}', 3000)

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
