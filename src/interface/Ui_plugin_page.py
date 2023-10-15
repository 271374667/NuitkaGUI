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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qmaterialwidgets import (BodyLabel, CardWidget, ElevatedCardWidget, FilledPushButton,
    IconWidget, OutlinedCardWidget, SmoothScrollArea, TitleLabel,
    TonalPushButton)
from src.resource import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(816, 493)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 15, 30, 30)
        self.ElevatedCardWidget = ElevatedCardWidget(Form)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.horizontalLayout = QHBoxLayout(self.ElevatedCardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.IconWidget = IconWidget(self.ElevatedCardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(50, 50))
        self.IconWidget.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/Icons/materialIcons/icons8_info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout.addWidget(self.IconWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TitleLabel = TitleLabel(self.ElevatedCardWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.BodyLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TonalPushButton = TonalPushButton(self.ElevatedCardWidget)
        self.TonalPushButton.setObjectName(u"TonalPushButton")
        self.TonalPushButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_4.addWidget(self.TonalPushButton)

        self.FilledPushButton = FilledPushButton(self.ElevatedCardWidget)
        self.FilledPushButton.setObjectName(u"FilledPushButton")
        self.FilledPushButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_4.addWidget(self.FilledPushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.ElevatedCardWidget)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 756, 317))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u8bf4\u660e", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Nuitka\u9700\u8981\u5f00\u542f\u63d2\u4ef6\u6765\u652f\u6301\u7279\u6b8a\u7684\u6a21\u5757\u5de5\u4f5c</p><p>\u60a8\u4e5f\u53ef\u4ee5\u9009\u62e9\u81ea\u52a8\u5206\u6790\u4ee5\u6b64\u6536\u96c6\u9009\u4e2d &quot;.py&quot; \u548c\u9879\u76ee\u76ee\u5f55\u4e0b\u6240\u6709\u7684\u4f9d\u8d56\u5e93</p></body></html>", None))
        self.TonalPushButton.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u5df2\u9009\u62e9", None))
        self.FilledPushButton.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5206\u6790", None))
    # retranslateUi

