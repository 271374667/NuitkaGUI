# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced_page.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

from qmaterialwidgets import (CheckBox, LineEdit, SpinBox, StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(864, 548)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 20, 831, 521))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 808, 675))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.CBLowMemory = CheckBox(self.groupBox_2)
        self.CBLowMemory.setObjectName(u"CBLowMemory")
        self.CBLowMemory.setMinimumSize(QSize(45, 36))

        self.gridLayout_3.addWidget(self.CBLowMemory, 0, 2, 1, 1)

        self.CBClang = CheckBox(self.groupBox_2)
        self.CBClang.setObjectName(u"CBClang")

        self.gridLayout_3.addWidget(self.CBClang, 2, 0, 1, 1)

        self.CBMingw64 = CheckBox(self.groupBox_2)
        self.CBMingw64.setObjectName(u"CBMingw64")
        self.CBMingw64.setMinimumSize(QSize(45, 36))

        self.gridLayout_3.addWidget(self.CBMingw64, 2, 2, 1, 1)

        self.label_3 = StrongBodyLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.jobs = SpinBox(self.groupBox_2)
        self.jobs.setObjectName(u"jobs")
        self.jobs.setMinimumSize(QSize(156, 43))
        self.jobs.setMaximumSize(QSize(131, 43))

        self.gridLayout_3.addWidget(self.jobs, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 290))
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CBQuiet = CheckBox(self.groupBox_4)
        self.CBQuiet.setObjectName(u"CBQuiet")

        self.gridLayout_5.addWidget(self.CBQuiet, 6, 1, 1, 1)

        self.CBCleanCache = CheckBox(self.groupBox_4)
        self.CBCleanCache.setObjectName(u"CBCleanCache")

        self.gridLayout_5.addWidget(self.CBCleanCache, 7, 1, 1, 1)

        self.CBwindowsUacAdmin = CheckBox(self.groupBox_4)
        self.CBwindowsUacAdmin.setObjectName(u"CBwindowsUacAdmin")

        self.gridLayout_5.addWidget(self.CBwindowsUacAdmin, 8, 0, 1, 1)

        self.CBDisableConsole = CheckBox(self.groupBox_4)
        self.CBDisableConsole.setObjectName(u"CBDisableConsole")

        self.gridLayout_5.addWidget(self.CBDisableConsole, 1, 0, 1, 1)

        self.CBLto = CheckBox(self.groupBox_4)
        self.CBLto.setObjectName(u"CBLto")

        self.gridLayout_5.addWidget(self.CBLto, 1, 1, 1, 1)

        self.CBRemoveOutput = CheckBox(self.groupBox_4)
        self.CBRemoveOutput.setObjectName(u"CBRemoveOutput")

        self.gridLayout_5.addWidget(self.CBRemoveOutput, 0, 0, 1, 1)

        self.CBShowMemory = CheckBox(self.groupBox_4)
        self.CBShowMemory.setObjectName(u"CBShowMemory")

        self.gridLayout_5.addWidget(self.CBShowMemory, 7, 0, 1, 1)

        self.CBDisableCcache = CheckBox(self.groupBox_4)
        self.CBDisableCcache.setObjectName(u"CBDisableCcache")

        self.gridLayout_5.addWidget(self.CBDisableCcache, 6, 0, 1, 1)

        self.CBShowProgress = CheckBox(self.groupBox_4)
        self.CBShowProgress.setObjectName(u"CBShowProgress")

        self.gridLayout_5.addWidget(self.CBShowProgress, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 224))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.LBCompanyName = StrongBodyLabel(self.groupBox_3)
        self.LBCompanyName.setObjectName(u"LBCompanyName")
        self.LBCompanyName.setMinimumSize(QSize(200, 0))

        self.gridLayout_4.addWidget(self.LBCompanyName, 0, 0, 1, 1)

        self.LBFileVersion = StrongBodyLabel(self.groupBox_3)
        self.LBFileVersion.setObjectName(u"LBFileVersion")
        self.LBFileVersion.setMinimumSize(QSize(200, 0))

        self.gridLayout_4.addWidget(self.LBFileVersion, 1, 0, 1, 1)

        self.LECompanyName = LineEdit(self.groupBox_3)
        self.LECompanyName.setObjectName(u"LECompanyName")

        self.gridLayout_4.addWidget(self.LECompanyName, 0, 2, 1, 1)

        self.LBFileDescription = StrongBodyLabel(self.groupBox_3)
        self.LBFileDescription.setObjectName(u"LBFileDescription")
        self.LBFileDescription.setMinimumSize(QSize(200, 0))

        self.gridLayout_4.addWidget(self.LBFileDescription, 3, 0, 1, 1)

        self.LBProductVersion = StrongBodyLabel(self.groupBox_3)
        self.LBProductVersion.setObjectName(u"LBProductVersion")
        self.LBProductVersion.setMinimumSize(QSize(200, 0))

        self.gridLayout_4.addWidget(self.LBProductVersion, 2, 0, 1, 1)

        self.LEFileVersion = LineEdit(self.groupBox_3)
        self.LEFileVersion.setObjectName(u"LEFileVersion")

        self.gridLayout_4.addWidget(self.LEFileVersion, 1, 2, 1, 1)

        self.LEProductVersion = LineEdit(self.groupBox_3)
        self.LEProductVersion.setObjectName(u"LEProductVersion")

        self.gridLayout_4.addWidget(self.LEProductVersion, 2, 2, 1, 1)

        self.LEFileDescription = LineEdit(self.groupBox_3)
        self.LEFileDescription.setObjectName(u"LEFileDescription")

        self.gridLayout_4.addWidget(self.LEFileDescription, 3, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6027\u80fd", None))
#if QT_CONFIG(tooltip)
        self.CBLowMemory.setToolTip(QCoreApplication.translate("Form", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBLowMemory.setStatusTip(QCoreApplication.translate("Form", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBLowMemory.setWhatsThis(QCoreApplication.translate("Form", u"\u8be5\u9009\u9879\u4f1a\u964d\u4f4e\u6253\u5305\u901f\u5ea6", None))
#endif // QT_CONFIG(whatsthis)
        self.CBLowMemory.setText(QCoreApplication.translate("Form", u"\u7f16\u8bd1\u65f6\u5360\u7528\u66f4\u5c11\u7684\u5185\u5b58\n"
"low-memory", None))
#if QT_CONFIG(tooltip)
        self.CBClang.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u901f\u5ea6\u6700\u5feb\uff0c\u6bd4mingw64\u6700\u5feb\u80fd\u5feb5\u500d\u4ee5\u4e0a\uff0c\u4f46\u662f\u6253\u5305\u62a5\u9519\u6982\u7387\u63d0\u9ad8\uff0c\u540c\u65f6\u4f60\u9700\u8981\u81ea\u5df1\u4e0b\u8f7dclang\u7f16\u8bd1\u5668\uff0c\u7b2c\u4e00\u6b21\u53ef\u4ee5\u5c1d\u8bd5\uff0c\u5931\u8d25\u540e\u518d\u7528mingw64</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBClang.setStatusTip(QCoreApplication.translate("Form", u"\u901f\u5ea6\u6700\u5feb\uff0c\u6bd4mingw64\u6700\u5feb\u80fd\u5feb5\u500d\u4ee5\u4e0a\uff0c\u4f46\u662f\u6253\u5305\u62a5\u9519\u6982\u7387\u63d0\u9ad8\uff0c\u540c\u65f6\u4f60\u9700\u8981\u81ea\u5df1\u4e0b\u8f7dclang\u7f16\u8bd1\u5668\uff0c\u7b2c\u4e00\u6b21\u53ef\u4ee5\u5c1d\u8bd5\uff0c\u5931\u8d25\u540e\u518d\u7528mingw64", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBClang.setWhatsThis(QCoreApplication.translate("Form", u"\u901f\u5ea6\u6700\u5feb\uff0c\u6bd4mingw64\u6700\u5feb\u80fd\u5feb5\u500d\u4ee5\u4e0a\uff0c\u4f46\u662f\u6253\u5305\u62a5\u9519\u6982\u7387\u63d0\u9ad8\uff0c\u540c\u65f6\u4f60\u9700\u8981\u81ea\u5df1\u4e0b\u8f7dclang\u7f16\u8bd1\u5668\uff0c\u7b2c\u4e00\u6b21\u53ef\u4ee5\u5c1d\u8bd5\uff0c\u5931\u8d25\u540e\u518d\u7528mingw64", None))
#endif // QT_CONFIG(whatsthis)
        self.CBClang.setText(QCoreApplication.translate("Form", u"\u5f00\u542fclang\n"
"--clang", None))
#if QT_CONFIG(tooltip)
        self.CBMingw64.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8be5\u9009\u9879\u7528\u6765\u5f00\u542fmingw64\u8fdb\u884c\u52a0\u901f\uff0cnuitka\u4f1a\u81ea\u52a8\u4e0b\u8f7d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CBMingw64.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8be5\u9009\u9879\u7528\u6765\u5f00\u542fmingw64\u8fdb\u884c\u52a0\u901f\uff0cnuitka\u4f1a\u81ea\u52a8\u4e0b\u8f7d</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CBMingw64.setText(QCoreApplication.translate("Form", u"\u5f00\u542fmingw64\n"
"--mingw64 ", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Form", u"\u8bf7\u4e0d\u8981\u8bbe\u7f6e\u5927\u4e8e\u81ea\u5df1\u7535\u8111\u6838\u5fc3\u7684\u7ebf\u7a0b\uff0c\u901a\u5e38\u8bbe\u7f6e\u4e3a6\u6216\u80058\u5373\u53ef", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u7684\u7ebf\u7a0b jobs", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u5176\u4ed6\u9009\u9879", None))
#if QT_CONFIG(tooltip)
        self.CBQuiet.setToolTip(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBQuiet.setStatusTip(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBQuiet.setWhatsThis(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(whatsthis)
        self.CBQuiet.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u5b89\u9759\u6253\u5305\u6a21\u5f0f(\u53ea\u8f93\u51fa\u9519\u8bef)\n"
"--quiet", None))
#if QT_CONFIG(tooltip)
        self.CBCleanCache.setToolTip(QCoreApplication.translate("Form", u"remove-output", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBCleanCache.setStatusTip(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBCleanCache.setWhatsThis(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.CBCleanCache.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u6240\u6709\u7f13\u5b58\n"
"--clean-cache", None))
#if QT_CONFIG(tooltip)
        self.CBwindowsUacAdmin.setToolTip(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u88ab\u8fd0\u884c\u7684\u65f6\u5019\u4f1a\u5411\u7528\u6237\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650\u8fd0\u884c(\u4ec5window)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBwindowsUacAdmin.setStatusTip(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u88ab\u8fd0\u884c\u7684\u65f6\u5019\u4f1a\u5411\u7528\u6237\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650\u8fd0\u884c(\u4ec5window)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBwindowsUacAdmin.setWhatsThis(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u88ab\u8fd0\u884c\u7684\u65f6\u5019\u4f1a\u5411\u7528\u6237\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650\u8fd0\u884c(\u4ec5window)", None))
#endif // QT_CONFIG(whatsthis)
        self.CBwindowsUacAdmin.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u83b7\u53d6\u7ba1\u7406\u5458\u6743\u9650\n"
"--windows-uac-admin", None))
#if QT_CONFIG(tooltip)
        self.CBDisableConsole.setToolTip(QCoreApplication.translate("Form", u"\u8bf7\u4e0d\u8981\u5728\u4e00\u5f00\u59cb\u76f4\u63a5\u4f7f\u7528\uff0c\u8bf7\u786e\u4fdd\u81ea\u5df1\u7684\u7a0b\u5e8f\u6253\u5305\u4e4b\u540e\u80fd\u591f\u8fd0\u884c\u518d\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBDisableConsole.setStatusTip(QCoreApplication.translate("Form", u"\u8bf7\u4e0d\u8981\u5728\u4e00\u5f00\u59cb\u76f4\u63a5\u4f7f\u7528\uff0c\u8bf7\u786e\u4fdd\u81ea\u5df1\u7684\u7a0b\u5e8f\u6253\u5305\u4e4b\u540e\u80fd\u591f\u8fd0\u884c\u518d\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBDisableConsole.setWhatsThis(QCoreApplication.translate("Form", u"\u8bf7\u4e0d\u8981\u5728\u4e00\u5f00\u59cb\u76f4\u63a5\u4f7f\u7528\uff0c\u8bf7\u786e\u4fdd\u81ea\u5df1\u7684\u7a0b\u5e8f\u6253\u5305\u4e4b\u540e\u80fd\u591f\u8fd0\u884c\u518d\u5f00\u542f\u8fd9\u4e2a\u9009\u9879", None))
#endif // QT_CONFIG(whatsthis)
        self.CBDisableConsole.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u547d\u4ee4\u884c\n"
"--windows-disable-console", None))
#if QT_CONFIG(tooltip)
        self.CBLto.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5173\u95edLTO\u80fd\u907f\u514d\u6765\u81ea\u7f16\u8bd1\u5668\u7684\u9519\u8bef\uff0cLTO\u5728nuitka\u662f\u9ed8\u8ba4\u5f00\u542f\u7684</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBLto.setStatusTip(QCoreApplication.translate("Form", u"\u5173\u95edLTO\u80fd\u907f\u514d\u6765\u81ea\u7f16\u8bd1\u5668\u7684\u9519\u8bef\uff0cLTO\u5728nuitka\u662f\u9ed8\u8ba4\u5f00\u542f\u7684", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBLto.setWhatsThis(QCoreApplication.translate("Form", u"\u5173\u95edLTO\u80fd\u907f\u514d\u6765\u81ea\u7f16\u8bd1\u5668\u7684\u9519\u8bef\uff0cLTO\u5728nuitka\u662f\u9ed8\u8ba4\u5f00\u542f\u7684", None))
#endif // QT_CONFIG(whatsthis)
        self.CBLto.setText(QCoreApplication.translate("Form", u"\u5173\u95edlto\n"
"--lto=no", None))
#if QT_CONFIG(tooltip)
        self.CBRemoveOutput.setToolTip(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBRemoveOutput.setStatusTip(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBRemoveOutput.setWhatsThis(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
        self.CBRemoveOutput.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5220\u9664\u6784\u5efa\u6587\u4ef6\u5939\n"
"remove-output", None))
#if QT_CONFIG(tooltip)
        self.CBShowMemory.setToolTip(QCoreApplication.translate("Form", u"\u663e\u793a\u5185\u5b58", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBShowMemory.setStatusTip(QCoreApplication.translate("Form", u"\u663e\u793a\u5185\u5b58", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBShowMemory.setWhatsThis(QCoreApplication.translate("Form", u"\u663e\u793a\u5185\u5b58", None))
#endif // QT_CONFIG(whatsthis)
        self.CBShowMemory.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u5185\u5b58\u5360\u7528\n"
"-show-memory", None))
#if QT_CONFIG(tooltip)
        self.CBDisableCcache.setToolTip(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBDisableCcache.setStatusTip(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBDisableCcache.setWhatsThis(QCoreApplication.translate("Form", u"\u8be5\u63a7\u4ef6\u6709\u66f4\u8be6\u7ec6\u7684\u8bf4\u660e\uff0c\u8bf7\u70b9\u51fb\u53f3\u4e0a\u89d2\u7684\u5c0f\u56fe\u6807\u518d\u70b9\u51fb\u8fd9\u91cc", None))
#endif // QT_CONFIG(whatsthis)
        self.CBDisableCcache.setText(QCoreApplication.translate("Form", u"\u4e0d\u4f7f\u7528\u4e0a\u4e00\u6b21\u7684\u7f13\u5b58\uff0c\u9632\u6b62\u6253\u5305\u5931\u8d25\n"
"disable-ccache", None))
#if QT_CONFIG(tooltip)
        self.CBShowProgress.setToolTip(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u5728\u6253\u5305\u7684\u65f6\u5019\u663e\u793a\u66f4\u591a\u7684\u8fdb\u5ea6\u6761", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.CBShowProgress.setStatusTip(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u5728\u6253\u5305\u7684\u65f6\u5019\u663e\u793a\u66f4\u591a\u7684\u8fdb\u5ea6\u6761", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.CBShowProgress.setWhatsThis(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u5728\u6253\u5305\u7684\u65f6\u5019\u663e\u793a\u66f4\u591a\u7684\u8fdb\u5ea6\u6761", None))
#endif // QT_CONFIG(whatsthis)
        self.CBShowProgress.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u8fdb\u5ea6\u6761\n"
"--show-progress", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51faexe\u7684\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.LBCompanyName.setToolTip(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBCompanyName.setStatusTip(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBCompanyName.setWhatsThis(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(whatsthis)
        self.LBCompanyName.setText(QCoreApplication.translate("Form", u"\u516c\u53f8\u540d\u79f0\n"
"--windows-company-name", None))
#if QT_CONFIG(tooltip)
        self.LBFileVersion.setToolTip(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBFileVersion.setStatusTip(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBFileVersion.setWhatsThis(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
        self.LBFileVersion.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c\n"
"--windows-file-version", None))
#if QT_CONFIG(tooltip)
        self.LECompanyName.setToolTip(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LECompanyName.setStatusTip(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LECompanyName.setWhatsThis(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u8bbe\u7f6e\u516c\u53f8\u7684\u540d\u5b57", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.LBFileDescription.setToolTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBFileDescription.setStatusTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBFileDescription.setWhatsThis(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(whatsthis)
        self.LBFileDescription.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u63cf\u8ff0\n"
"--windows-file-description", None))
#if QT_CONFIG(tooltip)
        self.LBProductVersion.setToolTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LBProductVersion.setStatusTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LBProductVersion.setWhatsThis(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
        self.LBProductVersion.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7248\u672c\n"
"--windows-product-version", None))
#if QT_CONFIG(tooltip)
        self.LEFileVersion.setToolTip(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEFileVersion.setStatusTip(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEFileVersion.setWhatsThis(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.LEProductVersion.setToolTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEProductVersion.setStatusTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEProductVersion.setWhatsThis(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u7248\u672c", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.LEFileDescription.setToolTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEFileDescription.setStatusTip(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEFileDescription.setWhatsThis(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7684\u63cf\u8ff0", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.LEFileDescription.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

