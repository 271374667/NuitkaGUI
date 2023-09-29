# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'embed_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QScrollArea, QSizePolicy,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from customWidget.filetree import FileTree
from qmaterialwidgets import (FilledPushButton, StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(861, 546)
        self.scrollArea_3 = QScrollArea(Form)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(10, 10, 841, 521))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 839, 519))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = StrongBodyLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(9)
        font.setBold(False)
        self.label_4.setFont(font)

        self.verticalLayout_14.addWidget(self.label_4)

        self.treeWidget = FileTree(self.scrollAreaWidgetContents_3)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_14.addWidget(self.treeWidget)

        self.BTNFlushDir = FilledPushButton(self.scrollAreaWidgetContents_3)
        self.BTNFlushDir.setObjectName(u"BTNFlushDir")

        self.verticalLayout_14.addWidget(self.BTNFlushDir)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5d4c\u5165\u6587\u4ef6\uff0c\u5728\u4e0b\u9762\u9009\u4e2d\u4f60\u9700\u8981\u6253\u5305\u7684\u6587\u4ef6\uff0c\u8fd9\u4e9b\u5185\u5bb9\u6700\u7ec8\u4f1a\u4f1a\u88ab\u7f16\u8bd1\u5230exe\u5f53\u4e2d\uff0c\u5176\u4e2d\u7684\u8def\u5f84\u5219\u662f\u91c7\u7528\u76f8\u5bf9\u6253\u5305\u6587\u4ef6\u7684\u8def\u5f84", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"\u6587\u4ef6\u7c7b\u578b", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"\u76f8\u5bf9\u8def\u5f84", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"\u7edd\u5bf9\u8def\u5f84", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u540d\u79f0", None));
#if QT_CONFIG(tooltip)
        self.BTNFlushDir.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8b66\u544a:\u5c3d\u53ef\u80fd\u4e0d\u8981\u4f7f\u7528\u9664\u4e86\u9879\u76ee\u8def\u5f84\u5916\u7684\u5176\u4ed6\u8def\u5f84\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u610f\u6599\u4e4b\u5916\u7684\u9519\u8bef</p><p>\u7a0b\u5e8f\u5bfb\u627e\u8fd9\u4e9b\u989d\u5916\u7684\u6587\u4ef6\u662f\u4f7f\u7528\u76f8\u5bf9\u8def\u5f84\u8fdb\u884c\u5bfb\u627e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BTNFlushDir.setStatusTip(QCoreApplication.translate("Form", u"\u8b66\u544a:\u5c3d\u53ef\u80fd\u4e0d\u8981\u4f7f\u7528\u9664\u4e86\u9879\u76ee\u8def\u5f84\u5916\u7684\u5176\u4ed6\u8def\u5f84\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u610f\u6599\u4e4b\u5916\u7684\u9519\u8bef \u7a0b\u5e8f\u5bfb\u627e\u8fd9\u4e9b\u989d\u5916\u7684\u6587\u4ef6\u662f\u4f7f\u7528\u76f8\u5bf9\u8def\u5f84\u8fdb\u884c\u5bfb\u627e", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BTNFlushDir.setWhatsThis(QCoreApplication.translate("Form", u"\u8b66\u544a:\u5c3d\u53ef\u80fd\u4e0d\u8981\u4f7f\u7528\u9664\u4e86\u9879\u76ee\u8def\u5f84\u5916\u7684\u5176\u4ed6\u8def\u5f84\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u610f\u6599\u4e4b\u5916\u7684\u9519\u8bef \u7a0b\u5e8f\u5bfb\u627e\u8fd9\u4e9b\u989d\u5916\u7684\u6587\u4ef6\u662f\u4f7f\u7528\u76f8\u5bf9\u8def\u5f84\u8fdb\u884c\u5bfb\u627e", None))
#endif // QT_CONFIG(whatsthis)
        self.BTNFlushDir.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4e00\u4e2a\u65b0\u7684\u76ee\u5f55", None))
    # retranslateUi

