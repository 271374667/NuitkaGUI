from pathlib import Path
from typing import Optional
from typing import Type, TypeVar

from src.common.nuitka_command import command
from src.common.nuitka_command.command_implement import command_flag, command_path
from src.common.nuitka_command.manager.manager_base import ManagerBase
from src.common.nuitka_command.manager.manager_choice import ManagerChoice
from src.common.nuitka_command.manager.manager_flag import ManagerFlag
from src.common.nuitka_command.manager.manager_int import ManagerInt
from src.common.nuitka_command.manager.manager_multiple_times import (
    ManagerMultipleTimes,
)
from src.common.nuitka_command.manager.manager_path import ManagerPath
from src.common.nuitka_command.manager.manager_plugin import ManagerPlugin
from src.common.nuitka_command.manager.manager_text import ManagerText
from src.config import cfg
from src.utils.class_utils import ClassUtils
from src.utils.singleton import singleton

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
            ManagerPath(),
            ManagerMultipleTimes(),
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

    @property
    def current_command(self) -> str:
        project_python_exe_path: Path = Path(cfg.get(cfg.project_python_exe_path))
        if not project_python_exe_path.exists():
            project_python_exe_path = Path(cfg.get(cfg.global_python_exe_path))
        if not project_python_exe_path.exists():
            raise ValueError("Must have a avialable python exe(project or gloabl)")

        result: list[str] = [f'"{project_python_exe_path}"', '-m', 'nuitka']
        for i in self.command_list:
            if i.enabled and i.value != "" and i.value is not None and i.value is not False and i.value != -1:
                result.append(i.get_command())
        return ",".join(result)

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
        """通过类型获取命令"""
        for each in self.command_list:
            if ClassUtils.is_the_same_class(each.__class__, command_type):
                return each
        return None

    def get_command_by_name(self, command_name: str) -> Optional[command.CommandBase]:
        """通过名称获取命令"""
        for each in self.command_list:
            if each.name == command_name:
                return each
        return None

    def get_command_by_command(self, command: str) -> Optional[command.CommandBase]:
        """通过命令获取命令"""
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
    print(manager.get_command_by_command("include-data-dir"))
    print(manager.current_command)
    app.exec()
