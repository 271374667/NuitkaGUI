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

    def update_all_widget(self):
        for manager in self.manager_list:
            manager.update_widget()
