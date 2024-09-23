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
from src.common.nuitka_command.command_implement import command_flag
from typing import Type


class ManagerFlag(ManagerBase):
    gourp_name: str = "开关标志"
    layout_weight: int = 3
    command_type: Type[CommandFlagBase] = CommandFlagBase
    _command_list: list[CommandFlagBase] = []
    mutually_exclusive_group: list[list[Type[CommandFlagBase]]] = [
        [command_flag.CommandClang, command_flag.CommandMingw64],
    ]

    def create_widget(self) -> QWidget:
        command_list = [command for command in self._command_list if command.visible]

        groupBox = QGroupBox(self.gourp_name)
        groupBox.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        groupBox.setTitle(self.gourp_name)
        layout = QGridLayout(groupBox)

        column_count = 3
        for i, command in enumerate(command_list):
            row = i // column_count
            column = i % column_count
            bind_widget = command.create_widget()
            if bind_widget is not None:
                layout.addWidget(bind_widget, row, column)
                bind_widget.checkStateChanged.connect(
                    lambda x, cmd=command: self._check_mutually_exclusive_group(cmd)
                )
        return groupBox

    def update_widget(self):
        for command in self._command_list:
            command.update_widget()

    def _check_mutually_exclusive_group(self, command_flag: CommandFlagBase):
        # 如果当前命令被选中，则将同一组互斥组中的命令全部设置为False,同时将他们设置为不可用
        # 如果当前命令未被选中，则将同一互斥组中的命令设置为可用
        print(command_flag)
        print(command_flag.value)
        if command_flag.value:
            for group in self.mutually_exclusive_group:
                if type(command_flag) not in group:
                    continue
                
                for command in group:
                    if command != type(command_flag):
                        print(command)
                        command().value = False
                        command().update_widget()
        else:
            for group in self.mutually_exclusive_group:
                if type(command_flag) not in group:
                    continue
                
                for command in group:
                    if command != type(command_flag):
                        command().update_widget()

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
