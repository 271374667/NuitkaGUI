from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, NavigationItemPosition

from src.component.cmd_text_edit import CMDTextEdit
from src.view.basic_view import BasicView
from src.view.embed_view import EmbedView
from src.view.about_view import AboutView
from src.view.advanced_view import AdvancedView


class MainView(FluentWindow):
    def __init__(
        self, basic_view: BasicView,advanced_view: AdvancedView, embed_view: EmbedView, about_view: AboutView
    ):
        super().__init__()

        # create sub interface
        self.basic_interface = basic_view
        self.embed_interface = embed_view
        self.advanced_interface = advanced_view
        self.about_interface = about_view
        self.cmd_interface = CMDTextEdit()
        self.about_interface.setObjectName("about")
        # self.setting_interface = setting_view

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.basic_interface, FIF.HOME, "主页")
        self.addSubInterface(self.advanced_interface, FIF.DEVELOPER_TOOLS, "高级")
        self.addSubInterface(self.embed_interface, FIF.ZIP_FOLDER, "嵌入")
        self.addSubInterface(self.cmd_interface, FIF.COMMAND_PROMPT, "日志")

        self.addSubInterface(self.about_interface, FIF.CHAT, '关于', NavigationItemPosition.BOTTOM)
        # self.addSubInterface(self.setting_interface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(1100, 750)
        # 设置窗口的最大尺寸
        self.setMaximumSize(1100, 750)
        # 设置窗口的最小尺寸
        self.setMinimumSize(1100, 750)
        self.setWindowIcon(QIcon(":/Icons/materialIcons/software_icon.svg"))
        self.setWindowTitle("NuitkaGUI")

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


if __name__ == "__main__":
    app = QApplication([])
    w = MainView(BasicView(), AdvancedView(), EmbedView(), AboutView())
    w.show()
    app.exec()
