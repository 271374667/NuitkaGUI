from src.common.nuitka_command.manager.manager_base import ManagerBase


class CommandGroupManager:
    def __init__(self):
        self._command_group_list: list[ManagerBase] = []

    def add_command_group(self, command_group: ManagerBase):
        self._command_group_list.append(command_group)

    def get_command_group(self, name: str) -> ManagerBase: ...
