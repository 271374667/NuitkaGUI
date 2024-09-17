from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget

from src.common.nuitka_command.command import CommandBase


class ManagerBase(ABC):
    gourp_name: str = ''
    _command_list: list[CommandBase] = []

    @property
    def command_list(self) -> list[CommandBase]:
        return self._command_list

    @command_list.setter
    def command_list(self, command_list: list[CommandBase]):
        self._command_list = command_list

    @property
    def enabled_commands(self) -> list[CommandBase]:
        return [command for command in self._command_list if command.enabled]

    @abstractmethod
    def create_widget(self) -> QWidget:
        raise NotImplementedError("create_widget method must be implemented")
