from src.common.nuitka_command.command import CommandBase
from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command_implement.command_flag import (
    CommandMingw64,
    CommandClang,
)
from typing import Type


class CommandMiddleware:
    # 定义互斥命令组, 每个列表中的命令互相排斥
    mutually_exclusive_commands: list[list[Type[CommandBase]]] = [
        [CommandMingw64, CommandClang]
    ]

    manager_list: list[ManagerBase] = []
    command_list: list[CommandBase] = []

    def __init__(self):
        for manager in self.manager_list:
            self.command_list.extend(manager.command_list)

    def command_changed(self, command: CommandBase):
        """命令被传递后，检查是否互斥命令，并更新UI"""
        for exclusive_group in self.mutually_exclusive_commands:
            if type(command) in exclusive_group and command.enabled:
                for each_command in exclusive_group:
                    # 将exclusive_group中除了command之外的command的enabled设置为False
                    if each_command != command:
                        each_command.enabled = False
                break
            elif type(command) in exclusive_group and not command.enabled:
                for each_command in exclusive_group:
                    if each_command != command:
                        each_command.enabled = True
                break

        self.update_all_widget()

    def update_all_widget(self):
        for manager in self.manager_list:
            manager.update_widget()
