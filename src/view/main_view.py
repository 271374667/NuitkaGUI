from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qmaterialwidgets import FluentIcon as FIF, InfoBar
from qmaterialwidgets import MaterialWindow, NavigationItemPosition

from src.view.about_view import AboutView
from src.view.advanced_view import AdvancedView
from src.view.basic_view import BasicView
from src.view.embed_view import EmbedView
from src.view.output_view import OutputView
from src.view.plugin_view import PluginView
from src.view.settings_view import SettingsView


class MainView(MaterialWindow):
    def __init__(self, basic_view: BasicView,
                 advanced_view: AdvancedView,
                 plugins_view: PluginView,
                 embed_view: EmbedView,
                 output_view: OutputView,
                 settings_view: SettingsView,
                 about_view: AboutView):
        super().__init__()

        # create sub interface
        self.basic_view = basic_view
        self.advanced_view = advanced_view
        self.plugins_view = plugins_view
        self.embed_view = embed_view
        self.output_view = output_view
        self.settings_view = settings_view
        self.about_view = about_view

        self.initNavigation()
        self.initWindow()

    def show_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.info(title, content, parent=self, duration=duration)

    def show_warning_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.warning(title, content, parent=self, duration=duration)

    def show_success_info(self, title: str, content: str, duration: int = 15000) -> None:
        InfoBar.success(title, content, parent=self, duration=duration)

    def show_error_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.error(title, content, parent=self, duration=duration)

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
    w.show_pythonexe_error_message()
    app.exec()
