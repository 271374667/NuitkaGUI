from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, NavigationItemPosition

from src.component.cmd_text_edit import CMDTextEdit
from src.view.about_view import AboutView
from src.view.advanced_view import AdvancedView
from src.view.args_view import ArgsView
from src.view.basic_view import BasicView
from src.view.embed_view import EmbedView
from src.view.plugin_view import PluginView
from src.view.setting_view import SettingView


class MainView(FluentWindow):
    def __init__(
            self,
            basic_view: BasicView,
            advanced_view: AdvancedView,
            plugin_view: PluginView,
            embed_view: EmbedView,
            args_view: ArgsView,
            about_view: AboutView,
            setting_view: SettingView,
    ):
        super().__init__()
        self.navigationInterface.setAcrylicEnabled(True)
        self.navigationInterface.panel.expandWidth = 150

        # create sub interface
        self.basic_interface = basic_view
        self.embed_interface = embed_view
        self.advanced_interface = advanced_view
        self.plugin_interface = plugin_view
        self.args_interface = args_view
        self.about_interface = about_view
        self.setting_interface = setting_view
        self.cmd_interface = CMDTextEdit()

        self.about_interface.setObjectName("about")
        self.cmd_interface.setObjectName("cmd")
        self.plugin_interface.setObjectName("plugin")
        self.args_interface.setObjectName("args")
        # self.setting_interface = setting_view

        self._init_navigation()
        self._init_window()

    def _init_navigation(self):
        self.addSubInterface(self.basic_interface, FIF.HOME, "主页")
        self.addSubInterface(self.advanced_interface, FIF.DEVELOPER_TOOLS, "高级")
        self.addSubInterface(self.embed_interface, FIF.ZIP_FOLDER, "嵌入")
        self.addSubInterface(self.plugin_interface, FIF.DEVELOPER_TOOLS, "插件")
        self.addSubInterface(self.args_interface, FIF.EDIT, "参数")
        self.addSubInterface(self.cmd_interface, FIF.COMMAND_PROMPT, "日志")

        self.addSubInterface(
            self.about_interface, FIF.CHAT, "关于", NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.setting_interface, FIF.SETTING, "设置", NavigationItemPosition.BOTTOM
        )

    def _init_window(self):
        self.resize(1100, 750)
        # 设置窗口的最小尺寸
        self.setMinimumSize(1100, 750)
        self.setWindowIcon(QIcon(":/Icons/materialIcons/software_icon.svg"))
        self.setWindowTitle("NuitkaGUI")

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


if __name__ == "__main__":
    app = QApplication([])
    w = MainView(
        BasicView(), AdvancedView(), PluginView(), EmbedView(), ArgsView(), AboutView(), SettingView()
    )
    w.show()
    app.exec()
