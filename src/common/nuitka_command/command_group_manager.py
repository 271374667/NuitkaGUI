from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command import CommandBase
from typing import Type

class CommandGroupManager(ManagerBase):
    def __init__(self):
        self._command_group_list: list[CommandBase] = []

    def add_command_group(self, command_group: CommandBase):
        self._command_group_list.append(command_group)


    def get_command_group(self, command_type: Type[CommandBase]) -> CommandBase:
        for command in self._command_group_list:
            if isinstance(command, command_type):
                return command
        raise ValueError(f"Command group {command_type} not found")
