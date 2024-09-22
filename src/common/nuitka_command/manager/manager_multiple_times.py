from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.command import CommandMultipleTimesBase
from typing import Type


class ManagerMultipleTimes(ManagerBase):
    gourp_name: str = "多次"
    visible: bool = False
    command_type: Type[CommandMultipleTimesBase] = CommandMultipleTimesBase
    _command_list: list[CommandMultipleTimesBase] = []

    def create_widget(self): ...

    def update_widget(self): ...


if __name__ == "__main__":
    manager = ManagerMultipleTimes()
    print(manager.command_list)
