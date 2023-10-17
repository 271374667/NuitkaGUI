# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qmaterialwidgets import (BodyLabel, DisplayLabel, IconWidget, OutlinedPushButton,
    ScrollArea, SubtitleLabel, TextPushButton)
from src.resource import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(928, 561)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea = ScrollArea(Form)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setFrameShape(QFrame.StyledPanel)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 926, 559))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.IconWidget = IconWidget(self.scrollAreaWidgetContents)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(100, 100))
        icon = QIcon()
        icon.addFile(u":/Icons/materialIcons/software_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout.addWidget(self.IconWidget)

        self.DisplayLabel = DisplayLabel(self.scrollAreaWidgetContents)
        self.DisplayLabel.setObjectName(u"DisplayLabel")

        self.horizontalLayout.addWidget(self.DisplayLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.SubtitleLabel)

        self.BodyLabel = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.BodyLabel)

        self.TextPushButton = TextPushButton(self.scrollAreaWidgetContents)
        self.TextPushButton.setObjectName(u"TextPushButton")

        self.verticalLayout_2.addWidget(self.TextPushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.DisplayLabel.setText(QCoreApplication.translate("Form", u"NuitkaGUI", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u7684\u4e00\u4e9b\u8bdd", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8be5\u9879\u76ee\u662f\u6211\u5bf9\u4e8e MVP \u8bbe\u8ba1\u6846\u67b6\u7684\u6478\u7d22\u6210\u679c,\u540c\u65f6\u4e5f\u662f\u7ed9\u5f53\u65f6\u9e3d\u4e86\u5f88\u4e45\u7684 NuitkaGUI \u4e00\u6b21\u65b0\u7684\u673a\u4f1a</p><p>\u5982\u679c\u60f3\u8981\u5b66\u4e60\u5176\u4e2d\u7684 MVP \u67b6\u6784\u6b22\u8fce\u6765\u6211\u7684 B\u7ad9 \u770b\u6211\u7684 PyQt \u6559\u5b66\u89c6\u9891</p><p><span style=\" color:#606060;\">Python\u5b66\u4e60QQ\u7fa4\u4e3b\u7fa4:633585910<br/>Python\u5b66\u4e60QQ\u7fa42\u7fa4:557434492</span></p><p><br/></p></body></html>", None))
        self.TextPushButton.setText(QCoreApplication.translate("Form", u"\u706b\u901f\u524d\u5f80\u6211\u7684B\u7ad9", None))
    # retranslateUi

