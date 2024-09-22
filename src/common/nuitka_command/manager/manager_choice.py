from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command import CommandChoiceBase
from typing import Type
from PySide6.QtWidgets import QGroupBox, QSizePolicy, QWidget, QVBoxLayout, QGridLayout


class ManagerChoice(ManagerBase):
    gourp_name: str = "选择"
    command_type: Type[CommandChoiceBase] = CommandChoiceBase
    _command_list: list[CommandChoiceBase] = []

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


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ManagerChoice Preview")
            self.setGeometry(100, 100, 800, 600)

            main_widget = QWidget()
            layout = QVBoxLayout(main_widget)

            manager_choice = ManagerChoice()
            widget = manager_choice.create_widget()
            layout.addWidget(widget)

            self.setCentralWidget(main_widget)

    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
