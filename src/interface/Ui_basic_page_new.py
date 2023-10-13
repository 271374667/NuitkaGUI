# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_page_new.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qmaterialwidgets import (FilledPushButton, LargeTitleLabel, OpacityAniStackedWidget, StrongBodyLabel)
from src.resource import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 494)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OpacityAniStackedWidget = OpacityAniStackedWidget(Form)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.LargeTitleLabel = LargeTitleLabel(self.page)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LargeTitleLabel.sizePolicy().hasHeightForWidth())
        self.LargeTitleLabel.setSizePolicy(sizePolicy)
        self.LargeTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.LargeTitleLabel)

        self.StrongBodyLabel = StrongBodyLabel(self.page)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setAlignment(Qt.AlignCenter)
        self.StrongBodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.StrongBodyLabel)

        self.FilledPushButton = FilledPushButton(self.page)
        self.FilledPushButton.setObjectName(u"FilledPushButton")

        self.verticalLayout_2.addWidget(self.FilledPushButton)

        self.OpacityAniStackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u4e00\u5207\u7684\u5f00\u59cb", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u4e00\u4e2a\u53ef\u4ee5\u8fd0\u884c\u7684\u9879\u76ee\u5165\u53e3\u6587\u4ef6\n"
"\u4e00\u822c\u6307 if __name__ == \"__main__\" \u6240\u5728\u76ee\u5f55", None))
        self.FilledPushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4e00\u4e2a .py \u6587\u4ef6", None))
    # retranslateUi

