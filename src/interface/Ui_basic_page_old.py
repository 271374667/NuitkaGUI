# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_page_old.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from qmaterialwidgets import (CaptionLabel, ElevatedPushButton, FilledPushButton, LineEdit,
    RadioButton, TonalPushButton, TransparentToolButton)
from src.resource import rc_res

class Ui_home_page(object):
    def setupUi(self, home_page):
        if not home_page.objectName():
            home_page.setObjectName(u"home_page")
        home_page.resize(850, 550)
        self.btnGetPy = ElevatedPushButton(home_page)
        self.btnGetPy.setObjectName(u"btnGetPy")
        self.btnGetPy.setGeometry(QRect(20, 60, 201, 36))
        self.btnGetPy.setBorderRadius(10)
        self.groupBox = QGroupBox(home_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 30, 511, 81))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.standalone = RadioButton(self.groupBox)
        self.standalone.setObjectName(u"standalone")
        self.standalone.setMinimumSize(QSize(0, 30))
        self.standalone.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.standalone.setFont(font)
        self.standalone.setIconSize(QSize(16, 16))
        self.standalone.setChecked(True)

        self.horizontalLayout.addWidget(self.standalone)

        self.onefile = RadioButton(self.groupBox)
        self.onefile.setObjectName(u"onefile")
        self.onefile.setMinimumSize(QSize(0, 30))
        self.onefile.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.onefile)

        self.toolButton = TransparentToolButton(home_page)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(770, 50, 36, 36))
        icon = QIcon()
        icon.addFile(u":/Icons/materialIcons/help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setCheckable(False)
        self.LinePyFilePath = CaptionLabel(home_page)
        self.LinePyFilePath.setObjectName(u"LinePyFilePath")
        self.LinePyFilePath.setGeometry(QRect(20, 110, 401, 31))
        self.widget = QWidget(home_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 160, 831, 381))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(122, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.RBJRNone = RadioButton(self.groupBox_2)
        self.RBJRNone.setObjectName(u"RBJRNone")

        self.verticalLayout.addWidget(self.RBJRNone)

        self.RBJRHigh = RadioButton(self.groupBox_2)
        self.RBJRHigh.setObjectName(u"RBJRHigh")

        self.verticalLayout.addWidget(self.RBJRHigh)

        self.RBJRTop = RadioButton(self.groupBox_2)
        self.RBJRTop.setObjectName(u"RBJRTop")

        self.verticalLayout.addWidget(self.RBJRTop)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.LEPythonExePath = LineEdit(self.widget)
        self.LEPythonExePath.setObjectName(u"LEPythonExePath")

        self.gridLayout.addWidget(self.LEPythonExePath, 1, 0, 1, 2)

        self.BTNSetIcon = TonalPushButton(self.widget)
        self.BTNSetIcon.setObjectName(u"BTNSetIcon")

        self.gridLayout.addWidget(self.BTNSetIcon, 2, 0, 1, 1)

        self.BTNSetOutputPath = TonalPushButton(self.widget)
        self.BTNSetOutputPath.setObjectName(u"BTNSetOutputPath")

        self.gridLayout.addWidget(self.BTNSetOutputPath, 4, 0, 1, 1)

        self.LEOutpuPath = LineEdit(self.widget)
        self.LEOutpuPath.setObjectName(u"LEOutpuPath")

        self.gridLayout.addWidget(self.LEOutpuPath, 5, 0, 1, 2)

        self.BTNPythonExePath = TonalPushButton(self.widget)
        self.BTNPythonExePath.setObjectName(u"BTNPythonExePath")

        self.gridLayout.addWidget(self.BTNPythonExePath, 0, 0, 1, 1)

        self.LEIcon = LineEdit(self.widget)
        self.LEIcon.setObjectName(u"LEIcon")

        self.gridLayout.addWidget(self.LEIcon, 3, 0, 1, 2)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btnStart = FilledPushButton(self.widget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setBorderRadius(10)

        self.verticalLayout_2.addWidget(self.btnStart)


        self.retranslateUi(home_page)

        QMetaObject.connectSlotsByName(home_page)
    # setupUi

    def retranslateUi(self, home_page):
        home_page.setWindowTitle(QCoreApplication.translate("home_page", u"home_page", None))
#if QT_CONFIG(tooltip)
        self.btnGetPy.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u6253\u5f00\u4e00\u4e2apy\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnGetPy.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u6253\u5f00\u4e00\u4e2apy\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btnGetPy.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u6253\u5f00\u4e00\u4e2apy\u6587\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
        self.btnGetPy.setText(QCoreApplication.translate("home_page", u"\u9009\u62e9\u6253\u5305\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("home_page", u"\u9009\u62e9\u60a8\u7684\u6253\u5305\u7b56\u7565", None))
#if QT_CONFIG(tooltip)
        self.standalone.setToolTip(QCoreApplication.translate("home_page", u"standalone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.standalone.setStatusTip(QCoreApplication.translate("home_page", u"\u591a\u6587\u4ef6\u6253\u5305\uff0c\u7a33\u5b9a\u6027\u5c1a\u53ef\uff08\u63a8\u8350\uff09", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.standalone.setWhatsThis(QCoreApplication.translate("home_page", u"<html><head/><body><p>\u751f\u6210\u4e00\u4e2a\u6587\u4ef6\u5939\uff0c\u53ef\u8fd0\u884c\u6587\u4ef6\u5728\u8fd9\u4e2a\u6587\u4ef6\u5939\u91cc\u9762</p><p>\u540c\u65f6\u8fd9\u4e2a\u6587\u4ef6\u5939\u91cc\u9762\u8fd8\u6709\u5f88\u591a\u5176\u4ed6\u7684\u5185\u5bb9</p><p>\u4f7f\u7528\u8fd9\u79cd\u65b9\u6cd5\u76f8\u5bf9\u4e8e\u5355\u6587\u4ef6\u4e0d\u5bb9\u6613\u62a5\u9519\uff0c\u4f46\u662f\u65b0\u624b\u53ef\u80fd\u627e\u4e0d\u5230\u53ef\u6267\u884c\u6587\u4ef6</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.standalone.setText(QCoreApplication.translate("home_page", u"\u6253\u5305\u4e3a\u591a\u6587\u4ef6\n"
"--standalone", None))
#if QT_CONFIG(tooltip)
        self.onefile.setToolTip(QCoreApplication.translate("home_page", u"onefile", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.onefile.setStatusTip(QCoreApplication.translate("home_page", u"\u6253\u5305\u6210\u4e00\u4e2a\u5355\u4e2aexe(\u4e0d\u63a8\u8350)\uff0c\u63a8\u8350\u540e\u671f\u4f7f\u7528EVB\u81ea\u5df1\u6253\u5305\uff0c\u4e0d\u8981\u7528nuitka\u7684", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.onefile.setWhatsThis(QCoreApplication.translate("home_page", u"<html><head/><body><p>\u6253\u5305\u51fa\u6765\u7684\u6587\u4ef6\u662f\u5355\u4e2aexe\u6587\u4ef6\uff0c\u65b9\u4fbf\u4f20\u64ad\uff0c\u4f46\u662f\u4e0d\u65b9\u4fbf\u8c03\u8bd5</p><p>\u901a\u5e38\u90fd\u662f\u591a\u6587\u4ef6\u8fd0\u884c\u6210\u529f\u4ee5\u540e\u624d\u4f1a\u4f7f\u7528\u8fd9\u4e2a</p><p>\u8be5\u547d\u4ee4\u4f1a\u540c\u65f6\u5f00\u542f--windows-onefile-tempdir-spec=./temp</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.onefile.setText(QCoreApplication.translate("home_page", u"\u6253\u5305\u4e3a\u5355\u6587\u4ef6\n"
"--onefile", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.toolButton.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u6211\u8fdb\u5165\u8fd9\u662f\u4ec0\u4e48WhatThis\u9875\u9762", None))
#endif // QT_CONFIG(whatsthis)
        self.toolButton.setText("")
        self.LinePyFilePath.setText(QCoreApplication.translate("home_page", u"\u5f53\u524d\u6ca1\u6709\u9009\u62e9\u4efb\u4f55py\u6587\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("home_page", u"\u517c\u5bb9\u6027", None))
        self.RBJRNone.setText(QCoreApplication.translate("home_page", u"\u65e0", None))
#if QT_CONFIG(tooltip)
        self.RBJRHigh.setToolTip(QCoreApplication.translate("home_page", u"\u8be5\u529f\u80fd\u6d4b\u8bd5\u4e2d", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.RBJRHigh.setStatusTip(QCoreApplication.translate("home_page", u"\u8be5\u529f\u80fd\u6d4b\u8bd5\u4e2d", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.RBJRHigh.setWhatsThis(QCoreApplication.translate("home_page", u"\u8be5\u529f\u80fd\u6d4b\u8bd5\u4e2d", None))
#endif // QT_CONFIG(whatsthis)
        self.RBJRHigh.setText(QCoreApplication.translate("home_page", u"\u52a0\u5f3a\u517c\u5bb9", None))
#if QT_CONFIG(tooltip)
        self.RBJRTop.setToolTip(QCoreApplication.translate("home_page", u"\u8be5\u529f\u80fd\u6d4b\u8bd5\u4e2d", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.RBJRTop.setStatusTip(QCoreApplication.translate("home_page", u"\u8be5\u529f\u80fd\u6d4b\u8bd5\u4e2d", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.RBJRTop.setWhatsThis(QCoreApplication.translate("home_page", u"\u8be5\u529f\u80fd\u6d4b\u8bd5\u4e2d", None))
#endif // QT_CONFIG(whatsthis)
        self.RBJRTop.setText(QCoreApplication.translate("home_page", u"\u6700\u5927\u517c\u5bb9", None))
#if QT_CONFIG(tooltip)
        self.LEPythonExePath.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6epython.exe\u7684\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEPythonExePath.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6epython.exe\u7684\u8def\u5f84", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEPythonExePath.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6epython.exe\u7684\u8def\u5f84", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.BTNSetIcon.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNSetIcon.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNSetIcon.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u8bbe\u7f6e\u6253\u5305\u4e4b\u540eExe\u7684\u56fe\u6807", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNSetIcon.setText(QCoreApplication.translate("home_page", u"\u8bbe\u7f6e\u56fe\u6807", None))
#if QT_CONFIG(tooltip)
        self.BTNSetOutputPath.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNSetOutputPath.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNSetOutputPath.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNSetOutputPath.setText(QCoreApplication.translate("home_page", u"\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.LEOutpuPath.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEOutpuPath.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEOutpuPath.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNPythonExePath.setText(QCoreApplication.translate("home_page", u"Python.exe\u7684\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.LEIcon.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEIcon.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEIcon.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.btnStart.setToolTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u4e2a\u6309\u94ae\u5c31\u4f1a\u5f00\u59cb\u6253\u5305\uff0c\u901a\u5e38\u9700\u8981\u7b49\u5f85\u4e00\u6bb5\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnStart.setStatusTip(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btnStart.setWhatsThis(QCoreApplication.translate("home_page", u"\u70b9\u51fb\u8fd9\u91cc\u8bbe\u7f6e\u8f93\u51fa\u8def\u5f84\uff0c\u4e0d\u8fc7\u4e00\u822c\u90fd\u4f1a\u9ed8\u8ba4output\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.btnStart.setText(QCoreApplication.translate("home_page", u"\u70b9\u6211\u6253\u5305", None))
    # retranslateUi
