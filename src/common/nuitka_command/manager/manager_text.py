from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command import CommandTextBase
from typing import Type
from PySide6.QtWidgets import QGroupBox, QSizePolicy, QWidget, QVBoxLayout


class ManagerText(ManagerBase):
    gourp_name: str = "文本"
    layout_weight: int = 2
    command_type: Type[CommandTextBase] = CommandTextBase
    _command_list: list[CommandTextBase] = []

    def create_widget(self) -> QWidget:
        command_list = [command for command in self._command_list if command.visible]
        groupBox = QGroupBox(self.gourp_name)
        groupBox.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        groupBox.setTitle(self.gourp_name)
        layout = QVBoxLayout(groupBox)

        for command in command_list:
            layout.addWidget(command.create_widget())
        return groupBox


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ManagerText Preview")
            self.setGeometry(100, 100, 800, 600)

            main_widget = QWidget()
            layout = QVBoxLayout(main_widget)

            manager_text = ManagerText()
            widget = manager_text.create_widget()
            layout.addWidget(widget)

            self.setCentralWidget(main_widget)

    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
