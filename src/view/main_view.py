# coding:utf-8
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout
from qmaterialwidgets import FluentIcon as FIF
from qmaterialwidgets import MaterialWindow, MessageBox, NavigationItemPosition, SubtitleLabel, setFont

from src.view.basic_view import BasicView


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class MainView(MaterialWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = BasicView()
        self.appInterface = Widget('Application Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.libraryInterface = Widget('library Interface', self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '基础', FIF.HOME_FILL)
        self.addSubInterface(self.appInterface, FIF.APPLICATION, '进阶')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, '插件')

        self.addSubInterface(self.libraryInterface, FIF.BOOK_SHELF, '库', FIF.LIBRARY_FILL,
                             NavigationItemPosition.BOTTOM)
        self.navigationInterface.addItem(
                routeKey='Help',
                icon=FIF.HELP,
                text='帮助',
                onClick=self.showMessageBox,
                selectable=False,
                position=NavigationItemPosition.BOTTOM,
                )

        self.navigationInterface.setCurrentItem(self.homeInterface.objectName())

    def initWindow(self):
        self.resize(1000, 650)
        self.setWindowIcon(QIcon(':/Icons/materialIcons/software_icon.svg'))
        self.setWindowTitle('NuitkaGUI')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def showMessageBox(self):
        w = MessageBox(
                '支持作者🥰',
                '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
                self
                )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))


if __name__ == '__main__':
    app = QApplication([])
    w = MainView()
    w.show()
    app.exec()
