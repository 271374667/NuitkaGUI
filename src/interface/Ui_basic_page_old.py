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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qmaterialwidgets import (BodyLabel, CaptionLabel, CardWidget, ElevatedCardWidget,
    FilledPushButton, IconWidget, OutlinedCardWidget, OutlinedPushButton,
    StrongBodyLabel, SubtitleLabel, SwitchButton)
from src.resource import rc_res

class Ui_basic_page(object):
    def setupUi(self, basic_page):
        if not basic_page.objectName():
            basic_page.setObjectName(u"basic_page")
        basic_page.resize(785, 551)
        self.verticalLayout_4 = QVBoxLayout(basic_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.CardWidget = CardWidget(basic_page)
        self.CardWidget.setObjectName(u"CardWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.IWSelectedFile = IconWidget(self.CardWidget)
        self.IWSelectedFile.setObjectName(u"IWSelectedFile")
        self.IWSelectedFile.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icons/materialIcons/no_file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IWSelectedFile.setIcon(icon)

        self.horizontalLayout.addWidget(self.IWSelectedFile)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.verticalLayout.addWidget(self.StrongBodyLabel)

        self.LBPyFilePath = CaptionLabel(self.CardWidget)
        self.LBPyFilePath.setObjectName(u"LBPyFilePath")

        self.verticalLayout.addWidget(self.LBPyFilePath)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.BTNGetPy = FilledPushButton(self.CardWidget)
        self.BTNGetPy.setObjectName(u"BTNGetPy")

        self.horizontalLayout.addWidget(self.BTNGetPy)


        self.verticalLayout_4.addWidget(self.CardWidget)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 0, 30, -1)
        self.CardWidget_3 = CardWidget(basic_page)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SubtitleLabel_2 = SubtitleLabel(self.CardWidget_3)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.SubtitleLabel_2)

        self.LBOutputPath = BodyLabel(self.CardWidget_3)
        self.LBOutputPath.setObjectName(u"LBOutputPath")
        self.LBOutputPath.setTextFormat(Qt.RichText)
        self.LBOutputPath.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.LBOutputPath.setWordWrap(True)
        self.LBOutputPath.setMargin(0)
        self.LBOutputPath.setProperty("strikeOut", False)

        self.verticalLayout_3.addWidget(self.LBOutputPath)

        self.BTNOutputPath = OutlinedPushButton(self.CardWidget_3)
        self.BTNOutputPath.setObjectName(u"BTNOutputPath")
        self.BTNOutputPath.setBorderRadius(10)

        self.verticalLayout_3.addWidget(self.BTNOutputPath)


        self.horizontalLayout_3.addWidget(self.CardWidget_3)

        self.CardWidget_4 = CardWidget(basic_page)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.verticalLayout_5 = QVBoxLayout(self.CardWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.CardWidget_4)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.LBIcon = BodyLabel(self.CardWidget_4)
        self.LBIcon.setObjectName(u"LBIcon")
        self.LBIcon.setTextFormat(Qt.RichText)
        self.LBIcon.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.LBIcon.setWordWrap(True)
        self.LBIcon.setMargin(0)
        self.LBIcon.setProperty("strikeOut", False)

        self.verticalLayout_5.addWidget(self.LBIcon)

        self.BTNIcon = OutlinedPushButton(self.CardWidget_4)
        self.BTNIcon.setObjectName(u"BTNIcon")
        self.BTNIcon.setBorderRadius(10)

        self.verticalLayout_5.addWidget(self.BTNIcon)


        self.horizontalLayout_3.addWidget(self.CardWidget_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.ElevatedCardWidget = ElevatedCardWidget(basic_page)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        sizePolicy.setHeightForWidth(self.ElevatedCardWidget.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.ElevatedCardWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SwitchButton = SwitchButton(self.ElevatedCardWidget)
        self.SwitchButton.setObjectName(u"SwitchButton")
        self.SwitchButton.setMaximumSize(QSize(150, 24))

        self.horizontalLayout_2.addWidget(self.SwitchButton)

        self.BTNStart = FilledPushButton(self.ElevatedCardWidget)
        self.BTNStart.setObjectName(u"BTNStart")

        self.horizontalLayout_2.addWidget(self.BTNStart)


        self.verticalLayout_4.addWidget(self.ElevatedCardWidget)


        self.retranslateUi(basic_page)

        QMetaObject.connectSlotsByName(basic_page)
    # setupUi

    def retranslateUi(self, basic_page):
        basic_page.setWindowTitle(QCoreApplication.translate("basic_page", u"basic_page", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u4e00\u4e2aPython\u6587\u4ef6", None))
        self.LBPyFilePath.setText(QCoreApplication.translate("basic_page", u"\u5728\u8fd9\u91cc\u9009\u62e9\u9700\u8981\u88ab\u6253\u5305\u7684 .py \u6587\u4ef6", None))
        self.BTNGetPy.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u6587\u4ef6", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("basic_page", u"\u8f93\u51fa\u8def\u5f84", None))
        self.LBOutputPath.setText(QCoreApplication.translate("basic_page", u"<html><head/><body><p>\u60a8\u7684\u7a0b\u5e8f\u88ab\u6253\u5305\u4e4b\u540e\u5b58\u653e\u7684\u4f4d\u7f6e</p></body></html>", None))
        self.BTNOutputPath.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u8def\u5f84", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("basic_page", u"\u8bbe\u7f6e\u56fe\u6807", None))
        self.LBIcon.setText(QCoreApplication.translate("basic_page", u"<html><head/><body><p>\u4e3a\u60a8\u7684\u7a0b\u5e8f\u52a0\u4e0a\u5fc3\u7231\u7684\u56fe\u6807</p><p>\u60a8\u4e5f\u53ef\u4ee5\u5ffd\u89c6\u8be5\u9009\u9879\uff0c\u8f6f\u4ef6\u9ed8\u8ba4\u4f1a\u63d0\u4f9b\u4e00\u4e2a\u56fe\u6807</p></body></html>", None))
        self.BTNIcon.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u56fe\u6807", None))
        self.SwitchButton.setText(QCoreApplication.translate("basic_page", u"\u5f53\u524d:\u591a\u6587\u4ef6", None))
        self.SwitchButton.setOnText(QCoreApplication.translate("basic_page", u"\u5f53\u524d:\u5355\u6587\u4ef6", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("basic_page", u"\u5f53\u524d:\u591a\u6587\u4ef6", None))
        self.BTNStart.setText(QCoreApplication.translate("basic_page", u"\u5f00\u59cb\u6253\u5305", None))
    # retranslateUi

