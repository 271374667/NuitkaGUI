# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plugin_page_fluent.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QColor,
    QIcon,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from qfluentwidgets import (
    BodyLabel,
    ElevatedCardWidget,
    IconWidget,
    PrimaryPushButton,
    PushButton,
    SmoothScrollArea,
    TitleLabel,
)
from src.resource import rc_res

rc_res = rc_res  # 防止格式化的时候资源文件被删除


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(816, 493)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 15, 30, 30)
        self.ElevatedCardWidget = ElevatedCardWidget(Form)
        self.ElevatedCardWidget.setObjectName("ElevatedCardWidget")
        self.horizontalLayout = QHBoxLayout(self.ElevatedCardWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IconWidget = IconWidget(self.ElevatedCardWidget)
        self.IconWidget.setObjectName("IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(50, 50))
        self.IconWidget.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(
            ":/Icons/materialIcons/icons8_info.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.IconWidget.setIcon(icon)

        self.horizontalLayout.addWidget(self.IconWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleLabel = TitleLabel(self.ElevatedCardWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.TitleLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setObjectName("BodyLabel")
        self.BodyLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.BodyLabel)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.PushButton = PushButton(self.ElevatedCardWidget)
        self.PushButton.setObjectName("PushButton")
        self.PushButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_4.addWidget(self.PushButton)

        self.PrimaryPushButton = PrimaryPushButton(self.ElevatedCardWidget)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.PrimaryPushButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_4.addWidget(self.PrimaryPushButton)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3.addWidget(self.ElevatedCardWidget)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName("SmoothScrollArea")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 756, 317))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")

        self.verticalLayout.addWidget(self.widget)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.SmoothScrollArea)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.TitleLabel.setText(
            QCoreApplication.translate("Form", "\u8bf4\u660e", None)
        )
        self.BodyLabel.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>Nuitka\u9700\u8981\u5f00\u542f\u63d2\u4ef6\u6765\u652f\u6301\u7279\u6b8a\u7684\u6a21\u5757\u5de5\u4f5c</p><p>\u60a8\u4e5f\u53ef\u4ee5\u9009\u62e9\u81ea\u52a8\u5206\u6790\u4ee5\u6b64\u6536\u96c6\u9009\u4e2d &quot;.py&quot; \u548c\u9879\u76ee\u76ee\u5f55\u4e0b\u6240\u6709\u7684\u4f9d\u8d56\u5e93</p></body></html>",
                None,
            )
        )
        self.PushButton.setText(
            QCoreApplication.translate("Form", "\u67e5\u770b\u5df2\u9009\u62e9", None)
        )
        # if QT_CONFIG(tooltip)
        self.PrimaryPushButton.setToolTip(
            QCoreApplication.translate(
                "Form",
                "\u8be5\u9009\u9879\u4f1a\u81ea\u52a8\u5206\u6790\u9879\u76ee\u76ee\u5f55\u4e0b\u53ef\u4ee5\u5f00\u542f\u7684\u63d2\u4ef6",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.PrimaryPushButton.setText(
            QCoreApplication.translate("Form", "\u81ea\u52a8\u5206\u6790", None)
        )

    # retranslateUi
