# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_page.ui'
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

from qmaterialwidgets import (CaptionLabel, CardWidget, IconWidget, LargeTitleLabel,
    OutlinedPushButton, StrongBodyLabel, SwitchButton)
from src.resource import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(844, 556)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 15, 30, 30)
        self.LargeTitleLabel = LargeTitleLabel(Form)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LargeTitleLabel.sizePolicy().hasHeightForWidth())
        self.LargeTitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.LargeTitleLabel)

        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        sizePolicy1.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.IconWidget = IconWidget(self.CardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy2)
        self.IconWidget.setMinimumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/Icons/materialIcons/icons8_python.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout.addWidget(self.IconWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.strongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.strongBodyLabel.setObjectName(u"strongBodyLabel")

        self.verticalLayout_2.addWidget(self.strongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.CardWidget)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.CaptionLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.OutlinedPushButton_3 = OutlinedPushButton(self.CardWidget)
        self.OutlinedPushButton_3.setObjectName(u"OutlinedPushButton_3")
        sizePolicy2.setHeightForWidth(self.OutlinedPushButton_3.sizePolicy().hasHeightForWidth())
        self.OutlinedPushButton_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.OutlinedPushButton_3)

        self.OutlinedPushButton = OutlinedPushButton(self.CardWidget)
        self.OutlinedPushButton.setObjectName(u"OutlinedPushButton")
        sizePolicy2.setHeightForWidth(self.OutlinedPushButton.sizePolicy().hasHeightForWidth())
        self.OutlinedPushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.OutlinedPushButton)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        sizePolicy1.setHeightForWidth(self.CardWidget_2.sizePolicy().hasHeightForWidth())
        self.CardWidget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.IconWidget_2 = IconWidget(self.CardWidget_2)
        self.IconWidget_2.setObjectName(u"IconWidget_2")
        sizePolicy2.setHeightForWidth(self.IconWidget_2.sizePolicy().hasHeightForWidth())
        self.IconWidget_2.setSizePolicy(sizePolicy2)
        self.IconWidget_2.setMinimumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/materialIcons/icons8_unicast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_2.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.IconWidget_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.strongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.strongBodyLabel_2.setObjectName(u"strongBodyLabel_2")

        self.verticalLayout_3.addWidget(self.strongBodyLabel_2)

        self.CaptionLabel_2 = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_3.addWidget(self.CaptionLabel_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.OutlinedPushButton_2 = OutlinedPushButton(self.CardWidget_2)
        self.OutlinedPushButton_2.setObjectName(u"OutlinedPushButton_2")
        sizePolicy2.setHeightForWidth(self.OutlinedPushButton_2.sizePolicy().hasHeightForWidth())
        self.OutlinedPushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.OutlinedPushButton_2)


        self.verticalLayout.addWidget(self.CardWidget_2)

        self.CardWidget_3 = CardWidget(Form)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        sizePolicy1.setHeightForWidth(self.CardWidget_3.sizePolicy().hasHeightForWidth())
        self.CardWidget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.IconWidget_3 = IconWidget(self.CardWidget_3)
        self.IconWidget_3.setObjectName(u"IconWidget_3")
        sizePolicy2.setHeightForWidth(self.IconWidget_3.sizePolicy().hasHeightForWidth())
        self.IconWidget_3.setSizePolicy(sizePolicy2)
        self.IconWidget_3.setMinimumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/materialIcons/icons8_speedometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_3.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.IconWidget_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.strongBodyLabel_3 = StrongBodyLabel(self.CardWidget_3)
        self.strongBodyLabel_3.setObjectName(u"strongBodyLabel_3")

        self.verticalLayout_4.addWidget(self.strongBodyLabel_3)

        self.CaptionLabel_3 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_4.addWidget(self.CaptionLabel_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.SwitchButton = SwitchButton(self.CardWidget_3)
        self.SwitchButton.setObjectName(u"SwitchButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SwitchButton.sizePolicy().hasHeightForWidth())
        self.SwitchButton.setSizePolicy(sizePolicy3)
        self.SwitchButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.SwitchButton)


        self.verticalLayout.addWidget(self.CardWidget_3)

        self.CardWidget_4 = CardWidget(Form)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        sizePolicy1.setHeightForWidth(self.CardWidget_4.sizePolicy().hasHeightForWidth())
        self.CardWidget_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.IconWidget_4 = IconWidget(self.CardWidget_4)
        self.IconWidget_4.setObjectName(u"IconWidget_4")
        sizePolicy2.setHeightForWidth(self.IconWidget_4.sizePolicy().hasHeightForWidth())
        self.IconWidget_4.setSizePolicy(sizePolicy2)
        self.IconWidget_4.setMinimumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/materialIcons/icons8_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_4.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.IconWidget_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.strongBodyLabel_4 = StrongBodyLabel(self.CardWidget_4)
        self.strongBodyLabel_4.setObjectName(u"strongBodyLabel_4")

        self.verticalLayout_5.addWidget(self.strongBodyLabel_4)

        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_4)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")
        self.CaptionLabel_4.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_5.addWidget(self.CaptionLabel_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.OutlinedPushButton_4 = OutlinedPushButton(self.CardWidget_4)
        self.OutlinedPushButton_4.setObjectName(u"OutlinedPushButton_4")
        sizePolicy2.setHeightForWidth(self.OutlinedPushButton_4.sizePolicy().hasHeightForWidth())
        self.OutlinedPushButton_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.OutlinedPushButton_4)


        self.verticalLayout.addWidget(self.CardWidget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.strongBodyLabel.setText(QCoreApplication.translate("Form", u"Python.exe \u8def\u5f84", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u5728\u8fd9\u91cc\u9009\u62e9 Python.exe \u89e3\u91ca\u5668\u7684\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.OutlinedPushButton_3.setToolTip(QCoreApplication.translate("Form", u"\u81ea\u52a8\u641c\u7d22\u672c\u5730\u53ef\u7528\u7684Python.exe\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
        self.OutlinedPushButton_3.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.OutlinedPushButton.setToolTip(QCoreApplication.translate("Form", u"\u5f53\u524d\u672a\u9009\u62e9Python.exe\u7684\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
        self.OutlinedPushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84", None))
        self.strongBodyLabel_2.setText(QCoreApplication.translate("Form", u"Pip \u6e90", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"\u70b9\u51fb\u8fd9\u91cc\u53ef\u4ee5\u91cd\u65b0\u4e3a pip \u6d4b\u901f\u5e76\u66f4\u65b0 pip \u6e90\u5934,\u5728\u60a8\u4e0b\u8f7d\u7f13\u6162\u65f6\u542f\u7528", None))
#if QT_CONFIG(tooltip)
        self.OutlinedPushButton_2.setToolTip(QCoreApplication.translate("Form", u"\u6ca1\u6709\u627e\u5230\u53ef\u7528\u7684 Pip \u6e90", None))
#endif // QT_CONFIG(tooltip)
        self.OutlinedPushButton_2.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u9009\u62e9", None))
        self.strongBodyLabel_3.setText(QCoreApplication.translate("Form", u"\u9009\u9879\u4f18\u5316(\u5efa\u8bae\u5f00\u542f)", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"NuitkaGUI \u9ed8\u8ba4\u5f00\u542f\u4e86\u4e00\u4e9b\u4f18\u5316\u9009\u9879,\u60a8\u53ef\u4ee5\u5173\u95ed\u4ed6\u4eec\u83b7\u5f97\u5b8c\u5168\u7684\u81ea\u5b9a\u4e49\u4f53\u9a8c", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton.setToolTip(QCoreApplication.translate("Form", u"\u5982\u65e0\u7279\u6b8a\u60c5\u51b5\u8bf7\u4e0d\u8981\u5173\u95ed\u8be5\u9009\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.strongBodyLabel_4.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", u"\u5728\u8fd9\u91cc\u53ef\u4ee5\u6e05\u9664\u6240\u6709\u7684\u914d\u7f6e\u6587\u4ef6,\u5c06\u8f6f\u4ef6\u6062\u590d\u5230\u6700\u521d\u7684\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.OutlinedPushButton_4.setToolTip(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u672c\u5730\u5b58\u50a8\u7684\u914d\u7f6e\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.OutlinedPushButton_4.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316", None))
    # retranslateUi

