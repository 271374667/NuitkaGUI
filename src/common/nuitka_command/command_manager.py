from pathlib import Path
from typing import Optional

from src.common.nuitka_command import command
from src.common.nuitka_command.manager.manager_choice import ManagerChoice
from src.common.nuitka_command.manager.manager_int import ManagerInt
from src.common.nuitka_command.manager.manager_text import ManagerText
from src.common.nuitka_command.manager.manager_flag import ManagerFlag
from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.manager.manager_plugin import ManagerPlugin
from src.common.nuitka_command.command_implement import command_flag, command_path
from src.utils.singleton import singleton
from typing import Type, TypeVar

CommandBaseType = TypeVar("CommandBaseType", bound=command.CommandBase)


@singleton
class CommandManager:
    def __init__(self):
        self.command_list: list[command.CommandBase] = []

        self.manager_list: list[ManagerBase] = [
            ManagerChoice(),
            ManagerInt(),
            ManagerText(),
            ManagerFlag(),
        ]

        self.manager_plugin = ManagerPlugin()

        self.update_command_list()

    @property
    def source_script(self) -> Optional[Path]:
        result = self.get_command_by_type(command_path.CommandMain)
        if result is None:
            return None
        return Path(result.value)

    @source_script.setter
    def source_script(self, source_script: Optional[Path]) -> None:
        result = self.get_command_by_type(command_path.CommandMain)
        if result is None:
            return
        result.value = str(source_script)

    def update_command_list(self):
        self.command_list = []
        for manager in self.manager_list:
            self.command_list.extend(manager.command_list)

    def update_widget(self):
        for manager in self.manager_list:
            manager.update_widget()

    def get_command_by_type(
        self, command_type: Type[command.CommandBase]
    ) -> Optional[command.CommandBase]:
        for each in self.command_list:
            print(type(each), command_type)
            if (
                each.__class__.__name__ == command_type.__name__
                and each.__class__.__module__.split(".")[-1]
                == command_type.__module__.split(".")[-1]
            ):
                return each
        return None

    def get_command_by_name(self, command_name: str) -> Optional[command.CommandBase]:
        for each in self.command_list:
            if each.name == command_name:
                return each
        return None

    def get_command_by_command(self, command: str) -> Optional[command.CommandBase]:
        for each in self.command_list:
            if each.command == command:
                return each
        return None


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    manager = CommandManager()
    print(manager.command_list)
    print(manager.get_command_by_type(command_flag.CommandClang))
    print(manager.get_command_by_name("公司名称"))
    print(manager.get_command_by_command("clang"))
    app.exec()
