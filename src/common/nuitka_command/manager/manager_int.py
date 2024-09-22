from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command import CommandIntBase
from typing import Type
from PySide6.QtWidgets import QGroupBox, QSizePolicy, QGridLayout, QWidget


class ManagerInt(ManagerBase):
    gourp_name: str = "整数"
    layout_weight: int = 1
    command_type: Type[CommandIntBase] = CommandIntBase
    _command_list: list[CommandIntBase] = []

    def create_widget(self) -> QWidget:
        command_list = [command for command in self._command_list if command.visible]
        groupBox = QGroupBox(self.gourp_name)
        groupBox.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        groupBox.setTitle(self.gourp_name)
        layout = QGridLayout(groupBox)

        column_count = 2
        for i, command in enumerate(command_list):
            row = i // column_count
            column = i % column_count
            layout.addWidget(command.create_widget(), row, column)
        return groupBox

    def update_widget(self):
        for command in self._command_list:
            command.update_widget()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ManagerFlag Preview")
            self.setGeometry(100, 100, 800, 600)

            main_widget = QWidget()
            layout = QVBoxLayout(main_widget)

            manager_int = ManagerInt()
            widget = manager_int.create_widget()
            layout.addWidget(widget)

            self.setCentralWidget(main_widget)

    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
