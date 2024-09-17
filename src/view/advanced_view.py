from PySide6.QtWidgets import QVBoxLayout, QGridLayout
from src.view.message_base_view import MessageBaseView
from src.common.nuitka_command.command_manager import CommandManager
from qfluentwidgets.components import SmoothScrollArea


class AdvancedView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.col_count: int = 2
        self._count: int = 0

        self._command_manager = CommandManager()

        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("高级设置")
        self.setObjectName("advanced_view")

        self._main_layout = QVBoxLayout()
        self._main_scroll_area = SmoothScrollArea()
        self._main_scroll_area.setWidgetResizable(True)
        self._main_scroll_area.setObjectName("main_scroll_area")

        self._scrool_layout = QGridLayout()

    def _add_one_col_command(self):
        ...