# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 10, 30, 30)
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
        self.LBPyFilePath.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout.addWidget(self.LBPyFilePath)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.BTNGetPy = FilledPushButton(self.CardWidget)
        self.BTNGetPy.setObjectName(u"BTNGetPy")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/materialIcons/icons8_double_down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BTNGetPy.setIcon(icon1)

        self.horizontalLayout.addWidget(self.BTNGetPy)


        self.verticalLayout_4.addWidget(self.CardWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.CardWidget_3 = CardWidget(basic_page)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CardWidget_3.sizePolicy().hasHeightForWidth())
        self.CardWidget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.SubtitleLabel_2 = SubtitleLabel(self.CardWidget_3)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        sizePolicy.setHeightForWidth(self.SubtitleLabel_2.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_2.setSizePolicy(sizePolicy)
        self.SubtitleLabel_2.setAlignment(Qt.AlignCenter)
        self.SubtitleLabel_2.setProperty("pixelFontSize", 28)

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
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 30, 30, 30)
        self.SubtitleLabel_3 = SubtitleLabel(self.CardWidget_4)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        sizePolicy.setHeightForWidth(self.SubtitleLabel_3.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_3.setSizePolicy(sizePolicy)
        self.SubtitleLabel_3.setAlignment(Qt.AlignCenter)
        self.SubtitleLabel_3.setProperty("pixelFontSize", 28)

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
        icon2 = QIcon()
        icon2.addFile(u":/Icons/materialIcons/icons8_load_cargo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BTNStart.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.BTNStart)


        self.verticalLayout_4.addWidget(self.ElevatedCardWidget)


        self.retranslateUi(basic_page)

        QMetaObject.connectSlotsByName(basic_page)
    # setupUi

    def retranslateUi(self, basic_page):
        basic_page.setWindowTitle(QCoreApplication.translate("basic_page", u"basic_page", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u4e00\u4e2aPython\u6587\u4ef6", None))
        self.LBPyFilePath.setText(QCoreApplication.translate("basic_page", u"\u62d6\u52a8\u6587\u4ef6\u8fdb\u5165\u7a97\u4f53\u9009\u62e9\u88ab\u6253\u5305\u7684 .py \u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.BTNGetPy.setToolTip(QCoreApplication.translate("basic_page", u"\u5f53\u524d\u672a\u9009\u62e9\u4efb\u4f55\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.BTNGetPy.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u6587\u4ef6", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("basic_page", u"\u8f93\u51fa\u8def\u5f84", None))
        self.LBOutputPath.setText(QCoreApplication.translate("basic_page", u"<html><head/><body><p>\u60a8\u7684\u7a0b\u5e8f\u88ab\u6253\u5305\u4e4b\u540e\u5b58\u653e\u7684\u4f4d\u7f6e</p><p><br/></p><p><span style=\" font-style:italic;\">\u5982\u679c\u60a8\u672a\u8fdb\u884c\u9009\u62e9\uff0c\u5219\u9ed8\u8ba4\u4f1a\u5728\u88ab\u6253\u5305\u7684 Python \u6587\u4ef6\u76ee\u5f55\u4e0b\u65b0\u5efa\u4e00\u4e2a output \u6587\u4ef6\u5939\u8fdb\u884c\u4fdd\u5b58</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.BTNOutputPath.setToolTip(QCoreApplication.translate("basic_page", u"\u5f53\u524d\u672a\u9009\u62e9\u4efb\u4f55\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.BTNOutputPath.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u8def\u5f84", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("basic_page", u"\u8bbe\u7f6e\u56fe\u6807", None))
        self.LBIcon.setText(QCoreApplication.translate("basic_page", u"<html><head/><body><p>\u4e3a\u60a8\u7684\u7a0b\u5e8f\u52a0\u4e0a\u5fc3\u7231\u7684\u56fe\u6807</p><p>\u60a8\u4e5f\u53ef\u4ee5\u5ffd\u89c6\u8be5\u9009\u9879\uff0c\u8f6f\u4ef6\u9ed8\u8ba4\u4f1a\u63d0\u4f9b\u4e00\u4e2a\u56fe\u6807</p><p><br/><span style=\" font-style:italic;\">\u9ed8\u8ba4\u56fe\u6807\u6837\u5f0f\u5982\u4e0b</span></p><p><img src=\":/Icons/materialIcons/logo-small.png\"/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.BTNIcon.setToolTip(QCoreApplication.translate("basic_page", u"\u5f53\u524d\u4f7f\u7528\u9ed8\u8ba4\u56fe\u6807", None))
#endif // QT_CONFIG(tooltip)
        self.BTNIcon.setText(QCoreApplication.translate("basic_page", u"\u9009\u62e9\u56fe\u6807", None))
        self.SwitchButton.setText(QCoreApplication.translate("basic_page", u"\u5f53\u524d:\u591a\u6587\u4ef6", None))
        self.SwitchButton.setOnText(QCoreApplication.translate("basic_page", u"\u5f53\u524d:\u5355\u6587\u4ef6", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("basic_page", u"\u5f53\u524d:\u591a\u6587\u4ef6", None))
        self.BTNStart.setText(QCoreApplication.translate("basic_page", u"\u5f00\u59cb\u6253\u5305", None))
    # retranslateUi

