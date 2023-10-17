from typing import Callable

from PySide6.QtCore import QEasingCurve, Signal
from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QWidget
from qmaterialwidgets import (FilledPushButton, FlowLayout, FlyoutViewBase, InfoBar, InfoBarPosition,
                              ListWidget,
                              TonalPushButton, ToolTipFilter)
from qmaterialwidgets.components import SubtitleLabel

from src.interface.Ui_component_list_item import Ui_Form as Ui_ComponentListItem
from src.interface.Ui_plugin_page import Ui_Form as Ui_PluginPage


class CustomFlyoutView(FlyoutViewBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = SubtitleLabel('下面为当前启用的插件')
        self.list_widget = ListWidget()

        # self.vBoxLayout.setSpacing(12)
        # self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.list_widget)

    def add_plugin(self, plugin: str) -> None:
        self.list_widget.addItem(plugin)

    def add_plugins(self, plugins: list[str]) -> None:
        self.list_widget.addItems(plugins)

    def clear(self) -> None:
        self.list_widget.clear()


class PluginItem(QFrame):
    plugin_changed = Signal(str, bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_ComponentListItem()
        self.ui.setupUi(self)
        self.ui.SwitchButton.checkedChanged.connect(lambda x: self.plugin_changed.emit(self.objectName(), x))

    def set_title(self, title: str) -> None:
        """设置插件的标题"""
        self.ui.LBTitle.setText(title)
        self.setObjectName(title)

    def set_info(self, info: str) -> None:
        """设置插件的简介"""
        self.ui.LBinfo.setText(info)

    def set_switch_status(self, status: bool) -> None:
        """设置插件的开关状态"""
        self.ui.SwitchButton.setChecked(status)

    def get_switch_status(self) -> bool:
        """获取插件的开关状态"""
        return self.ui.SwitchButton.isChecked()

    def switch_clicked(self, func: Callable[[str, bool], None]) -> None:
        """插件的开关被点击"""
        # 因为默认只有一个参数bool，所以需要使用 lambda 表达式来传递一个额外参数参数
        self.ui.SwitchButton.checkedChanged.connect(lambda x: func(self.objectName(), x))


class PluginView(QWidget):
    plugin_changed = Signal(str, bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_PluginPage()
        self.ui.setupUi(self)

        self.fly_widget = CustomFlyoutView()

        content_widget = self.get_content_widget()
        self.content_flowlayout = FlowLayout(content_widget, needAni=True, isTight=True)
        self.content_flowlayout.setAnimation(1000, QEasingCurve.InOutCubic)
        content_widget.setLayout(self.content_flowlayout)

        self.setObjectName('PluginView')
        self.initialize()

    def get_flyout(self) -> CustomFlyoutView:
        return self.fly_widget

    def get_content_widget(self) -> QWidget:
        return self.ui.widget

    def get_auto_btn(self) -> FilledPushButton:
        return self.ui.FilledPushButton

    def get_selected_btn(self) -> TonalPushButton:
        return self.ui.TonalPushButton

    def get_plugins_length(self) -> int:
        """获取插件的数量"""
        number = 0
        for each in self.content_flowlayout.children():
            if isinstance(each, PluginItem):
                number += 1
        return number

    # noinspection PyTypeChecker
    def set_plugin_status(self, plugin_name: str, status: bool) -> None:
        """设置插件的开关状态"""
        plugin: PluginItem = self.findChild(PluginItem, plugin_name)
        if plugin is None:
            return
        plugin.set_switch_status(status)

    def enable_plugins(self, plugins: list[str]) -> None:
        """启用插件"""
        for plugin in plugins:
            self.set_plugin_status(plugin, True)

    def disable_plugins(self, plugins: list[str]) -> None:
        """禁用插件"""
        for plugin in plugins:
            self.set_plugin_status(plugin, False)

    def enable_all_plugin(self) -> None:
        """启用所有插件"""
        for each in self.content_flowlayout.children():
            if isinstance(each, PluginItem):
                each.set_switch_status(True)

    def disable_all_plugin(self) -> None:
        """禁用所有插件"""
        for each in self.content_flowlayout.children():
            if isinstance(each, PluginItem):
                each.set_switch_status(False)

    def add_plugin(self, title: str, desc: str) -> PluginItem:
        """添加一个插件"""
        plugin_item = PluginItem()
        plugin_item.set_title(title)
        plugin_item.set_info(desc)
        self.content_flowlayout.addWidget(plugin_item)
        return plugin_item

    def clear_all_plugin(self) -> None:
        self.content_flowlayout.removeAllWidgets()

    def show_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.info(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def show_warning_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.warning(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def show_success_info(self, title: str, content: str, duration: int = 15000) -> None:
        InfoBar.success(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def show_error_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.error(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def initialize(self) -> None:
        # 找到界面内所有的控件,然后对他们installEventFilter
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == '__main__':
    app = QApplication([])
    # window = PluginItem()
    # window.set_title('--standalone')
    # window.switch_clicked(lambda x, y: print(x, y))
    # window.show()

    # options = [('--standalone', '生成独立的可执行文件'), ('--onefile', '生成一个文件'),
    #         ('--console', '生成一个控制台程序'), ('--noconsole', '生成一个非控制台程序')]
    #
    # window = PluginView()
    # for each in options:
    #     x = window.add_plugin(each[0], each[1])
    #     x.plugin_changed.connect(lambda x, y: print(x, y))
    #
    # window.set_plugin_status('--standalone', True)
    #
    # window.show()

    flyout = CustomFlyoutView()
    flyout.add_plugins(['--standalone', '--onefile', '--console', '--noconsole', '--windowed', '--icon', '--name', ])
    flyout.show()
    app.exec()
