from PySide6.QtWidgets import QVBoxLayout, QApplication, QSizePolicy, QLayout, QWidget
from qfluentwidgets import ToolTipFilter
from qfluentwidgets.components import SmoothScrollArea

from src.common.nuitka_command.command_manager import CommandManager
from src.view.message_base_view import MessageBaseView


class AdvancedView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self._command_manager = CommandManager()

        self._init_ui()

        self.initialize()

    def _init_ui(self):
        self.setWindowTitle("高级设置")
        self.setObjectName("advanced_view")

        self._main_layout = QVBoxLayout()
        self._main_layout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self._main_scroll_area = SmoothScrollArea()
        self._main_scroll_area.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        self._scroll_content = QWidget()
        self._main_scroll_area_layout = QVBoxLayout(self._scroll_content)
        self._scroll_content.setLayout(self._main_scroll_area_layout)
        self._main_scroll_area.setWidget(self._scroll_content)
        self._main_scroll_area.setWidgetResizable(True)
        self._main_scroll_area.setObjectName("main_scroll_area")

        for each in self._command_manager.manager_list:
            if not each.visible:
                continue

            group_widget = each.create_widget()
            if each.layout_weight and each.layout_weight == 0:
                self._main_scroll_area_layout.addWidget(group_widget)
            else:
                self._main_scroll_area_layout.addWidget(
                    group_widget, each.layout_weight
                )

        self._main_layout.addWidget(self._main_scroll_area)
        self.setLayout(self._main_layout)

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    view = AdvancedView()
    view.show()
    app.exec()
