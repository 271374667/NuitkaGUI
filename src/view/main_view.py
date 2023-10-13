from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QHBoxLayout, QWidget
from qmaterialwidgets import FluentIcon as FIF
from qmaterialwidgets import MaterialWindow, MessageBox, NavigationItemPosition, SubtitleLabel

from src.view.basic_view import BasicView
from src.view.plugin_view import PluginView


class Widget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class MainView(MaterialWindow):
    def __init__(self):
        super().__init__()

        # create sub interface
        self.basic_interface = BasicView()
        self.app_interface = Widget('基础', self)
        self.plugins_interface = PluginView()
        self.embed_interface = Widget('嵌入式', self)
        self.args_interface = Widget('打包参数', self)
        self.settings_interface = Widget('设置', self)
        self.about_interface = Widget('关于', self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.basic_interface, FIF.HOME, '基础', FIF.HOME_FILL)
        self.addSubInterface(self.app_interface, FIF.DEVELOPER_TOOLS, '高级')
        self.addSubInterface(self.plugins_interface, FIF.APPLICATION, '插件')
        self.addSubInterface(self.embed_interface, FIF.ZIP_FOLDER, '嵌入')
        self.addSubInterface(self.args_interface, FIF.COMMAND_PROMPT, '参数')

        self.addSubInterface(self.settings_interface, FIF.SETTING, '设置',
                             position=NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.about_interface, FIF.INFO, '关于', position=NavigationItemPosition.BOTTOM)
        # self.navigationInterface.addItem(
        #         routeKey='Help',
        #         icon=FIF.HELP,
        #         text='帮助',
        #         onClick=self.showMessageBox,
        #         selectable=False,
        #         position=NavigationItemPosition.BOTTOM,
        #         )

        self.navigationInterface.setCurrentItem(self.basic_interface.objectName())

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
            print('yes')


if __name__ == '__main__':
    app = QApplication([])
    w = MainView()
    options = [('--standalone', '生成独立的可执行文件'), ('--onefile', '生成一个文件'),
            ('--console', '生成一个控制台程序'), ('--noconsole', '生成一个非控制台程序')]

    window = w.plugins_interface
    for each in options:
        x = window.add_plugin(each[0], each[1])
        x.plugin_changed.connect(lambda x, y: print(x, y))
    w.show()
    app.exec()
