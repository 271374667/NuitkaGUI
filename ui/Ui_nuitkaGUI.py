# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuitkaGUIuceuwQ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                               QListWidget, QListWidgetItem, QMainWindow, QMenu,
                               QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
                               QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
                               QToolButton, QVBoxLayout, QWidget)

from ui.dragableqlineedit import DragableQLineEdit
from ui import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/images/icons8_compass_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icons8_wink_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionBatchMode = QAction(MainWindow)
        self.actionBatchMode.setObjectName(u"actionBatchMode")
        self.actionBatchMode.setEnabled(False)
        self.action_Dark = QAction(MainWindow)
        self.action_Dark.setObjectName(u"action_Dark")
        self.action_Dark.setEnabled(False)
        self.action_Bright = QAction(MainWindow)
        self.action_Bright.setObjectName(u"action_Bright")
        self.action_Bright.setEnabled(False)
        self.actionShowArgs = QAction(MainWindow)
        self.actionShowArgs.setObjectName(u"actionShowArgs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnLoadConfig = QPushButton(self.centralwidget)
        self.btnLoadConfig.setObjectName(u"btnLoadConfig")
        self.btnLoadConfig.setEnabled(True)
        self.btnLoadConfig.setMinimumSize(QSize(0, 36))
        self.btnLoadConfig.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.btnLoadConfig)

        self.btnSaveConfig = QPushButton(self.centralwidget)
        self.btnSaveConfig.setObjectName(u"btnSaveConfig")
        self.btnSaveConfig.setMinimumSize(QSize(0, 36))
        self.btnSaveConfig.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.btnSaveConfig)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnGetPy = QPushButton(self.centralwidget)
        self.btnGetPy.setObjectName(u"btnGetPy")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icons8_code_file_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGetPy.setIcon(icon2)
        self.btnGetPy.setIconSize(QSize(28, 28))

        self.verticalLayout.addWidget(self.btnGetPy)

        self.LinePyFilePath = QLabel(self.centralwidget)
        self.LinePyFilePath.setObjectName(u"LinePyFilePath")
        self.LinePyFilePath.setMinimumSize(QSize(20, 0))
        self.LinePyFilePath.setWordWrap(True)

        self.verticalLayout.addWidget(self.LinePyFilePath)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.standalone = QRadioButton(self.groupBox)
        self.standalone.setObjectName(u"standalone")
        self.standalone.setChecked(True)

        self.horizontalLayout.addWidget(self.standalone)

        self.onefile = QRadioButton(self.groupBox)
        self.onefile.setObjectName(u"onefile")

        self.horizontalLayout.addWidget(self.onefile)

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/icons8_puzzled_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QSize(32, 32))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.toolButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbShowProgress = QCheckBox(self.tab)
        self.cbShowProgress.setObjectName(u"cbShowProgress")
        self.cbShowProgress.setEnabled(True)
        self.cbShowProgress.setChecked(False)

        self.gridLayout.addWidget(self.cbShowProgress, 0, 0, 1, 1)

        self.cbShowMemory = QCheckBox(self.tab)
        self.cbShowMemory.setObjectName(u"cbShowMemory")

        self.gridLayout.addWidget(self.cbShowMemory, 0, 1, 1, 1)

        self.btnSetRequirements = QPushButton(self.tab)
        self.btnSetRequirements.setObjectName(u"btnSetRequirements")
        self.btnSetRequirements.setMaximumSize(QSize(165, 48))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/icons8_py_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSetRequirements.setIcon(icon4)
        self.btnSetRequirements.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btnSetRequirements, 1, 0, 1, 1)

        self.lePythonPath_2 = DragableQLineEdit(self.tab)
        self.lePythonPath_2.setObjectName(u"lePythonPath_2")
        self.lePythonPath_2.setMinimumSize(QSize(0, 40))
        self.lePythonPath_2.setDragEnabled(True)
        self.lePythonPath_2.setReadOnly(False)

        self.gridLayout.addWidget(self.lePythonPath_2, 1, 1, 1, 1)

        self.btnModifyingPythonPaths = QPushButton(self.tab)
        self.btnModifyingPythonPaths.setObjectName(u"btnModifyingPythonPaths")
        self.btnModifyingPythonPaths.setMaximumSize(QSize(165, 48))
        self.btnModifyingPythonPaths.setIcon(icon4)
        self.btnModifyingPythonPaths.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btnModifyingPythonPaths, 2, 0, 1, 1)

        self.lePythonPath = DragableQLineEdit(self.tab)
        self.lePythonPath.setObjectName(u"lePythonPath")
        self.lePythonPath.setMinimumSize(QSize(0, 40))
        self.lePythonPath.setDragEnabled(True)
        self.lePythonPath.setReadOnly(False)

        self.gridLayout.addWidget(self.lePythonPath, 2, 1, 1, 1)

        self.btnSetIcon = QPushButton(self.tab)
        self.btnSetIcon.setObjectName(u"btnSetIcon")
        self.btnSetIcon.setMinimumSize(QSize(0, 0))
        self.btnSetIcon.setIcon(icon1)
        self.btnSetIcon.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btnSetIcon, 3, 0, 1, 1)

        self.lineEdit = DragableQLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.btnSetOutputPath = QPushButton(self.tab)
        self.btnSetOutputPath.setObjectName(u"btnSetOutputPath")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/icons8_external_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSetOutputPath.setIcon(icon5)
        self.btnSetOutputPath.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btnSetOutputPath, 4, 0, 1, 1)

        self.lineEdit_2 = DragableQLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.listUnselect = QListWidget(self.tab_3)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        QListWidgetItem(self.listUnselect)
        self.listUnselect.setObjectName(u"listUnselect")

        self.verticalLayout_5.addWidget(self.listUnselect)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btnAddPlugin = QToolButton(self.tab_3)
        self.btnAddPlugin.setObjectName(u"btnAddPlugin")
        self.btnAddPlugin.setArrowType(Qt.RightArrow)

        self.verticalLayout_6.addWidget(self.btnAddPlugin)

        self.btnRemovePlugin = QToolButton(self.tab_3)
        self.btnRemovePlugin.setObjectName(u"btnRemovePlugin")
        self.btnRemovePlugin.setArrowType(Qt.LeftArrow)

        self.verticalLayout_6.addWidget(self.btnRemovePlugin)

        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.listSelect = QListWidget(self.tab_3)
        self.listSelect.setObjectName(u"listSelect")

        self.verticalLayout_7.addWidget(self.listSelect)

        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.plainTextEdit = QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(10000, 57))
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.plainTextEdit)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cbDisableCcache = QCheckBox(self.tab_2)
        self.cbDisableCcache.setObjectName(u"cbDisableCcache")

        self.gridLayout_2.addWidget(self.cbDisableCcache, 1, 1, 1, 1)

        self.cbNoFollowImports = QCheckBox(self.tab_2)
        self.cbNoFollowImports.setObjectName(u"cbNoFollowImports")

        self.gridLayout_2.addWidget(self.cbNoFollowImports, 0, 2, 1, 1)

        self.cbRemoveOutput = QCheckBox(self.tab_2)
        self.cbRemoveOutput.setObjectName(u"cbRemoveOutput")

        self.gridLayout_2.addWidget(self.cbRemoveOutput, 0, 0, 1, 1)

        self.cbFollowImports = QCheckBox(self.tab_2)
        self.cbFollowImports.setObjectName(u"cbFollowImports")

        self.gridLayout_2.addWidget(self.cbFollowImports, 1, 2, 1, 1)

        self.cbLowMemory = QCheckBox(self.tab_2)
        self.cbLowMemory.setObjectName(u"cbLowMemory")

        self.gridLayout_2.addWidget(self.cbLowMemory, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(78, 16777215))
        self.label_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.jobs = QSpinBox(self.tab_2)
        self.jobs.setObjectName(u"jobs")
        self.jobs.setMinimum(1)
        self.jobs.setMaximum(64)
        self.jobs.setValue(8)

        self.horizontalLayout_7.addWidget(self.jobs)

        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.cbIncludeDataFiles = QCheckBox(self.tab_2)
        self.cbIncludeDataFiles.setObjectName(u"cbIncludeDataFiles")
        self.cbIncludeDataFiles.setEnabled(True)

        self.gridLayout_2.addWidget(self.cbIncludeDataFiles, 2, 0, 1, 1)

        self.cbIncludeDataDir = QCheckBox(self.tab_2)
        self.cbIncludeDataDir.setObjectName(u"cbIncludeDataDir")
        self.cbIncludeDataDir.setEnabled(True)

        self.gridLayout_2.addWidget(self.cbIncludeDataDir, 2, 1, 1, 1)

        self.cbDisableConsole = QCheckBox(self.tab_2)
        self.cbDisableConsole.setObjectName(u"cbDisableConsole")

        self.gridLayout_2.addWidget(self.cbDisableConsole, 2, 2, 1, 1)

        self.cbQuiet = QCheckBox(self.tab_2)
        self.cbQuiet.setObjectName(u"cbQuiet")

        self.gridLayout_2.addWidget(self.cbQuiet, 3, 2, 1, 1)

        self.lineEditIncludeDataFiles = DragableQLineEdit(self.tab_2)
        self.lineEditIncludeDataFiles.setObjectName(u"lineEditIncludeDataFiles")
        self.lineEditIncludeDataFiles.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineEditIncludeDataFiles, 3, 0, 1, 1)

        self.lineEditIncludeDataDir = DragableQLineEdit(self.tab_2)
        self.lineEditIncludeDataDir.setObjectName(u"lineEditIncludeDataDir")
        self.lineEditIncludeDataDir.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineEditIncludeDataDir, 3, 1, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.lineEditCompanyName = QLineEdit(self.tab_2)
        self.lineEditCompanyName.setObjectName(u"lineEditCompanyName")

        self.verticalLayout_4.addWidget(self.lineEditCompanyName)

        self.lineEditFileVersion = QLineEdit(self.tab_2)
        self.lineEditFileVersion.setObjectName(u"lineEditFileVersion")

        self.verticalLayout_4.addWidget(self.lineEditFileVersion)

        self.lineEditProductVersion = QLineEdit(self.tab_2)
        self.lineEditProductVersion.setObjectName(u"lineEditProductVersion")

        self.verticalLayout_4.addWidget(self.lineEditProductVersion)

        self.lineEditFileDescription = QLineEdit(self.tab_2)
        self.lineEditFileDescription.setObjectName(u"lineEditFileDescription")

        self.verticalLayout_4.addWidget(self.lineEditFileDescription)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/images/images/icons8_start_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStart.setIcon(icon6)
        self.btnStart.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.btnStart)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menu_2)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionAbout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionBatchMode)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.actionShowArgs)
        self.menu_3.addAction(self.action_Dark)
        self.menu_3.addAction(self.action_Bright)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        self.cbIncludeDataFiles.clicked["bool"].connect(self.lineEditIncludeDataFiles.setEnabled)
        self.cbIncludeDataDir.clicked["bool"].connect(self.lineEditIncludeDataDir.setEnabled)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NuitkaGUI", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionBatchMode.setText(QCoreApplication.translate("MainWindow", u"\u6279\u5904\u7406\u6a21\u5f0f", None))
        self.action_Dark.setText(QCoreApplication.translate("MainWindow", u"\u6697\u9ed1", None))
        self.action_Bright.setText(QCoreApplication.translate("MainWindow", u"\u660e\u4eae", None))
        self.actionShowArgs.setText(
            QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u5f53\u524d\u53c2\u6570", None))
        self.btnLoadConfig.setText(
            QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u914d\u7f6e\u6587\u4ef6", None))
        self.btnSaveConfig.setText(
            QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e\u6587\u4ef6", None))
        self.btnGetPy.setText(
            QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9879\u76ee\u5165\u53e3\u6587\u4ef6", None))
        self.LinePyFilePath.setText(
            QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6ca1\u6709\u9009\u62e9\u4efb\u4f55py\u6587\u4ef6",
                                       None))
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u60a8\u7684\u6253\u5305\u7b56\u7565", None))
        # if QT_CONFIG(tooltip)
        self.standalone.setToolTip(QCoreApplication.translate("MainWindow", u"standalone", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.standalone.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p>\u751f\u6210\u4e00\u4e2a\u6587\u4ef6\u5939\uff0c\u53ef\u8fd0\u884c\u6587\u4ef6\u5728\u8fd9\u4e2a\u6587\u4ef6\u5939\u91cc\u9762</p><p>\u540c\u65f6\u8fd9\u4e2a\u6587\u4ef6\u5939\u91cc\u9762\u8fd8\u6709\u5f88\u591a\u5176\u4ed6\u7684\u5185\u5bb9</p><p>\u4f7f\u7528\u8fd9\u79cd\u65b9\u6cd5\u76f8\u5bf9\u4e8e\u5355\u6587\u4ef6\u4e0d\u5bb9\u6613\u62a5\u9519\uff0c\u4f46\u662f\u65b0\u624b\u53ef\u80fd\u627e\u4e0d\u5230\u53ef\u6267\u884c\u6587\u4ef6</p></body></html>",
                                                                None))
        # endif // QT_CONFIG(whatsthis)
        self.standalone.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u4e3a\u591a\u6587\u4ef6\n"
                                                                         "--standalone", None))
        # if QT_CONFIG(tooltip)
        self.onefile.setToolTip(QCoreApplication.translate("MainWindow", u"onefile", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.onefile.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                             u"<html><head/><body><p>\u6253\u5305\u51fa\u6765\u7684\u6587\u4ef6\u662f\u5355\u4e2aexe\u6587\u4ef6\uff0c\u65b9\u4fbf\u4f20\u64ad\uff0c\u4f46\u662f\u4e0d\u65b9\u4fbf\u8c03\u8bd5</p><p>\u901a\u5e38\u90fd\u662f\u591a\u6587\u4ef6\u8fd0\u884c\u6210\u529f\u4ee5\u540e\u624d\u4f1a\u4f7f\u7528\u8fd9\u4e2a</p><p>\u8be5\u547d\u4ee4\u4f1a\u540c\u65f6\u5f00\u542f--windows-onefile-tempdir-spec=./temp</p></body></html>",
                                                             None))
        # endif // QT_CONFIG(whatsthis)
        self.onefile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u4e3a\u5355\u6587\u4ef6\n"
                                                                      "--onefile", None))
        # if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("MainWindow",
                                                              u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762",
                                                              None))
        # endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        # if QT_CONFIG(tooltip)
        self.cbShowProgress.setToolTip(QCoreApplication.translate("MainWindow", u"show-progress", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbShowProgress.setWhatsThis(QCoreApplication.translate("MainWindow", u"show-progress", None))
        # endif // QT_CONFIG(whatsthis)
        self.cbShowProgress.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8fdb\u5ea6\u6761\n"
                                                                             "--show-progress", None))
        # if QT_CONFIG(tooltip)
        self.cbShowMemory.setToolTip(QCoreApplication.translate("MainWindow", u"show-memory", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbShowMemory.setWhatsThis(QCoreApplication.translate("MainWindow", u"show-memory", None))
        # endif // QT_CONFIG(whatsthis)
        self.cbShowMemory.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5185\u5b58\u5360\u7528\n"
                                                                           "-show-memory", None))
        self.btnSetRequirements.setText(QCoreApplication.translate("MainWindow", u"Requirements\u8def\u5f84", None))
        self.lePythonPath_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u914d\u7f6erequirements.txt\u5b89\u88c5\u4f9d\u8d56", None))
        self.btnModifyingPythonPaths.setText(
            QCoreApplication.translate("MainWindow", u"\u4fee\u6539Python\u8def\u5f84", None))
        self.lePythonPath.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                        u"\u5f53\u524d\u7684Python\u8def\u5f84\u672a\u521d\u59cb\u5316\uff01",
                                                                        None))
        self.btnSetIcon.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u56fe\u6807", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                    u"\u8fd9\u91cc\u653e\u7f6e\u56fe\u6807\uff0c\u53ef\u4ee5\u76f4\u63a5\u62d6\u5165",
                                                                    None))
        self.btnSetOutputPath.setText(
            QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                      u"\u5728\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u53ef\u4ee5\u4f7f\u7528\u62d6\u62fd\u7684\u65b9\u5f0f",
                                                                      None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u672a\u542f\u7528\u7684\u63d2\u4ef6", None))

        __sortingEnabled = self.listUnselect.isSortingEnabled()
        self.listUnselect.setSortingEnabled(False)
        ___qlistwidgetitem = self.listUnselect.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"pyside6", None));
        ___qlistwidgetitem1 = self.listUnselect.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"pyside2", None));
        ___qlistwidgetitem2 = self.listUnselect.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"pyqt6", None));
        ___qlistwidgetitem3 = self.listUnselect.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"pyqt5", None));
        ___qlistwidgetitem4 = self.listUnselect.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"matplotlib", None));
        ___qlistwidgetitem5 = self.listUnselect.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"tensorflow", None));
        ___qlistwidgetitem6 = self.listUnselect.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"tk-inter", None));
        ___qlistwidgetitem7 = self.listUnselect.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"pywebview", None));
        ___qlistwidgetitem8 = self.listUnselect.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"upx", None));
        ___qlistwidgetitem9 = self.listUnselect.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"multiprocessing", None));
        ___qlistwidgetitem10 = self.listUnselect.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"trio", None));
        ___qlistwidgetitem11 = self.listUnselect.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"kivy", None));
        self.listUnselect.setSortingEnabled(__sortingEnabled)

        self.btnAddPlugin.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnRemovePlugin.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u5df2\u7ecf\u542f\u7528\u7684\u63d2\u4ef6", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow",
                                                                   u"\u5982\u679c\u4f60\u5bfc\u5165\u4e86\u76f8\u5e94\u7684\u6a21\u5757\uff0c\u90a3\u4e48\u4f60\u9700\u8981\u4ece\u5de6\u8fb9\u9009\u62e9\u5bf9\u5e94\u7684\u63d2\u4ef6\uff0c\u7136\u540e\u53cc\u51fb\u4ed6\u6216\u8005\u70b9\u51fb\u6309\u94ae\u5c06\u5b83\u6dfb\u52a0\u5230\u53f3\u8fb9\n"
                                                                   "\n"
                                                                   "\u8fd9\u6837\u505a\u80fd\u591f\u8ba9\u4f60\u66f4\u5feb\u7684\u7f16\u8bd1\uff0c\u800c\u4e14\u6709\u7684\u65f6\u5019\u5982\u679c\u4f60\u6ca1\u6709\u5f00\u542f\u63d2\u4ef6\u6700\u540e\u751a\u81f3\u53ef\u80fd\u65e0\u6cd5\u8fd0\u884c\uff0c\u6bd4\u5982PyQt",
                                                                   None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u63d2\u4ef6", None))
        # if QT_CONFIG(tooltip)
        self.cbDisableCcache.setToolTip(QCoreApplication.translate("MainWindow",
                                                                   u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                                   None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbDisableCcache.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                     u"\u5f53\u4f60\u9891\u7e41\u6253\u5305\u5931\u8d25\u7684\u65f6\u5019\u53ef\u4ee5\u5f00\u8d77\u6765\uff0c\u5e73\u65f6\u5c3d\u91cf\u5173\u95ed\uff0c\u5173\u95ed\u8fd9\u4e2a\u9009\u9879\u80fd\u52a0\u5feb\u6253\u5305\u901f\u5ea6",
                                                                     None))
        # endif // QT_CONFIG(whatsthis)
        self.cbDisableCcache.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u6e05\u9664\u4e0a\u4e00\u6b21\u7684\u7f13\u5b58\uff0c\u9632\u6b62\u6253\u5305\u5931\u8d25\n"
                                                                "disable-ccache", None))
        # if QT_CONFIG(tooltip)
        self.cbNoFollowImports.setToolTip(QCoreApplication.translate("MainWindow", u"nofollow-imports", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbNoFollowImports.setWhatsThis(QCoreApplication.translate("MainWindow", u"nofollow-imports", None))
        # endif // QT_CONFIG(whatsthis)
        self.cbNoFollowImports.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u4e0d\u5bfc\u5165\u4efb\u4f55\u6a21\u5757(\u4e0d\u9002\u5408\u5355\u6587\u4ef6)\n"
                                                                  "--nofollow-imports", None))
        # if QT_CONFIG(tooltip)
        self.cbRemoveOutput.setToolTip(QCoreApplication.translate("MainWindow", u"remove-output", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbRemoveOutput.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
        # endif // QT_CONFIG(whatsthis)
        self.cbRemoveOutput.setText(
            QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939\n"
                                                     "remove-output", None))
        # if QT_CONFIG(tooltip)
        self.cbFollowImports.setToolTip(QCoreApplication.translate("MainWindow",
                                                                   u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                                   None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbFollowImports.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                     u"\u5982\u679c\u4f60\u5bfc\u5165\u4e86\u5f88\u591a\u7b2c\u4e09\u65b9\u5e93\uff0c\u8bf7\u52a1\u5fc5\u5f00\u542f\u8fd9\u4e2a\u9009\u9879",
                                                                     None))
        # endif // QT_CONFIG(whatsthis)
        self.cbFollowImports.setText(
            QCoreApplication.translate("MainWindow", u"\u9012\u5f52\u67e5\u627e\u6240\u6709\u7684\u6a21\u5757\n"
                                                     "--follow-imports", None))
        # if QT_CONFIG(tooltip)
        self.cbLowMemory.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6",
                                       None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbLowMemory.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6",
                                       None))
        # endif // QT_CONFIG(whatsthis)
        self.cbLowMemory.setText(
            QCoreApplication.translate("MainWindow", u"\u7f16\u8bd1\u65f6\u5360\u7528\u66f4\u5c11\u7684\u5185\u5b58\n"
                                                     "low-memory", None))
        # if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow",
                                                           u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                           None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                             u"\u8bf7\u4e0d\u8981\u8bbe\u7f6e\u5927\u4e8e\u81ea\u5df1\u7535\u8111\u6838\u5fc3\u7684\u7ebf\u7a0b\uff0c\u901a\u5e38\u8bbe\u7f6e\u4e3a6\u6216\u80058\u5373\u53ef",
                                                             None))
        # endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u5f00\u542f\u7684\u7ebf\u7a0b\u6570<br/>jobs</p></body></html>",
                                                        None))
        # if QT_CONFIG(tooltip)
        self.cbIncludeDataFiles.setToolTip(QCoreApplication.translate("MainWindow", u"include-data-files", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbIncludeDataFiles.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                        u"<html><head/><body><p>\u5bf9\u4e8e\u8981\u5305\u542b\u7684\u6570\u636e\u6587\u4ef6\uff0c\u8bf7\u4f7f\u7528\u9009\u9879 --include-data-files=&lt;source&gt;=&lt;target&gt; \uff0c\u5176\u4e2d\u6e90\u662f\u6587\u4ef6\u7cfb\u7edf\u8def\u5f84\uff0c\u4f46\u5fc5\u987b\u6307\u5b9a\u76f8\u5bf9\u76ee\u6807\u3002\u5bf9\u4e8e\u72ec\u7acb\uff0c\u60a8\u4e5f\u53ef\u4ee5\u624b\u52a8\u590d\u5236\u5b83\u4eec\uff0c\u4f46\u8fd9\u53ef\u4ee5\u8fdb\u884c\u989d\u5916\u7684\u68c0\u67e5\uff0c\u5bf9\u4e8e\u5355\u6587\u4ef6\u6a21\u5f0f\uff0c\u65e0\u6cd5\u624b\u52a8\u590d\u5236\u3002</p><p>\u8981\u590d\u5236\u76ee\u5f55\u4e2d\u7684\u90e8\u5206\u6216\u5168\u90e8\u6587\u4ef6\uff0c\u8bf7\u4f7f\u7528\u9009\u9879 --include-data-files=/etc/*.txt=etc/ \uff0c\u60a8\u53ef\u4ee5\u5728\u5176\u4e2d\u6307\u5b9a\u6587\u4ef6\u7684 shell \u6a21\u5f0f\uff0c\u4ee5\u53ca\u653e\u7f6e\u5b83\u4eec\u7684\u5b50\u76ee\u5f55\uff0c\u7531\u5c3e\u90e8\u659c\u6760\u6307\u793a\u3002</p></body></html>",
                                                                        None))
        # endif // QT_CONFIG(whatsthis)
        self.cbIncludeDataFiles.setText(
            QCoreApplication.translate("MainWindow", u"\u6253\u5305\u989d\u5916\u7684\u6587\u4ef6\n"
                                                     "--include-data-files", None))
        # if QT_CONFIG(tooltip)
        self.cbIncludeDataDir.setToolTip(QCoreApplication.translate("MainWindow", u"include-data-dir", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbIncludeDataDir.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                      u"\u8981\u590d\u5236\u5305\u542b\u6240\u6709\u6587\u4ef6\u7684\u6574\u4e2a\u6587\u4ef6\u5939\uff0c\u60a8\u53ef\u4ee5\u4f7f\u7528 --include-data-dir=/path/to/images=images \uff0c\u5b83\u5c06\u590d\u5236\u6240\u6709\u6587\u4ef6\uff0c\u5305\u62ec\u6f5c\u5728\u7684\u5b50\u76ee\u5f55\u7ed3\u6784\u3002\u60a8\u4e0d\u80fd\u5728\u6b64\u5904\u8fc7\u6ee4\uff0c\u5373\u5982\u679c\u60a8\u53ea\u60f3\u8981\u90e8\u5206\u526f\u672c\uff0c\u8bf7\u4e8b\u5148\u5220\u9664\u6587\u4ef6\u3002",
                                                                      None))
        # endif // QT_CONFIG(whatsthis)
        self.cbIncludeDataDir.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u6253\u5305\u989d\u5916\u7684\u6587\u4ef6\u5939\u4ee5\u53ca\u6587\u4ef6\u5939\u4e0b\u6240\u6709\u7684\u5185\u5bb9\n"
                                                                 "--include-data-dir", None))
        # if QT_CONFIG(tooltip)
        self.cbDisableConsole.setToolTip(QCoreApplication.translate("MainWindow",
                                                                    u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                                    None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbDisableConsole.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                      u"\u8bf7\u4e0d\u8981\u5728\u4e00\u5f00\u59cb\u76f4\u63a5\u4f7f\u7528\uff0c\u8bf7\u786e\u4fdd\u81ea\u5df1\u7684\u7a0b\u5e8f\u6253\u5305\u4e4b\u540e\u80fd\u591f\u8fd0\u884c\u518d\u5f00\u542f\u8fd9\u4e2a\u9009\u9879",
                                                                      None))
        # endif // QT_CONFIG(whatsthis)
        self.cbDisableConsole.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u547d\u4ee4\u884c\n"
                                                                               "--windows-disable-console", None))
        # if QT_CONFIG(tooltip)
        self.cbQuiet.setToolTip(QCoreApplication.translate("MainWindow",
                                                           u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                           None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cbQuiet.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"\u8fd9\u4e2a\u9009\u9879\u53ea\u4f1a\u8f93\u51fa\u9519\u8bef",
                                       None))
        # endif // QT_CONFIG(whatsthis)
        self.cbQuiet.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u5f00\u542f\u5b89\u9759\u6253\u5305\u6a21\u5f0f(\u53ea\u8f93\u51fa\u9519\u8bef)\n"
                                                        "--quiet", None))
        # if QT_CONFIG(tooltip)
        self.lineEditIncludeDataFiles.setToolTip(QCoreApplication.translate("MainWindow",
                                                                            u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                                            None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEditIncludeDataFiles.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                              u"<html><head/><body><p>\u53ef\u4ee5\u901a\u8fc7/path/to/file/*.txt\u7684\u5f62\u5f0f\u83b7\u53d6\u591a\u4e2a\u6587\u4ef6</p><p>\u540c\u6837\u4e5f\u53ef\u4ee5\u901a\u8fc7\u62d6\u62fd\u7684\u5f62\u5f0f\u53ea\u6253\u5305\u4e00\u4e2a\u6587\u4ef6</p><p>\u5982\u679c\u662f\u591a\u6587\u4ef6\u6253\u5305\u63a8\u8350\u5c3d\u91cf\u4e0d\u8981\u6253\u5305\u6570\u636e\u6587\u4ef6\uff0c\u5728\u8fd0\u884c\u4e4b\u540e\u518d\u624b\u52a8\u653e\u5165\u6570\u636e\u6587\u4ef6</p><p><br/></p></body></html>",
                                                                              None))
        # endif // QT_CONFIG(whatsthis)
        self.lineEditIncludeDataFiles.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                    u"\u989d\u5916\u7684\u6587\u4ef6(\u53ef\u4ee5\u8fdb\u5165WhatThis\u6a21\u5f0f\u67e5\u770b\u8be6\u7ec6\u8bf4\u660e)",
                                                                                    None))
        # if QT_CONFIG(tooltip)
        self.lineEditIncludeDataDir.setToolTip(QCoreApplication.translate("MainWindow",
                                                                          u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc",
                                                                          None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEditIncludeDataDir.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                            u"\u53ef\u4ee5\u62d6\u62fd\uff0c\u8be5\u9009\u9879\u4f1a\u6253\u5305\u6587\u4ef6\u5939\u4e0b\u7684\u6240\u6709\u5185\u5bb9",
                                                                            None))
        # endif // QT_CONFIG(whatsthis)
        self.lineEditIncludeDataDir.setText("")
        self.lineEditIncludeDataDir.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                  u"\u989d\u5916\u7684\u6587\u4ef6\u5939\u4ee5\u53ca\u6587\u4ef6\u5939\u4e0b\u6240\u6709\u7684\u5185\u5bb9",
                                                                                  None))
        # if QT_CONFIG(tooltip)
        self.lineEditCompanyName.setToolTip(QCoreApplication.translate("MainWindow",
                                                                       u"\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u516c\u53f8\u540d\u79f0\u3002",
                                                                       None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEditCompanyName.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                         u"\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u516c\u53f8\u540d\u79f0\u3002",
                                                                         None))
        # endif // QT_CONFIG(whatsthis)
        self.lineEditCompanyName.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"windows-company-name", None))
        # if QT_CONFIG(tooltip)
        self.lineEditFileVersion.setToolTip(QCoreApplication.translate("MainWindow",
                                                                       u"\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u6587\u4ef6\u7248\u672c\u3002",
                                                                       None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEditFileVersion.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                         u"<html><head/><body><p>\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u6587\u4ef6\u7248\u672c\u3002</p><p>\u6ce8\u610f\u7248\u672c\u53f7\u5fc5\u987b\u8981\u6709\u56db\u4e2a\u6570\u5b57\uff0c\u6bd4\u59821.0.0.0</p><p><br/></p></body></html>",
                                                                         None))
        # endif // QT_CONFIG(whatsthis)
        self.lineEditFileVersion.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                               u"windows-file-version(\u5fc5\u987b\u662f4\u4f4d\u6570,\u6bd4\u59821.0.0.0)",
                                                                               None))
        # if QT_CONFIG(tooltip)
        self.lineEditProductVersion.setToolTip(QCoreApplication.translate("MainWindow",
                                                                          u"\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u4ea7\u54c1\u7248\u672c\u3002",
                                                                          None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEditProductVersion.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                            u"<html><head/><body><p>\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u4ea7\u54c1\u7248\u672c\u3002</p><p>\u6ce8\u610f\u7248\u672c\u53f7\u5fc5\u987b\u8981\u6709\u56db\u4e2a\u6570\u5b57\uff0c\u6bd4\u59821.0.0.0</p><p><br/></p></body></html>",
                                                                            None))
        # endif // QT_CONFIG(whatsthis)
        self.lineEditProductVersion.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                  u"windows-product-version(\u5fc5\u987b\u662f4\u4f4d\u6570,\u6bd4\u59821.0.0.0)",
                                                                                  None))
        # if QT_CONFIG(tooltip)
        self.lineEditFileDescription.setToolTip(QCoreApplication.translate("MainWindow",
                                                                           u"\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u6587\u4ef6\u63cf\u8ff0\u3002",
                                                                           None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lineEditFileDescription.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                             u"\u5728\u53ef\u6267\u884c\u6587\u4ef6\u7684\u7248\u672c\u4fe1\u606f\u4e2d\u6dfb\u52a0\u6587\u4ef6\u63cf\u8ff0\u3002",
                                                                             None))
        # endif // QT_CONFIG(whatsthis)
        self.lineEditFileDescription.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"windows-file-description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u53c2\u6570", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6253\u5305", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u76ae\u80a4", None))
    # retranslateUi
