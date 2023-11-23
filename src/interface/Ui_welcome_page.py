# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qmaterialwidgets import (BodyLabel, CardWidget, DisplayLabel, FilledPushButton,
    OutlinedPushButton, ProgressBar, TitleLabel, TonalPushButton)
from src.resource import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 650)
        Form.setMinimumSize(QSize(1000, 650))
        Form.setMaximumSize(QSize(1000, 650))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.DisplayLabel = DisplayLabel(Form)
        self.DisplayLabel.setObjectName(u"DisplayLabel")
        self.DisplayLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.DisplayLabel)

        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy)
        self.BodyLabel.setAlignment(Qt.AlignCenter)
        self.BodyLabel.setWordWrap(True)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_4.addWidget(self.BodyLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 10, 30, 10)
        self.CardWidget_3 = CardWidget(Form)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.TitleLabel_3 = TitleLabel(self.CardWidget_3)
        self.TitleLabel_3.setObjectName(u"TitleLabel_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel_3.sizePolicy().hasHeightForWidth())
        self.TitleLabel_3.setSizePolicy(sizePolicy1)
        self.TitleLabel_3.setMinimumSize(QSize(0, 0))
        self.TitleLabel_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.TitleLabel_3.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.TitleLabel_3)

        self.BodyLabel_4 = BodyLabel(self.CardWidget_3)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        sizePolicy.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy)
        self.BodyLabel_4.setAlignment(Qt.AlignCenter)
        self.BodyLabel_4.setWordWrap(True)
        self.BodyLabel_4.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_3.addWidget(self.BodyLabel_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.TonalPushButton_3 = TonalPushButton(self.CardWidget_3)
        self.TonalPushButton_3.setObjectName(u"TonalPushButton_3")

        self.verticalLayout_3.addWidget(self.TonalPushButton_3)

        self.FilledPushButton_3 = FilledPushButton(self.CardWidget_3)
        self.FilledPushButton_3.setObjectName(u"FilledPushButton_3")

        self.verticalLayout_3.addWidget(self.FilledPushButton_3)


        self.horizontalLayout.addWidget(self.CardWidget_3)

        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.CardWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CardWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.CardWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.TitleLabel = TitleLabel(self.CardWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)
        self.TitleLabel.setMinimumSize(QSize(0, 0))
        self.TitleLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.TitleLabel.setWordWrap(False)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.BodyLabel_2 = BodyLabel(self.CardWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy)
        self.BodyLabel_2.setAlignment(Qt.AlignCenter)
        self.BodyLabel_2.setWordWrap(True)
        self.BodyLabel_2.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout.addWidget(self.BodyLabel_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.TonalPushButton = TonalPushButton(self.CardWidget)
        self.TonalPushButton.setObjectName(u"TonalPushButton")

        self.verticalLayout.addWidget(self.TonalPushButton)

        self.FilledPushButton = FilledPushButton(self.CardWidget)
        self.FilledPushButton.setObjectName(u"FilledPushButton")

        self.verticalLayout.addWidget(self.FilledPushButton)


        self.horizontalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.TitleLabel_2 = TitleLabel(self.CardWidget_2)
        self.TitleLabel_2.setObjectName(u"TitleLabel_2")
        sizePolicy1.setHeightForWidth(self.TitleLabel_2.sizePolicy().hasHeightForWidth())
        self.TitleLabel_2.setSizePolicy(sizePolicy1)
        self.TitleLabel_2.setMinimumSize(QSize(0, 0))
        self.TitleLabel_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.TitleLabel_2.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.TitleLabel_2)

        self.BodyLabel_3 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy)
        self.BodyLabel_3.setAlignment(Qt.AlignCenter)
        self.BodyLabel_3.setWordWrap(True)
        self.BodyLabel_3.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.BodyLabel_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.TonalPushButton_2 = TonalPushButton(self.CardWidget_2)
        self.TonalPushButton_2.setObjectName(u"TonalPushButton_2")

        self.verticalLayout_2.addWidget(self.TonalPushButton_2)

        self.FilledPushButton_2 = FilledPushButton(self.CardWidget_2)
        self.FilledPushButton_2.setObjectName(u"FilledPushButton_2")

        self.verticalLayout_2.addWidget(self.FilledPushButton_2)


        self.horizontalLayout.addWidget(self.CardWidget_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.OutlinedPushButton = OutlinedPushButton(Form)
        self.OutlinedPushButton.setObjectName(u"OutlinedPushButton")
        self.OutlinedPushButton.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.OutlinedPushButton.sizePolicy().hasHeightForWidth())
        self.OutlinedPushButton.setSizePolicy(sizePolicy2)
        self.OutlinedPushButton.setSizeIncrement(QSize(0, 0))
        self.OutlinedPushButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.OutlinedPushButton)

        self.ProgressBar = ProgressBar(Form)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setMaximum(3)
        self.ProgressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.ProgressBar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9996\u6b21\u8bbe\u7f6e\u9875\u9762", None))
        self.DisplayLabel.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u4f7f\u7528NuitkaGUI", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f53\u524d\u7a97\u4f53\u4ec5\u4f1a\u51fa\u73b0\u4e00\u6b21\uff0c\u60a8\u9700\u8981\u5b8c\u6210\u4e0b\u9762\u7684\u914d\u7f6e\u9879</p><p>\u60a8\u4e5f\u53ef\u4ee5\u7a0d\u540e\u5728\u8bbe\u7f6e\u4e2d\u4fee\u6539</p></body></html>", None))
        self.TitleLabel_3.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u955c\u50cf\u6e90", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u9009\u62e9\u4e00\u4e2a\u6700\u5feb\u7684 pip \u4e0b\u8f7d\u955c\u50cf\u6e90</p><p>\u70b9\u51fb\u4e0b\u65b9\u6309\u94ae\u81ea\u52a8\u4ece\u5185\u7f6e\u76845\u4e2a\u955c\u50cf\u6e90\u4e2d\u9009\u62e9\u6700\u5feb\u7684\u4e00\u4e2a\u4e3a\u9ed8\u8ba4\u955c\u50cf\u6e90</p></body></html>", None))
        self.TonalPushButton_3.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u5b98\u65b9pypi", None))
        self.FilledPushButton_3.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u68c0\u6d4b", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"Python.exe\u8def\u5f84", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u9009\u62e9\u4e00\u4e2a\u53ef\u7528\u7684 Python.exe \u8def\u5f84</p><p>\u9009\u62e9\u5b8c\u6bd5\u4f1a\u7acb\u5373\u4e0b\u8f7d\u4e00\u4e9b\u7b2c\u4e09\u65b9\u5e93<br/></p></body></html>", None))
        self.TonalPushButton.setText(QCoreApplication.translate("Form", u"\u624b\u52a8\u641c\u7d22", None))
        self.FilledPushButton.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u641c\u7d22", None))
        self.TitleLabel_2.setText(QCoreApplication.translate("Form", u"GCC\u7f16\u8bd1\u5668", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Nuitka\u4f9d\u8d56GCC\u8fdb\u884c\u7f16\u8bd1</p><p>\u5982\u679c\u60a8\u5df2\u7ecf\u5b89\u88c5\u4e86GCC\u53ef\u4ee5\u70b9\u51fb\u68c0\u6d4b\u6765\u6d4b\u8bd5GCC\u662f\u5426\u53ef\u7528</p></body></html>", None))
        self.TonalPushButton_2.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4bGcc", None))
        self.FilledPushButton_2.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u4e0b\u8f7d", None))
        self.OutlinedPushButton.setText(QCoreApplication.translate("Form", u"\u60a8\u9700\u8981\u5148\u5b8c\u6210\u8bbe\u7f6e", None))
    # retranslateUi

