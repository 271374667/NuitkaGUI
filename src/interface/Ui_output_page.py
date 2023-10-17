# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_page.ui'
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
    QVBoxLayout, QWidget)

from qmaterialwidgets import (BodyLabel, CardWidget, ElevatedCardWidget, FilledPushButton,
    IconWidget, OutlinedCardWidget, OutlinedPushButton, TextEdit,
    TextPushButton, TitleLabel)
from src.resource import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(860, 546)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 10, 30, 30)
        self.ElevatedCardWidget = ElevatedCardWidget(Form)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.ElevatedCardWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.IconWidget = IconWidget(self.ElevatedCardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(64)
        sizePolicy.setVerticalStretch(64)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(64, 64))
        icon = QIcon()
        icon.addFile(u":/Icons/materialIcons/icons8_code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.IconWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.TitleLabel = TitleLabel(self.ElevatedCardWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)
        self.BodyLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout.addWidget(self.BodyLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.ElevatedCardWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TextEdit = TextEdit(self.CardWidget)
        self.TextEdit.setObjectName(u"TextEdit")
        self.TextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.TextEdit)

        self.TextPushButton_2 = TextPushButton(self.CardWidget)
        self.TextPushButton_2.setObjectName(u"TextPushButton_2")

        self.verticalLayout_2.addWidget(self.TextPushButton_2)


        self.horizontalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TextEdit_2 = TextEdit(self.CardWidget_2)
        self.TextEdit_2.setObjectName(u"TextEdit_2")

        self.verticalLayout_3.addWidget(self.TextEdit_2)

        self.TextPushButton = TextPushButton(self.CardWidget_2)
        self.TextPushButton.setObjectName(u"TextPushButton")

        self.verticalLayout_3.addWidget(self.TextPushButton)


        self.horizontalLayout.addWidget(self.CardWidget_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.FilledPushButton = FilledPushButton(Form)
        self.FilledPushButton.setObjectName(u"FilledPushButton")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/materialIcons/icons8_broom.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.FilledPushButton.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.FilledPushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u6253\u5305\u53c2\u6570", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5728\u8fd9\u91cc\u53ef\u4ee5\u83b7\u53d6Nuitka\u5f53\u524d\u7684\u53c2\u6570</p><p>\u6216\u8005\u4f60\u53ef\u4ee5\u5728\u8fd9\u91cc\u8f93\u5165\u5176\u4ed6\u4eba\u7684\u53c2\u6570,NuitkaGUI\u5c06\u8f6c\u6362\u5230\u754c\u9762\u4e0a</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.TextEdit.setToolTip(QCoreApplication.translate("Form", u"\u590d\u5236\u8fd9\u91cc\u7684\u4ee3\u7801\u5728\u547d\u4ee4\u884c\u5185\u624b\u52a8\u6267\u884c\u6216\u8005\u5206\u4eab\u7ed9\u522b\u4eba", None))
#endif // QT_CONFIG(tooltip)
        self.TextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Nuitka\u7684\u547d\u4ee4\u5728\u8fd9\u91cc\u8f93\u51fa", None))
#if QT_CONFIG(tooltip)
        self.TextPushButton_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u7ea2\u8272\u7684\u4ee3\u8868\u4e0d\u5728GUI\u7684\u9009\u9879\u5185<br/>\u84dd\u8272\u7684\u8868\u793a\u6210\u529f\u9009\u62e9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TextPushButton_2.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u547d\u4ee4", None))
#if QT_CONFIG(tooltip)
        self.TextEdit_2.setToolTip(QCoreApplication.translate("Form", u"\u5f53\u524d\u4e0d\u652f\u6301\u81ea\u52a8\u5f00\u542f\u63d2\u4ef6\uff0c\u5728\u672a\u6765\u7684\u7248\u672c\u4f1a\u8fdb\u884c\u66f4\u65b0", None))
#endif // QT_CONFIG(tooltip)
        self.TextEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u590d\u5236\u5176\u4ed6\u4eba\u7684Nuitka\u547d\u4ee4\u5230\u8fd9\u91cc,\u7ea2\u8272\u7684\u4ee3\u8868\u4e0d\u5728GUI\u7684\u9009\u9879\u5185,\u84dd\u8272\u7684\u8868\u793a\u6210\u529f\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.TextPushButton.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u7ea2\u8272\u7684\u4ee3\u8868\u4e0d\u5728GUI\u7684\u9009\u9879\u5185<br/>\u84dd\u8272\u7684\u8868\u793a\u6210\u529f\u9009\u62e9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TextPushButton.setText(QCoreApplication.translate("Form", u"\u5206\u6790\u547d\u4ee4", None))
#if QT_CONFIG(tooltip)
        self.FilledPushButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.FilledPushButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u6240\u6709\u53c2\u6570", None))
    # retranslateUi

