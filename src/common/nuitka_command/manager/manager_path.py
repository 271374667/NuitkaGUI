from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command import CommandPathBase
from typing import Type


class ManagerPath(ManagerBase):
    gourp_name: str = "路径"
    visible: bool = False
    command_type: Type[CommandPathBase] = CommandPathBase
    _command_list: list[CommandPathBase] = []

    def create_widget(self): ...

    def update_widget(self): ...


if __name__ == "__main__":
    manager = ManagerPath()
    od = manager.get_command_by_command('output-dir')
    od.value = 'C:/Users'
    print(od.value)
    print(manager.command_list)
