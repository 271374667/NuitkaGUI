from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QHBoxLayout, QWidget
from qmaterialwidgets import FluentIcon as FIF
from qmaterialwidgets import MaterialWindow, MessageBox, NavigationItemPosition, SubtitleLabel

from src.view.advanced_view import AdvancedView
from src.view.basic_view import BasicView
from src.view.embed_view import EmbedView
from src.view.output_view import OutputView
from src.view.plugin_view import PluginView
from src.view.settings_view import SettingsView


class Widget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class MainView(MaterialWindow):
    def __init__(self, basic_view: BasicView,
                 advanced_view: AdvancedView,
                 plugins_view: PluginView,
                 embed_view: EmbedView,
                 output_view: OutputView,
                 settings_view: SettingsView):
        super().__init__()

        # create sub interface
        self.basic_view = basic_view
        self.advanced_view = advanced_view
        self.plugins_view = plugins_view
        self.embed_view = embed_view
        self.output_view = output_view
        self.settings_view = settings_view
        self.about_view = Widget('关于', self)

        self.initNavigation()
        self.initWindow()

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

    def initNavigation(self):
        self.addSubInterface(self.basic_view, FIF.HOME, '基础', FIF.HOME_FILL)
        self.addSubInterface(self.advanced_view, FIF.DEVELOPER_TOOLS, '高级')
        self.addSubInterface(self.plugins_view, FIF.APPLICATION, '插件')
        self.addSubInterface(self.embed_view, FIF.ZIP_FOLDER, '嵌入')
        self.addSubInterface(self.output_view, FIF.COMMAND_PROMPT, '参数')

        self.addSubInterface(self.settings_view, FIF.SETTING, '设置',
                             position=NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.about_view, FIF.INFO, '关于', position=NavigationItemPosition.BOTTOM)

        self.navigationInterface.setCurrentItem(self.basic_view.objectName())

    def initWindow(self):
        self.resize(1200, 800)
        self.setWindowIcon(QIcon(':/Icons/materialIcons/software_icon.svg'))
        self.setWindowTitle('NuitkaGUI')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


if __name__ == '__main__':
    app = QApplication([])
    w = MainView(BasicView(), AdvancedView(), PluginView(), EmbedView(), OutputView(), SettingsView())
    options = [('--standalone', '生成独立的可执行文件'), ('--onefile', '生成一个文件'),
            ('--console', '生成一个控制台程序'), ('--noconsole', '生成一个非控制台程序')]

    window = w.plugins_view
    for each in options:
        x = window.add_plugin(each[0], each[1])
        x.plugin_changed.connect(lambda x, y: print(x, y))
    w.show()
    app.exec()
