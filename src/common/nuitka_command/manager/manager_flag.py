from PySide6.QtWidgets import (
    QVBoxLayout,
    QGroupBox,
    QWidget,
    QGridLayout,
    QMainWindow,
    QApplication,
    QSizePolicy,
)

from src.common.nuitka_command.command import CommandFlagBase
from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.utils.plugin_register import PluginRegister
from src.core.paths import COMMAND_IMPLEMENT_DIR


class ManagerFlag(ManagerBase):
    gourp_name: str = "标志"
    _command_list: list[CommandFlagBase] = []

    def __init__(self):
        self._command_list = PluginRegister.load_plugins(
            COMMAND_IMPLEMENT_DIR, CommandFlagBase
        )

    def create_widget(self) -> QWidget:
        groupBox = QGroupBox(self.gourp_name)
        groupBox.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        groupBox.setTitle(self.gourp_name)
        layout = QGridLayout(groupBox)

        column_count = 3
        for i, command in enumerate(self._command_list):
            row = i // column_count
            column = i % column_count
            layout.addWidget(command.create_widget(), row, column)
        return groupBox

    def update_widget(self):
        for command in self._command_list:
            command.update_widget()


if __name__ == "__main__":

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ManagerFlag Preview")
            self.setGeometry(100, 100, 800, 600)

            main_widget = QWidget()
            layout = QVBoxLayout(main_widget)

            manager_flag = ManagerFlag()
            widget = manager_flag.create_widget()
            layout.addWidget(widget)

            self.setCentralWidget(main_widget)

    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
