from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget
from src.utils.plugin_register import PluginRegister
from src.core.paths import COMMAND_IMPLEMENT_DIR

from src.common.nuitka_command.command import CommandBase
from typing import Type


class ManagerBase(ABC):
    gourp_name: str = ""  # 管理器对应的组名(会显示在UI上)
    command_type: Type[CommandBase] = CommandBase  # 管理器对应的命令类型
    _command_list: list[CommandBase] = []  # 管理器对应的命令列表

    def __init__(self):
        self._command_list = PluginRegister.load_plugins(
            COMMAND_IMPLEMENT_DIR, self.command_type
        )
        self._command_list = [
            command for command in self._command_list if command.visible
        ]

    @property
    def command_list(self) -> list[CommandBase]:
        return self._command_list

    @command_list.setter
    def command_list(self, command_list: list[CommandBase]):
        self._command_list = command_list

    @property
    def enabled_command_list(self) -> list[CommandBase]:
        return [command for command in self._command_list if command.enabled]

    def update_widget(self):
        """用于更新管理器对应的UI组件"""
        for command in self._command_list:
            command.update_widget()

    @abstractmethod
    def create_widget(self) -> QWidget:
        """用于创建管理器对应的UI组件"""
        raise NotImplementedError("create_widget method must be implemented")
