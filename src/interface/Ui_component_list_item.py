# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'component_list_item.ui'
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

from qmaterialwidgets import (BodyLabel, CardWidget, SwitchButton, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(696, 139)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.LBTitle = TitleLabel(self.CardWidget)
        self.LBTitle.setObjectName(u"LBTitle")
        self.LBTitle.setTextFormat(Qt.PlainText)
        self.LBTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.LBTitle)

        self.LBinfo = BodyLabel(self.CardWidget)
        self.LBinfo.setObjectName(u"LBinfo")
        self.LBinfo.setTextFormat(Qt.PlainText)
        self.LBinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.LBinfo.setWordWrap(True)
        self.LBinfo.setProperty("lightColor", QColor(96, 96, 96))
        self.LBinfo.setProperty("darkColor", QColor(210, 210, 210))

        self.verticalLayout_2.addWidget(self.LBinfo)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.SwitchButton = SwitchButton(self.CardWidget)
        self.SwitchButton.setObjectName(u"SwitchButton")
        self.SwitchButton.setMaximumSize(QSize(90, 24))
        self.SwitchButton.setChecked(False)

        self.horizontalLayout.addWidget(self.SwitchButton)


        self.verticalLayout.addWidget(self.CardWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LBTitle.setText(QCoreApplication.translate("Form", u"\u63d2\u4ef6\u540d\u79f0", None))
        self.LBinfo.setText(QCoreApplication.translate("Form", u"\u63d2\u4ef6\u8bf4\u660e", None))
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
    # retranslateUi

