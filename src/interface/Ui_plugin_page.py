# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plugin_page.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

from qmaterialwidgets import (FilledPushButton, FilledToolButton, TextEdit, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(837, 574)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(210, 30, 591, 521))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = TitleLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(17)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.BTNRemovePlugin = FilledToolButton(self.gridLayoutWidget)
        self.BTNRemovePlugin.setObjectName(u"BTNRemovePlugin")

        self.gridLayout.addWidget(self.BTNRemovePlugin, 4, 1, 1, 1)

        self.listUnselect = QListWidget(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.listUnselect, 2, 0, 4, 1)

        self.BTNAddPlugin = FilledToolButton(self.gridLayoutWidget)
        self.BTNAddPlugin.setObjectName(u"BTNAddPlugin")

        self.gridLayout.addWidget(self.BTNAddPlugin, 3, 1, 1, 1)

        self.label_2 = TitleLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.listSelect = QListWidget(self.gridLayoutWidget)
        self.listSelect.setObjectName(u"listSelect")

        self.gridLayout.addWidget(self.listSelect, 2, 2, 4, 1)

        self.TitleLabel_3 = TitleLabel(Form)
        self.TitleLabel_3.setObjectName(u"TitleLabel_3")
        self.TitleLabel_3.setGeometry(QRect(20, 50, 123, 38))
        self.plainTextEdit = TextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 100, 181, 251))
        self.btnStart1 = FilledPushButton(Form)
        self.btnStart1.setObjectName(u"btnStart1")
        self.btnStart1.setGeometry(QRect(20, 370, 159, 161))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.btnStart1.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u672a\u542f\u7528\u7684\u63d2\u4ef6", None))

        __sortingEnabled = self.listUnselect.isSortingEnabled()
        self.listUnselect.setSortingEnabled(False)
        ___qlistwidgetitem = self.listUnselect.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"pyside6", None));
        ___qlistwidgetitem1 = self.listUnselect.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"pyside2", None));
        ___qlistwidgetitem2 = self.listUnselect.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"pyqt6", None));
        ___qlistwidgetitem3 = self.listUnselect.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"pyqt5", None));
        ___qlistwidgetitem4 = self.listUnselect.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"matplotlib", None));
        ___qlistwidgetitem5 = self.listUnselect.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"tensorflow", None));
        ___qlistwidgetitem6 = self.listUnselect.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form", u"tk-inter", None));
        ___qlistwidgetitem7 = self.listUnselect.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Form", u"pywebview", None));
        ___qlistwidgetitem8 = self.listUnselect.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Form", u"upx", None));
        ___qlistwidgetitem9 = self.listUnselect.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Form", u"multiprocessing", None));
        ___qlistwidgetitem10 = self.listUnselect.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Form", u"trio", None));
        ___qlistwidgetitem11 = self.listUnselect.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Form", u"kivy", None));
        self.listUnselect.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listUnselect.setToolTip(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u662f\u6ca1\u6709\u88ab\u542f\u7528\u7684\u63d2\u4ef6\uff0c\u4f60\u4e5f\u53ef\u4ee5\u4e0a\u5b98\u7f51\u81ea\u5df1\u770b\u6709\u54ea\u4e9b\u5176\u4ed6\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.listUnselect.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.listUnselect.setWhatsThis(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u662f\u6ca1\u6709\u88ab\u542f\u7528\u7684\u63d2\u4ef6\uff0c\u4f60\u4e5f\u53ef\u4ee5\u4e0a\u5b98\u7f51\u81ea\u5df1\u770b\u6709\u54ea\u4e9b\u5176\u4ed6\u7684\u63d2\u4ef6", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5df2\u7ecf\u542f\u7528\u7684\u63d2\u4ef6", None))
        self.TitleLabel_3.setText(QCoreApplication.translate("Form", u"TIPS:", None))
        self.plainTextEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto','Segoe UI','Microsoft YaHei','PingFang SC','SimSun'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u5982\u679c\u4f60\u5bfc\u5165\u4e86\u76f8\u5e94\u7684\u6a21\u5757\uff0c\u90a3\u4e48\u4f60\u9700\u8981\u4ece\u5de6\u8fb9\u9009\u62e9\u5bf9\u5e94\u7684\u63d2\u4ef6\uff0c\u7136\u540e\u53cc\u51fb\u4ed6\u6216\u8005\u70b9\u51fb\u6309\u94ae\u5c06\u5b83\u6dfb\u52a0\u5230\u53f3\u8fb9</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u8fd9\u6837\u505a\u80fd\u591f\u8ba9\u4f60\u66f4\u5feb\u7684\u7f16\u8bd1\uff0c\u800c\u4e14\u6709\u7684\u65f6\u5019\u5982\u679c\u4f60\u6ca1\u6709\u5f00\u542f\u63d2\u4ef6\u6700\u540e\u751a\u81f3\u53ef\u80fd\u65e0\u6cd5\u8fd0\u884c\uff0c\u6bd4\u5982PyQt</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btnStart1.setText(QCoreApplication.translate("Form", u"\u6253\u5305", None))
    # retranslateUi

