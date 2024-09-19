from PySide6.QtWidgets import QFrame, QVBoxLayout, QGroupBox, QWidget
from qfluentwidgets import CheckBox

from src.common.nuitka_command.command import CommandFlagBase
from src.common.nuitka_command.manager.manager_base import ManagerBase


class ManagerFlag(ManagerBase):
    gourp_name: str = "标志"
    _command_list: list[CommandFlagBase] = []

    def create_widget(self) -> QWidget:
        groupBox = QGroupBox(self.gourp_name)
        groupBox.setTitle(self.gourp_name)
        layout = QVBoxLayout(groupBox)

        frame = QFrame()
        layout = QVBoxLayout(frame)
        for command in self._command_list:
            checkBox = CheckBox(command.name)
            checkBox.setChecked(command.value)
            layout.addWidget(checkBox)
        groupBox.layout().addWidget(frame)
        return groupBox
