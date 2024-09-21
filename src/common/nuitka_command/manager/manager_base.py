from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget

from src.common.nuitka_command.command import CommandBase


class ManagerBase(ABC):
    gourp_name: str = ""  # 管理器对应的组名(会显示在UI上)
    _command_list: list[CommandBase] = []  # 管理器对应的命令列表

    @property
    def command_list(self) -> list[CommandBase]:
        return self._command_list

    @command_list.setter
    def command_list(self, command_list: list[CommandBase]):
        self._command_list = command_list

    @property
    def enabled_command_list(self) -> list[CommandBase]:
        return [command for command in self._command_list if command.enabled]

    @abstractmethod
    def create_widget(self) -> QWidget:
        """用于创建管理器对应的UI组件"""
        raise NotImplementedError("create_widget method must be implemented")
    
    @abstractmethod
    def update_widget(self):
        """用于更新管理器对应的UI组件"""
        raise NotImplementedError("update_widget method must be implemented")
