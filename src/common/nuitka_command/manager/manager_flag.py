from typing import Optional, Type

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
from src.common.nuitka_command.command_implement import command_flag
from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.utils.class_utils import ClassUtils


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

        group_box = QGroupBox(self.gourp_name)
        group_box.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        group_box.setTitle(self.gourp_name)
        layout = QGridLayout(group_box)

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
        return group_box

    def update_widget(self):
        for command in self._command_list:
            command.update_widget()

    def _check_mutually_exclusive_group(self, command_flag: CommandFlagBase):
        # 如果当前命令被选中，则将同一组互斥组中的命令全部设置为False,同时将他们设置为不可用
        # 如果当前命令未被选中，则将同一互斥组中的命令设置为可用
        command_flag.update_value()  # 记得更新一下值(因为这个bug导致项目进度卡了很久)

        for group in self.mutually_exclusive_group:
            if not any(command.__name__ == type(command_flag).__name__ for command in group):
                continue

            for command in group:
                if command.__name__ != type(command_flag).__name__:
                    instance: Optional[CommandFlagBase] = ClassUtils.get_obj_in_list_by_type(command, self.command_list)
                    if instance is None:
                        continue
                    if command_flag.value is True:
                        instance.value = False
                        instance.enabled = False
                    else:
                        instance.enabled = True
                    instance.update_widget()


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
