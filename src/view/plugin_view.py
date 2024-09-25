from PySide6.QtCore import Qt, Signal, QEasingCurve
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from qfluentwidgets import (FlyoutViewBase, ListWidget, FlowLayout, SimpleCardWidget)
from qfluentwidgets.components import TitleLabel, BodyLabel, SwitchButton, PrimaryPushButton, PushButton, \
    SubtitleLabel

from src.interface.Ui_plugin_page_fluent import Ui_Form
from src.view.message_base_view import MessageBaseView


class CustomFlyoutView(FlyoutViewBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = SubtitleLabel()
        self.label.setText('下面为当前启用的插件')
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


class PluginItem(QWidget):
    # 返回值为(插件名，是否选中)
    card_clicked = Signal(str, bool)

    def __init__(self, title: str, desc: str):
        super().__init__()
        self.setObjectName(title)
        self.setMaximumHeight(300)

        self.card_widget: SimpleCardWidget = SimpleCardWidget()
        self.card_layout = QHBoxLayout()
        self.card_widget.setLayout(self.card_layout)

        self.title_lb: TitleLabel = TitleLabel()
        self.title_lb.setText(title)
        self.title_lb.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.title_lb.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.desc_lb: BodyLabel = BodyLabel()
        self.desc_lb.setText(desc)
        self.desc_lb.setWordWrap(True)
        self.desc_lb.setTextColor(QColor(90, 90, 90))
        self.desc_lb.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.desc_lb.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self._desc_layout = QVBoxLayout()
        self._desc_layout.addWidget(self.title_lb)
        self._desc_layout.addWidget(self.desc_lb)

        self.switch_button: SwitchButton = SwitchButton()
        self.switch_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.switch_button.setMaximumWidth(90)
        self.switch_button.checkedChanged.connect(lambda: self.card_clicked.emit(self.title, self.checked))
        self.card_layout.addLayout(self._desc_layout)
        self.card_layout.addWidget(self.switch_button)

        self._main_layout = QHBoxLayout()
        self._main_layout.addWidget(self.card_widget)
        self.setLayout(self._main_layout)

    @property
    def title(self) -> str:
        return self.title_lb.text()

    @property
    def desc(self) -> str:
        return self.desc_lb.text()

    @property
    def checked(self) -> bool:
        return self.switch_button.isChecked()

    @checked.setter
    def checked(self, status: bool) -> None:
        self.switch_button.setChecked(status)


class PluginView(MessageBaseView):
    # 返回值为(插件名，是否选中)
    card_clicked = Signal(str, bool)

    def __init__(self):
        super().__init__()
        self.setObjectName('PluginView')
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.fly_widget = CustomFlyoutView()

        content_widget = self.ui.widget
        self.content_flowlayout = FlowLayout(content_widget, needAni=True, isTight=True)
        self.content_flowlayout.setAnimation(1000, QEasingCurve.InOutCubic)
        content_widget.setLayout(self.content_flowlayout)

    def get_flyout(self) -> CustomFlyoutView:
        return self.fly_widget

    def get_content_widget(self) -> QWidget:
        return self.ui.widget

    def get_auto_btn(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton

    def get_selected_btn(self) -> PushButton:
        return self.ui.PushButton

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
        plugin.checked = status

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
        for each in self._get_all_plugin_items_from_layout(self.content_flowlayout):
            each.checked = True

    def disable_all_plugin(self) -> None:
        """禁用所有插件"""
        for each in self._get_all_plugin_items_from_layout(self.content_flowlayout):
            each.checked = False

    def add_plugin(self, title: str, desc: str):
        """添加一个插件"""
        plugin_item = PluginItem(title, desc)
        self.content_flowlayout.addWidget(plugin_item)
        plugin_item.card_clicked.connect(lambda name, is_selected: self.card_clicked.emit(name, is_selected))
        return plugin_item

    def clear_all_plugin(self) -> None:
        self.content_flowlayout.removeAllWidgets()

    def _get_all_plugin_items_from_layout(self, layout):
        plugin_items = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if isinstance(widget, PluginItem):
                plugin_items.append(widget)
        return plugin_items


if __name__ == '__main__':
    app = QApplication([])
    window = PluginItem('--standalone', '生成独立的可执行文件')
    window.card_clicked.connect(lambda x, y: print(x, y))
    window.show()

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

    # flyout = CustomFlyoutView()
    # flyout.add_plugins(['--standalone', '--onefile', '--console', '--noconsole', '--windowed', '--icon', '--name', ])
    # flyout.show()
    app.exec()
