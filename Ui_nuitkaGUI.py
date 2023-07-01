# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuitkaGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

from dragableqlineedit import DragableQLineEdit
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 619)
        icon = QIcon()
        icon.addFile(u":/images/images/icons8_compass_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/images/icons8_compass_30px.png", QSize(), QIcon.Normal, QIcon.On)
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/images/images/icons8_start_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStart.setIcon(icon4)
        self.btnStart.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btnStart, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CBShowProgress = QCheckBox(self.tab)
        self.CBShowProgress.setObjectName(u"CBShowProgress")
        self.CBShowProgress.setEnabled(True)
        self.CBShowProgress.setChecked(False)

        self.gridLayout.addWidget(self.CBShowProgress, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BTNSetOutputPath = QPushButton(self.tab)
        self.BTNSetOutputPath.setObjectName(u"BTNSetOutputPath")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/icons8_external_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTNSetOutputPath.setIcon(icon5)
        self.BTNSetOutputPath.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.BTNSetOutputPath)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.CBShowMemory = QCheckBox(self.tab)
        self.CBShowMemory.setObjectName(u"CBShowMemory")

        self.gridLayout.addWidget(self.CBShowMemory, 0, 1, 1, 1)

        self.LEIcon = DragableQLineEdit(self.tab)
        self.LEIcon.setObjectName(u"LEIcon")
        self.LEIcon.setMinimumSize(QSize(0, 40))
        self.LEIcon.setDragEnabled(True)
        self.LEIcon.setReadOnly(False)

        self.gridLayout.addWidget(self.LEIcon, 1, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BTNSetIcon = QPushButton(self.tab)
        self.BTNSetIcon.setObjectName(u"BTNSetIcon")
        self.BTNSetIcon.setMinimumSize(QSize(0, 0))
        self.BTNSetIcon.setIcon(icon1)
        self.BTNSetIcon.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.BTNSetIcon)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.LEOutpuPath = DragableQLineEdit(self.tab)
        self.LEOutpuPath.setObjectName(u"LEOutpuPath")
        self.LEOutpuPath.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.LEOutpuPath, 2, 1, 1, 1)

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
        self.BTNAddPlugin = QToolButton(self.tab_3)
        self.BTNAddPlugin.setObjectName(u"BTNAddPlugin")
        self.BTNAddPlugin.setArrowType(Qt.RightArrow)

        self.verticalLayout_6.addWidget(self.BTNAddPlugin)

        self.BTNRemovePlugin = QToolButton(self.tab_3)
        self.BTNRemovePlugin.setObjectName(u"BTNRemovePlugin")
        self.BTNRemovePlugin.setArrowType(Qt.LeftArrow)

        self.verticalLayout_6.addWidget(self.BTNRemovePlugin)


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
        self.plainTextEdit.setMaximumSize(QSize(10000, 86))
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.plainTextEdit)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 390, 476))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(78, 16777215))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.jobs = QSpinBox(self.groupBox_2)
        self.jobs.setObjectName(u"jobs")
        self.jobs.setMinimum(1)
        self.jobs.setMaximum(64)
        self.jobs.setValue(8)

        self.horizontalLayout_7.addWidget(self.jobs)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)

        self.CBLowMemory = QCheckBox(self.groupBox_2)
        self.CBLowMemory.setObjectName(u"CBLowMemory")

        self.horizontalLayout_3.addWidget(self.CBLowMemory)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 180))
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CBDisableCcache = QCheckBox(self.groupBox_4)
        self.CBDisableCcache.setObjectName(u"CBDisableCcache")

        self.gridLayout_5.addWidget(self.CBDisableCcache, 0, 0, 1, 1)

        self.CBQuiet = QCheckBox(self.groupBox_4)
        self.CBQuiet.setObjectName(u"CBQuiet")

        self.gridLayout_5.addWidget(self.CBQuiet, 1, 0, 1, 1)

        self.CBFollowImports = QCheckBox(self.groupBox_4)
        self.CBFollowImports.setObjectName(u"CBFollowImports")

        self.gridLayout_5.addWidget(self.CBFollowImports, 0, 1, 1, 1)

        self.CBCleanCache = QCheckBox(self.groupBox_4)
        self.CBCleanCache.setObjectName(u"CBCleanCache")

        self.gridLayout_5.addWidget(self.CBCleanCache, 2, 1, 1, 1)

        self.CBDisableConsole = QCheckBox(self.groupBox_4)
        self.CBDisableConsole.setObjectName(u"CBDisableConsole")

        self.gridLayout_5.addWidget(self.CBDisableConsole, 2, 0, 1, 1)

        self.CBRemoveOutput = QCheckBox(self.groupBox_4)
        self.CBRemoveOutput.setObjectName(u"CBRemoveOutput")

        self.gridLayout_5.addWidget(self.CBRemoveOutput, 1, 1, 1, 1)

        self.CBMingw64 = QCheckBox(self.groupBox_4)
        self.CBMingw64.setObjectName(u"CBMingw64")
        self.CBMingw64.setEnabled(True)
        self.CBMingw64.setChecked(False)

        self.gridLayout_5.addWidget(self.CBMingw64, 3, 0, 1, 1)

        self.CBLto = QCheckBox(self.groupBox_4)
        self.CBLto.setObjectName(u"CBLto")
        self.CBLto.setEnabled(True)
        self.CBLto.setChecked(False)

        self.gridLayout_5.addWidget(self.CBLto, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 197))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.LEFileVersion = QLineEdit(self.groupBox_3)
        self.LEFileVersion.setObjectName(u"LEFileVersion")

        self.gridLayout_4.addWidget(self.LEFileVersion, 1, 1, 1, 1)

        self.LBProductVersion = QLabel(self.groupBox_3)
        self.LBProductVersion.setObjectName(u"LBProductVersion")
        sizePolicy1.setHeightForWidth(self.LBProductVersion.sizePolicy().hasHeightForWidth())
        self.LBProductVersion.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.LBProductVersion, 2, 0, 1, 1)

        self.LECompanyName = QLineEdit(self.groupBox_3)
        self.LECompanyName.setObjectName(u"LECompanyName")

        self.gridLayout_4.addWidget(self.LECompanyName, 0, 1, 1, 1)

        self.LBFileVersion = QLabel(self.groupBox_3)
        self.LBFileVersion.setObjectName(u"LBFileVersion")
        sizePolicy1.setHeightForWidth(self.LBFileVersion.sizePolicy().hasHeightForWidth())
        self.LBFileVersion.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.LBFileVersion, 1, 0, 1, 1)

        self.LEProductVersion = QLineEdit(self.groupBox_3)
        self.LEProductVersion.setObjectName(u"LEProductVersion")

        self.gridLayout_4.addWidget(self.LEProductVersion, 2, 1, 1, 1)

        self.LBCompanyName = QLabel(self.groupBox_3)
        self.LBCompanyName.setObjectName(u"LBCompanyName")
        sizePolicy1.setHeightForWidth(self.LBCompanyName.sizePolicy().hasHeightForWidth())
        self.LBCompanyName.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.LBCompanyName, 0, 0, 1, 1)

        self.LBFileDescription = QLabel(self.groupBox_3)
        self.LBFileDescription.setObjectName(u"LBFileDescription")
        sizePolicy1.setHeightForWidth(self.LBFileDescription.sizePolicy().hasHeightForWidth())
        self.LBFileDescription.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.LBFileDescription, 3, 0, 1, 1)

        self.LEFileDescription = QLineEdit(self.groupBox_3)
        self.LEFileDescription.setObjectName(u"LEFileDescription")

        self.gridLayout_4.addWidget(self.LEFileDescription, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_3 = QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.PTEArgsOutput = QPlainTextEdit(self.tab_4)
        self.PTEArgsOutput.setObjectName(u"PTEArgsOutput")
        self.PTEArgsOutput.setMaximumSize(QSize(16777215, 50))
        self.PTEArgsOutput.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.PTEArgsOutput)

        self.scrollArea_2 = QScrollArea(self.tab_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 517, 526))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.PTEExplaineCompatibility = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PTEExplaineCompatibility.setObjectName(u"PTEExplaineCompatibility")
        self.PTEExplaineCompatibility.setMinimumSize(QSize(0, 150))
        self.PTEExplaineCompatibility.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.PTEExplaineCompatibility.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.PTEExplaineCompatibility)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.ListUnselectMod = QListWidget(self.scrollAreaWidgetContents_2)
        self.ListUnselectMod.setObjectName(u"ListUnselectMod")
        self.ListUnselectMod.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_9.addWidget(self.ListUnselectMod)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BTNAddMod = QToolButton(self.scrollAreaWidgetContents_2)
        self.BTNAddMod.setObjectName(u"BTNAddMod")
        self.BTNAddMod.setArrowType(Qt.RightArrow)

        self.verticalLayout_10.addWidget(self.BTNAddMod)

        self.BTNRemoveMod = QToolButton(self.scrollAreaWidgetContents_2)
        self.BTNRemoveMod.setObjectName(u"BTNRemoveMod")
        self.BTNRemoveMod.setArrowType(Qt.LeftArrow)

        self.verticalLayout_10.addWidget(self.BTNRemoveMod)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.ListSelectMod = QListWidget(self.scrollAreaWidgetContents_2)
        self.ListSelectMod.setObjectName(u"ListSelectMod")
        self.ListSelectMod.setMinimumSize(QSize(0, 150))

        self.verticalLayout_11.addWidget(self.ListSelectMod)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.BTNAnalysisMod = QPushButton(self.scrollAreaWidgetContents_2)
        self.BTNAnalysisMod.setObjectName(u"BTNAnalysisMod")
        self.BTNAnalysisMod.setMinimumSize(QSize(0, 50))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/icons8_1st_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTNAnalysisMod.setIcon(icon6)
        self.BTNAnalysisMod.setIconSize(QSize(32, 32))

        self.verticalLayout_12.addWidget(self.BTNAnalysisMod)

        self.BTNModDownload = QPushButton(self.scrollAreaWidgetContents_2)
        self.BTNModDownload.setObjectName(u"BTNModDownload")
        self.BTNModDownload.setMinimumSize(QSize(0, 50))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/icons8_circled_2_c_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTNModDownload.setIcon(icon7)
        self.BTNModDownload.setIconSize(QSize(32, 32))

        self.verticalLayout_12.addWidget(self.BTNModDownload)

        self.BTNModStandardCopy = QPushButton(self.scrollAreaWidgetContents_2)
        self.BTNModStandardCopy.setObjectName(u"BTNModStandardCopy")
        self.BTNModStandardCopy.setMinimumSize(QSize(0, 50))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/icons8_circled_3_c_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTNModStandardCopy.setIcon(icon8)
        self.BTNModStandardCopy.setIconSize(QSize(32, 32))

        self.verticalLayout_12.addWidget(self.BTNModStandardCopy)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 829, 21))
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
        self.actionShowArgs.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u5f53\u524d\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.btnGetPy.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u6253\u5f00\u4e00\u4e2apy\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnGetPy.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u6253\u5f00\u4e00\u4e2apy\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btnGetPy.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u6253\u5f00\u4e00\u4e2apy\u6587\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
        self.btnGetPy.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00Python\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.LinePyFilePath.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u663e\u793a\u6253\u5305py\u5165\u53e3\u6587\u4ef6\u7684\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.LinePyFilePath.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u663e\u793a\u6253\u5305py\u5165\u53e3\u6587\u4ef6\u7684\u8def\u5f84", None))
#endif // QT_CONFIG(whatsthis)
        self.LinePyFilePath.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6ca1\u6709\u9009\u62e9\u4efb\u4f55py\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u60a8\u7684\u6253\u5305\u7b56\u7565", None))
#if QT_CONFIG(tooltip)
        self.standalone.setToolTip(QCoreApplication.translate("MainWindow", u"standalone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.standalone.setStatusTip(QCoreApplication.translate("MainWindow", u"\u591a\u6587\u4ef6\u6253\u5305\uff0c\u7a33\u5b9a\u6027\u5c1a\u53ef\uff08\u63a8\u8350\uff09", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.standalone.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u751f\u6210\u4e00\u4e2a\u6587\u4ef6\u5939\uff0c\u53ef\u8fd0\u884c\u6587\u4ef6\u5728\u8fd9\u4e2a\u6587\u4ef6\u5939\u91cc\u9762</p><p>\u540c\u65f6\u8fd9\u4e2a\u6587\u4ef6\u5939\u91cc\u9762\u8fd8\u6709\u5f88\u591a\u5176\u4ed6\u7684\u5185\u5bb9</p><p>\u4f7f\u7528\u8fd9\u79cd\u65b9\u6cd5\u76f8\u5bf9\u4e8e\u5355\u6587\u4ef6\u4e0d\u5bb9\u6613\u62a5\u9519\uff0c\u4f46\u662f\u65b0\u624b\u53ef\u80fd\u627e\u4e0d\u5230\u53ef\u6267\u884c\u6587\u4ef6</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.standalone.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u4e3a\u591a\u6587\u4ef6\n"
"--standalone", None))
#if QT_CONFIG(tooltip)
        self.onefile.setToolTip(QCoreApplication.translate("MainWindow", u"onefile", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.onefile.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u6210\u4e00\u4e2a\u5355\u4e2aexe(\u4e0d\u63a8\u8350)\uff0c\u63a8\u8350\u540e\u671f\u4f7f\u7528EVB\u81ea\u5df1\u6253\u5305\uff0c\u4e0d\u8981\u7528nuitka\u7684", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.onefile.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6253\u5305\u51fa\u6765\u7684\u6587\u4ef6\u662f\u5355\u4e2aexe\u6587\u4ef6\uff0c\u65b9\u4fbf\u4f20\u64ad\uff0c\u4f46\u662f\u4e0d\u65b9\u4fbf\u8c03\u8bd5</p><p>\u901a\u5e38\u90fd\u662f\u591a\u6587\u4ef6\u8fd0\u884c\u6210\u529f\u4ee5\u540e\u624d\u4f1a\u4f7f\u7528\u8fd9\u4e2a</p><p>\u8be5\u547d\u4ee4\u4f1a\u540c\u65f6\u5f00\u542f--windows-onefile-tempdir-spec=./temp</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.onefile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u4e3a\u5355\u6587\u4ef6\n"
"--onefile", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.toolButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.btnStart.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u4e2a\u6309\u94ae\u5c31\u4f1a\u5f00\u59cb\u6253\u5305\uff0c\u901a\u5e38\u9700\u8981\u7b49\u5f85\u4e00\u6bb5\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnStart.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u4e2a\u6309\u94ae\u5c31\u4f1a\u5f00\u59cb\u6253\u5305\uff0c\u901a\u5e38\u9700\u8981\u7b49\u5f85\u4e00\u6bb5\u65f6\u95f4", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btnStart.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u4e2a\u6309\u94ae\u5c31\u4f1a\u5f00\u59cb\u6253\u5305\uff0c\u901a\u5e38\u9700\u8981\u7b49\u5f85\u4e00\u6bb5\u65f6\u95f4", None))
#endif // QT_CONFIG(whatsthis)
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6253\u5305", None))
#if QT_CONFIG(tooltip)
        self.CBShowProgress.setToolTip(QCoreApplication.translate("MainWindow", u"show-progress", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CBShowProgress.setWhatsThis(QCoreApplication.translate("MainWindow", u"show-progress", None))
#endif // QT_CONFIG(whatsthis)
        self.CBShowProgress.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8fdb\u5ea6\u6761\n"
"--show-progress", None))
#if QT_CONFIG(tooltip)
        self.BTNSetOutputPath.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNSetOutputPath.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNSetOutputPath.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNSetOutputPath.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.CBShowMemory.setToolTip(QCoreApplication.translate("MainWindow", u"show-memory", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CBShowMemory.setWhatsThis(QCoreApplication.translate("MainWindow", u"show-memory", None))
#endif // QT_CONFIG(whatsthis)
        self.CBShowMemory.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5185\u5b58\u5360\u7528\n"
"-show-memory", None))
#if QT_CONFIG(tooltip)
        self.LEIcon.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEIcon.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEIcon.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(whatsthis)
        self.LEIcon.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u653e\u7f6e\u56fe\u6807\uff0c\u53ef\u4ee5\u76f4\u63a5\u62d6\u5165", None))
#if QT_CONFIG(tooltip)
        self.BTNSetIcon.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNSetIcon.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNSetIcon.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNSetIcon.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u56fe\u6807", None))
#if QT_CONFIG(tooltip)
        self.LEOutpuPath.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEOutpuPath.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEOutpuPath.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.LEOutpuPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u53ef\u4ee5\u4f7f\u7528\u62d6\u62fd\u7684\u65b9\u5f0f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u53c2\u6570", None))
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

#if QT_CONFIG(tooltip)
        self.listUnselect.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u6ca1\u6709\u88ab\u542f\u7528\u7684\u63d2\u4ef6\uff0c\u4f60\u4e5f\u53ef\u4ee5\u4e0a\u5b98\u7f51\u81ea\u5df1\u770b\u6709\u54ea\u4e9b\u5176\u4ed6\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.listUnselect.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u6ca1\u6709\u88ab\u542f\u7528\u7684\u63d2\u4ef6\uff0c\u4f60\u4e5f\u53ef\u4ee5\u4e0a\u5b98\u7f51\u81ea\u5df1\u770b\u6709\u54ea\u4e9b\u5176\u4ed6\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.listUnselect.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u6ca1\u6709\u88ab\u542f\u7528\u7684\u63d2\u4ef6\uff0c\u4f60\u4e5f\u53ef\u4ee5\u4e0a\u5b98\u7f51\u81ea\u5df1\u770b\u6709\u54ea\u4e9b\u5176\u4ed6\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.BTNAddPlugin.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u79fb\u52a8\u63d2\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNAddPlugin.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u79fb\u52a8\u63d2\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNAddPlugin.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u79fb\u52a8\u63d2\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNAddPlugin.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.BTNRemovePlugin.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u79fb\u52a8\u63d2\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNRemovePlugin.setStatusTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u79fb\u52a8\u63d2\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNRemovePlugin.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u79fb\u52a8\u63d2\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNRemovePlugin.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u7ecf\u542f\u7528\u7684\u63d2\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.listSelect.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u5df2\u7ecf\u542f\u7528\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.listSelect.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u5df2\u7ecf\u542f\u7528\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.listSelect.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u5df2\u7ecf\u542f\u7528\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.plainTextEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.plainTextEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.plainTextEdit.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u662f\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(whatsthis)
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u4f60\u5bfc\u5165\u4e86\u76f8\u5e94\u7684\u6a21\u5757\uff0c\u90a3\u4e48\u4f60\u9700\u8981\u4ece\u5de6\u8fb9\u9009\u62e9\u5bf9\u5e94\u7684\u63d2\u4ef6\uff0c\u7136\u540e\u53cc\u51fb\u4ed6\u6216\u8005\u70b9\u51fb\u6309\u94ae\u5c06\u5b83\u6dfb\u52a0\u5230\u53f3\u8fb9\n"
"\n"
"\u8fd9\u6837\u505a\u80fd\u591f\u8ba9\u4f60\u66f4\u5feb\u7684\u7f16\u8bd1\uff0c\u800c\u4e14\u6709\u7684\u65f6\u5019\u5982\u679c\u4f60\u6ca1\u6709\u5f00\u542f\u63d2\u4ef6\u6700\u540e\u751a\u81f3\u53ef\u80fd\u65e0\u6cd5\u8fd0\u884c\uff0c\u6bd4\u5982PyQt\n"
"\n"
"--anti-bloat \u547d\u4ee4\u9009\u9879\u7528\u4e8e\u51cf\u5c0f\u6253\u5305\u540e\u7684\u53ef\u6267\u884c\u6587\u4ef6\u7684\u5927\u5c0f\u3002Nuitka \u4f1a\u5c1d\u8bd5\u79fb\u9664\u4e00\u4e9b\u4e0d\u5fc5\u8981\u7684\u4ee3\u7801\u548c\u6570\u636e,\u6709\u62a5\u9519\u53ef\u80fd\n"
"\n"
"--upx \u53ef\u4ee5\u5728\u51cf\u5c0f\u5305\u7684\u5927\u5c0f\u7684\u540c\u65f6\u4e0d\u62a5\u9519\uff0c\u4f46\u662f\u4f1a\u589e\u52a0\u6253\u5305\u65f6\u95f4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u63d2\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6027\u80fd", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0d\u8981\u8bbe\u7f6e\u5927\u4e8e\u81ea\u5df1\u7535\u8111\u6838\u5fc3\u7684\u7ebf\u7a0b\uff0c\u901a\u5e38\u8bbe\u7f6e\u4e3a6\u6216\u80058\u5373\u53ef", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5f00\u542f\u7684\u7ebf\u7a0b\u6570<br/>jobs</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CBLowMemory.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBLowMemory.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBLowMemory.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(whatsthis)
        self.CBLowMemory.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8bd1\u65f6\u5360\u7528\u66f4\u5c11\u7684\u5185\u5b58\n"
"low-memory", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u9009\u9879", None))
#if QT_CONFIG(tooltip)
        self.CBDisableCcache.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBDisableCcache.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5f53\u4f60\u9891\u7e41\u6253\u5305\u5931\u8d25\u7684\u65f6\u5019\u53ef\u4ee5\u5f00\u8d77\u6765\uff0c\u5e73\u65f6\u5c3d\u91cf\u5173\u95ed\uff0c\u5173\u95ed\u8fd9\u4e2a\u9009\u9879\u80fd\u52a0\u5feb\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBDisableCcache.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u5f53\u4f60\u9891\u7e41\u6253\u5305\u5931\u8d25\u7684\u65f6\u5019\u53ef\u4ee5\u5f00\u8d77\u6765\uff0c\u5e73\u65f6\u5c3d\u91cf\u5173\u95ed\uff0c\u5173\u95ed\u8fd9\u4e2a\u9009\u9879\u80fd\u52a0\u5feb\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(whatsthis)
        self.CBDisableCcache.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4f7f\u7528\u4e0a\u4e00\u6b21\u7684\u7f13\u5b58\uff0c\u9632\u6b62\u6253\u5305\u5931\u8d25\n"
"disable-ccache", None))
#if QT_CONFIG(tooltip)
        self.CBQuiet.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBQuiet.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e2a\u9009\u9879\u53ea\u4f1a\u8f93\u51fa\u9519\u8bef", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBQuiet.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e2a\u9009\u9879\u53ea\u4f1a\u8f93\u51fa\u9519\u8bef", None))
#endif // QT_CONFIG(whatsthis)
        self.CBQuiet.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u5b89\u9759\u6253\u5305\u6a21\u5f0f(\u53ea\u8f93\u51fa\u9519\u8bef)\n"
"--quiet", None))
#if QT_CONFIG(tooltip)
        self.CBFollowImports.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBFollowImports.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u4f60\u5bfc\u5165\u4e86\u5f88\u591a\u7b2c\u4e09\u65b9\u5e93\uff0c\u8bf7\u52a1\u5fc5\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBFollowImports.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u4f60\u5bfc\u5165\u4e86\u5f88\u591a\u7b2c\u4e09\u65b9\u5e93\uff0c\u8bf7\u52a1\u5fc5\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(whatsthis)
        self.CBFollowImports.setText(QCoreApplication.translate("MainWindow", u"\u9012\u5f52\u67e5\u627e\u6240\u6709\u7684\u6a21\u5757\n"
"--follow-imports", None))
#if QT_CONFIG(tooltip)
        self.CBCleanCache.setToolTip(QCoreApplication.translate("MainWindow", u"remove-output", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBCleanCache.setStatusTip(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBCleanCache.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.CBCleanCache.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6240\u6709\u7f13\u5b58\n"
"--clean-cache", None))
#if QT_CONFIG(tooltip)
        self.CBDisableConsole.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBDisableConsole.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0d\u8981\u5728\u4e00\u5f00\u59cb\u76f4\u63a5\u4f7f\u7528\uff0c\u8bf7\u786e\u4fdd\u81ea\u5df1\u7684\u7a0b\u5e8f\u6253\u5305\u4e4b\u540e\u80fd\u591f\u8fd0\u884c\u518d\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBDisableConsole.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0d\u8981\u5728\u4e00\u5f00\u59cb\u76f4\u63a5\u4f7f\u7528\uff0c\u8bf7\u786e\u4fdd\u81ea\u5df1\u7684\u7a0b\u5e8f\u6253\u5305\u4e4b\u540e\u80fd\u591f\u8fd0\u884c\u518d\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(whatsthis)
        self.CBDisableConsole.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u547d\u4ee4\u884c\n"
"--windows-disable-console", None))
#if QT_CONFIG(tooltip)
        self.CBRemoveOutput.setToolTip(QCoreApplication.translate("MainWindow", u"remove-output", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBRemoveOutput.setStatusTip(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBRemoveOutput.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.CBRemoveOutput.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939\n"
"remove-output", None))
#if QT_CONFIG(tooltip)
        self.CBMingw64.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u7528\u6765\u5f00\u542fmingw64\u8fdb\u884c\u52a0\u901f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBMingw64.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u7528\u6765\u5f00\u542fmingw64\u8fdb\u884c\u52a0\u901f", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBMingw64.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8be5\u9009\u9879\u7528\u6765\u5f00\u542fmingw64\u8fdb\u884c\u52a0\u901f", None))
#endif // QT_CONFIG(whatsthis)
        self.CBMingw64.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542fmingw64\n"
"--mingw64 ", None))
#if QT_CONFIG(tooltip)
        self.CBLto.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5173\u95edLTO\u80fd\u907f\u514d\u6765\u81ea\u7f16\u8bd1\u5668\u7684\u9519\u8bef\uff0cLTO\u5728nuitka\u662f\u9ed8\u8ba4\u5f00\u542f\u7684</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBLto.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5173\u95edLTO\u80fd\u907f\u514d\u6765\u81ea\u7f16\u8bd1\u5668\u7684\u9519\u8bef\uff0cLTO\u5728nuitka\u662f\u9ed8\u8ba4\u5f00\u542f\u7684", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBLto.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u5173\u95edLTO\u80fd\u907f\u514d\u6765\u81ea\u7f16\u8bd1\u5668\u7684\u9519\u8bef\uff0cLTO\u5728nuitka\u662f\u9ed8\u8ba4\u5f00\u542f\u7684", None))
#endif // QT_CONFIG(whatsthis)
        self.CBLto.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95edlto\n"
"--lto=no", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51faexe\u7684\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.LEFileVersion.setToolTip(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEFileVersion.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEFileVersion.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.LBProductVersion.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBProductVersion.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBProductVersion.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
        self.LBProductVersion.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7248\u672c\n"
"--windows-product-version", None))
#if QT_CONFIG(tooltip)
        self.LECompanyName.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LECompanyName.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LECompanyName.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.LBFileVersion.setToolTip(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBFileVersion.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBFileVersion.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
        self.LBFileVersion.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7248\u672c\n"
"--windows-file-version", None))
#if QT_CONFIG(tooltip)
        self.LEProductVersion.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEProductVersion.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEProductVersion.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.LBCompanyName.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBCompanyName.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBCompanyName.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(whatsthis)
        self.LBCompanyName.setText(QCoreApplication.translate("MainWindow", u"\u516c\u53f8\u540d\u79f0\n"
"--windows-company-name", None))
#if QT_CONFIG(tooltip)
        self.LBFileDescription.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBFileDescription.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBFileDescription.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(whatsthis)
        self.LBFileDescription.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u63cf\u8ff0\n"
"--windows-file-description", None))
#if QT_CONFIG(tooltip)
        self.LEFileDescription.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEFileDescription.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEFileDescription.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.PTEArgsOutput.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u663e\u793a\u8f93\u51fa\u5728\u547d\u4ee4\u884c\u7ed9nuitka\u7684\u53c2\u6570\uff0c\u901a\u5e38\u4f60\u4e5f\u53ef\u4ee5\u624b\u52a8\u590d\u5236\u5230\u547d\u4ee4\u884c\u6267\u884c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.PTEArgsOutput.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u663e\u793a\u8f93\u51fa\u5728\u547d\u4ee4\u884c\u7ed9nuitka\u7684\u53c2\u6570\uff0c\u901a\u5e38\u4f60\u4e5f\u53ef\u4ee5\u624b\u52a8\u590d\u5236\u5230\u547d\u4ee4\u884c\u6267\u884c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.PTEArgsOutput.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u663e\u793a\u8f93\u51fa\u5728\u547d\u4ee4\u884c\u7ed9nuitka\u7684\u53c2\u6570\uff0c\u901a\u5e38\u4f60\u4e5f\u53ef\u4ee5\u624b\u52a8\u590d\u5236\u5230\u547d\u4ee4\u884c\u6267\u884c", None))
#endif // QT_CONFIG(whatsthis)
        self.PTEArgsOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u663e\u793a\u5f53\u524d\u4f60\u9009\u62e9\u7684\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.PTEExplaineCompatibility.setToolTip(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u770b\u4e0d\u5b8c\u5168\u53ef\u4ee5\u6eda\u52a8\u6eda\u52a8\u6761", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.PTEExplaineCompatibility.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.PTEExplaineCompatibility.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u770b\u4e0d\u5b8c\u5168\u53ef\u4ee5\u6eda\u52a8\u6eda\u52a8\u6761", None))
#endif // QT_CONFIG(whatsthis)
        self.PTEExplaineCompatibility.setPlainText(QCoreApplication.translate("MainWindow", u"==(\u8be5\u9875\u9762\u662f\u5b9e\u9a8c\u6027\u7684\uff01\u5176\u4e2d\u754c\u9762\u7684\u5185\u5bb9\u751a\u81f3\u903b\u8f91\u90fd\u53ef\u80fd\u4f1a\u53d1\u751f\u53d8\u5316\uff0c\u4f7f\u7528\u524d\u8bf7\u8be6\u7ec6\u9605\u8bfb\u4e0b\u65b9\u8bf4\u660e)==\n"
"\n"
"\u542f\u52a8\u5176\u4e2d\u7684\u9009\u9879\u4e4b\u540e\u6240\u6709\u7684\u5305\u90fd\u4e0d\u4f1a\u88ab\u7f16\u8bd1\u800c\u662f\u4f1a\u88ab\u76f4\u63a5\u590d\u5236\u5230\u6253\u5305\u76ee\u5f55\u4e0b\uff0c\u4f7f\u7528\u8be5\u65b9\u6cd5\u53ef\u4ee5\u89e3\u51b3\u4e00\u4e9b\u5e93\u65e0\u6cd5\u7f16\u8bd1\u6216\u8005\u7f16\u8bd1\u9519\u8bef\u7684\u60c5\u51b5\uff0c\u5927\u90e8\u5206\u62a5\u9519\u51fa\u9519\u90fd\u53ef\u4ee5\u4ece\u8fd9\u91cc\u5220\u53bb\u6253\u5305\u5e93\u800c\u4f7f\u7528\u76f4\u63a5\u8c03\u7528\u7684\u65b9\u5f0f\u8fd0\u884c\uff0c\u80fd\u5927\u5e45\u589e\u52a0\u8fd0\u884c\u901a\u8fc7\u7684\u6982\u7387\n"
"\n"
"\u4f46\u662f\u9700\u8981\u6ce8\u610f\uff0c\u6b64\u65b9\u6cd5\u4f1a\u5bfc\u81f4\u6253\u5305\u4f53\u79ef\u5927\u5e45\u589e\u52a0\uff0c\u800c"
                        "\u4e14\u4f1a\u5728\u6253\u5305\u76ee\u5f55\u4e0b\u751f\u6210\u5927\u91cf\u6587\u4ef6\uff0c\u5728\u975e\u5fc5\u8981\u60c5\u51b5\u4e0b\u4e0d\u542f\u7528\n"
"\n"
"\u9009\u62e9\u597d\u9700\u8981\u6253\u5305\u7684Py\u6587\u4ef6\u540e\u70b9\u51fb\u4e0b\u65b9\u7684\u2460\u65b9\u6cd5\u5206\u6790\u7b2c\u4e09\u65b9\u5e93\uff0c\u7136\u540e\u70b9\u51fb\u2461\u65b9\u6cd5\u5c06\u6240\u6709\u5e93\u4e0b\u8f7d\u5230\u6253\u5305\u76ee\u5f55\u4e2d\n"
"\n"
"\u4f60\u65e0\u6cd5\u624b\u52a8\u7f16\u8f91\u4e0b\u65b9\u5185\u5bb9\uff0c\u6240\u6709\u7684\u5e93\u90fd\u4f1a\u7531pipreqs(\u4f1a\u81ea\u52a8\u5b89\u88c5)\u8fdb\u884c\u7b5b\u9009\n"
"", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u7684\u65f6\u5019\u8fd9\u4e9b\u5e93\u4f1a\u88ab\u7f16\u8bd1", None))
#if QT_CONFIG(tooltip)
        self.ListUnselectMod.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u5e93\u662f\u88ab\u8bc6\u522b\u51fa\u6765\u7684\u5e93\uff0c\u53cc\u52a0\u4ed6\u4eec\u6216\u8005\u70b9\u51fb\u4e2d\u95f4\u7684\u6309\u94ae\u6765\u79fb\u52a8", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.ListUnselectMod.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u5e93\u662f\u88ab\u8bc6\u522b\u51fa\u6765\u7684\u5e93\uff0c\u53cc\u52a0\u4ed6\u4eec\u6216\u8005\u70b9\u51fb\u4e2d\u95f4\u7684\u6309\u94ae\u6765\u79fb\u52a8", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.ListUnselectMod.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u5e93\u662f\u88ab\u8bc6\u522b\u51fa\u6765\u7684\u5e93\uff0c\u53cc\u52a0\u4ed6\u4eec\u6216\u8005\u70b9\u51fb\u4e2d\u95f4\u7684\u6309\u94ae\u6765\u79fb\u52a8", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.BTNAddMod.setToolTip(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u5e93", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.BTNAddMod.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u5e93", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNAddMod.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.BTNRemoveMod.setToolTip(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u5e93", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.BTNRemoveMod.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u5e93", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNRemoveMod.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4e00\u4e9b\u8bf4\u660e", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u5e93\u4f1a\u88ab\u76f4\u63a5\u590d\u5236\u8fdb\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.ListSelectMod.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u662f\u4f1a\u8ddf\u968f\u6253\u5305\u4e00\u8d77\u88ab\u653e\u8fdb\u6253\u5305\u76ee\u5f55\u7684\u5e93", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.ListSelectMod.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u662f\u4f1a\u8ddf\u968f\u6253\u5305\u4e00\u8d77\u88ab\u653e\u8fdb\u6253\u5305\u76ee\u5f55\u7684\u5e93", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.ListSelectMod.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e9b\u662f\u4f1a\u8ddf\u968f\u6253\u5305\u4e00\u8d77\u88ab\u653e\u8fdb\u6253\u5305\u76ee\u5f55\u7684\u5e93", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.BTNAnalysisMod.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e00\u6b65\u4f1a\u8c03\u7528pipreqs\uff0c\u6240\u4ee5\u53ef\u80fd\u4f1a\u51fa\u73b0\u547d\u4ee4\u884c\uff0c\u800c\u4e14\u4f1a\u7b49\u5f85\u5f88\u957f\u65f6\u95f4\uff0c\u5c5e\u4e8e\u6b63\u5e38\u60c5\u51b5", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNAnalysisMod.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e00\u6b65\u4f1a\u8c03\u7528pipreqs\uff0c\u6240\u4ee5\u53ef\u80fd\u4f1a\u51fa\u73b0\u547d\u4ee4\u884c\uff0c\u800c\u4e14\u4f1a\u7b49\u5f85\u5f88\u957f\u65f6\u95f4\uff0c\u5c5e\u4e8e\u6b63\u5e38\u60c5\u51b5", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNAnalysisMod.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u8fd9\u4e00\u6b65\u4f1a\u8c03\u7528pipreqs\uff0c\u6240\u4ee5\u53ef\u80fd\u4f1a\u51fa\u73b0\u547d\u4ee4\u884c\uff0c\u800c\u4e14\u4f1a\u7b49\u5f85\u5f88\u957f\u65f6\u95f4\uff0c\u5c5e\u4e8e\u6b63\u5e38\u60c5\u51b5", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNAnalysisMod.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u5f00\u59cb\u81ea\u52a8\u5206\u6790\u4ee3\u7801\u4e2d\u4f7f\u7528\u5230\u7684\u5e93(\u5728\u6253\u5305\u524d\u4f7f\u7528)", None))
#if QT_CONFIG(tooltip)
        self.BTNModDownload.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u4e2a\u65b9\u6cd5\u4f1a\u4f7f\u7528pip\u65b9\u6cd5\u5c06\u7b2c\u4e09\u65b9\u5e93\u4ee5\u53ca\u4e00\u4e9bpython\u539f\u751f\u7684dll\u548c\u6807\u51c6\u5e93\u590d\u5236\u8fdb\u6253\u5305\u76ee\u5f55\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u6253\u5305\u6587\u4ef6\u5939\u5185\u6587\u4ef6\u6570\u91cf\u5f88\u591a\uff0c\u540e\u671f\u53ef\u4ee5\u7528EVB\u5c01\u5305", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNModDownload.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff0c\u8be5\u65b9\u6cd5\u9700\u8981\u5148\u6253\u5305\u540e\u518d\u4f7f\u7528\uff0c\u4e0d\u7136nuitka\u4f1a\u6e05\u7a7a\u76ee\u5f55\u4e0b\u6240\u6709\u7684\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNModDownload.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u70b9\u51fb\u8fd9\u4e2a\u65b9\u6cd5\u4f1a\u4f7f\u7528pip\u65b9\u6cd5\u5c06\u7b2c\u4e09\u65b9\u5e93\u4ee5\u53ca\u4e00\u4e9bpython\u539f\u751f\u7684dll\u548c\u6807\u51c6\u5e93\u590d\u5236\u8fdb\u6253\u5305\u76ee\u5f55\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u6253\u5305\u6587\u4ef6\u5939\u5185\u6587\u4ef6\u6570\u91cf\u5f88\u591a\uff0c\u540e\u671f\u53ef\u4ee5\u7528EVB\u5c01\u5305</p><p><br/></p><p>\u6ce8\u610f\uff0c\u8be5\u65b9\u6cd5\u9700\u8981\u5148\u6253\u5305\u540e\u518d\u4f7f\u7528\uff0c\u4e0d\u7136nuitka\u4f1a\u6e05\u7a7a\u76ee\u5f55\u4e0b\u6240\u6709\u7684\u6587\u4ef6</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNModDownload.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u8fd9\u4e9b\u5e93\u4e0b\u8f7d\u5230\u6253\u5305\u76ee\u5f55\u4e2d(\u9700\u5728\u6253\u5305\u5b8c\u6210\u540e\u4f7f\u7528)", None))
#if QT_CONFIG(tooltip)
        self.BTNModStandardCopy.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5927\u91cf\u7b2c\u4e09\u65b9\u5e93\u90fd\u4f9d\u8d56\u6807\u51c6\u5e93\uff0c\u9700\u8981\u624b\u52a8\u5c06\u8fd9\u4e9b\u6807\u51c6\u5e93\u590d\u5236\u5230\u6253\u5305\u76ee\u5f55\u4e2d\u624d\u80fd\u6b63\u5e38\u4f7f\u7528</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNModStandardCopy.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5927\u91cf\u7b2c\u4e09\u65b9\u5e93\u90fd\u4f9d\u8d56\u6807\u51c6\u5e93\uff0c\u9700\u8981\u624b\u52a8\u5c06\u8fd9\u4e9b\u6807\u51c6\u5e93\u590d\u5236\u5230\u6253\u5305\u76ee\u5f55\u4e2d\u624d\u80fd\u6b63\u5e38\u4f7f\u7528", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNModStandardCopy.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u5927\u91cf\u7b2c\u4e09\u65b9\u5e93\u90fd\u4f9d\u8d56\u6807\u51c6\u5e93\uff0c\u9700\u8981\u624b\u52a8\u5c06\u8fd9\u4e9b\u6807\u51c6\u5e93\u590d\u5236\u5230\u6253\u5305\u76ee\u5f55\u4e2d\u624d\u80fd\u6b63\u5e38\u4f7f\u7528", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNModStandardCopy.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u6807\u51c6\u5e93\u590d\u5236\u5230\u6253\u5305\u76ee\u5f55\u4e2d(\u9700\u5728\u6253\u5305\u5b8c\u6210\u540e\u4f7f\u7528)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u517c\u5bb9\u6027(\u5b9e\u9a8c\u6027\u529f\u80fd)", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u76ae\u80a4", None))
    # retranslateUi

