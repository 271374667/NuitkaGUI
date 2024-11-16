import re
from pathlib import Path
from typing import Generic
from typing import Optional
from typing import Type, TypeVar

import loguru

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
from src.signal_bus import SignalBus
from src.utils.class_utils import ClassUtils
from src.utils.singleton import singleton

CommandBaseType = TypeVar("CommandBaseType", bound=command.CommandBase)


@singleton
class CommandManager(Generic[CommandBaseType]):
    def __init__(self):
        self.command_list: list[command.CommandBase] = []
        self._extra_command_list: list[str] = []

        self.manager_list: list[ManagerBase] = [
            ManagerChoice(),
            ManagerInt(),
            ManagerFlag(),
            ManagerPath(),
            ManagerText(),
            ManagerMultipleTimes(),
        ]

        self.manager_plugin = ManagerPlugin()
        self._signal_bus = SignalBus()

        self.update_command_list()

    @property
    def source_script(self) -> Optional[Path]:
        result = self.get_command_by_type(command_path.CommandMain)
        if result is None or result.value is None:
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
        project_python_exe_path: Path = self.python_exe_path

        result: list[str] = [f'"{project_python_exe_path}"', '-m', 'nuitka']
        for i in self.command_list:
            if i.enabled and i.value != "" and i.value is not None and i.value is not False and i.value != -1:
                result.append(i.get_command())
        result.extend(self._extra_command_list)
        return " ".join(result)

    @property
    def python_exe_path(self) -> Path:
        project_python_exe_path: Path = Path(cfg.get(cfg.project_python_exe_path))
        if not project_python_exe_path.exists():
            project_python_exe_path = Path(cfg.get(cfg.global_python_exe_path))
        if not project_python_exe_path.exists():
            raise ValueError("Must have a avialable python exe(project or gloabl)")
        return project_python_exe_path

    def parse_command(self, command: str) -> None:
        loguru.logger.debug(f"开始解析命令: {command}")

        def parse_python_path(command: str) -> str:
            """从Nuitka命令中提取Python路径"""
            patterns = [
                r'^(python)\s+.*nuitka',  # Case 1: python followed by nuitka command
                r'^(python\s+-m\s+nuitka)',  # Case 2: python -m nuitka followed by nuitka command
                r'^"(.+python\.exe)"\s+.*nuitka',  # Case 3: long python.exe path in quotes followed by nuitka command
                r'^"(.+python\.exe)"\s+-m\s+nuitka',
                # Case 4: long python.exe path in quotes -m nuitka followed by nuitka command
                r'^(.+python\.exe)\s+.*nuitka',  # Case 5: long python.exe path followed by nuitka command
                r'^(.+python\.exe)\s+-m\s+nuitka'  # Case 6: long python.exe path -m nuitka followed by nuitka command
            ]

            for pattern in patterns:
                match = re.match(pattern, command)
                if match:
                    return match.group(1)

            loguru.logger.error(f"Failed to parse python path from command: {command}, use default python path")
            return 'python'

        python_path: str = parse_python_path(command)
        loguru.logger.debug(f"Python path: {python_path}")

        command_excluded_text: list[str] = [
            python_path,
            '-m',
            'nuitka'
        ]
        command_args: list[str] = []
        for each in command.split(" "):
            if each in command_excluded_text or not each:
                continue
            command_args.append(each)
        command = " ".join(command_args)

        for each in command.split(" "):
            command_str_list: list[str] = each.split("=")
            command_name = command_str_list[0]
            # 去掉开头的-
            while command_name.startswith("-"):
                command_name = command_name[1:]
            command_value: Optional[str] = command_str_list[1] if len(command_str_list) > 1 else None
            command = self.get_command_by_command(command_name)
            if not command:
                loguru.logger.error(f"Unknown command: {command_name}")
                is_keep_unsupported_command: bool = cfg.get(cfg.keep_unsupported_command)
                if is_keep_unsupported_command:
                    self._extra_command_list.append(each)
                continue
            loguru.logger.debug(f"command_name: {command_name}, command_value: {command_value}")
            command.parse(command_value)

        self.update_widget()
        # 因为插件页面的命令是动态生成的,所以需要单独处理
        plugin_command = self.get_command_by_command('enable-plugins')
        self.manager_plugin.disable_all_plugin()
        for each in self.manager_plugin.filter_plugins(plugin_command.value.split(",")):
            self.manager_plugin.set_plugin_enable(each, True)

        self._signal_bus.update_plugin_view.emit()

    def update_command_list(self):
        self.command_list = []
        for manager in self.manager_list:
            self.command_list.extend(manager.command_list)

    def update_widget(self):
        for manager in self.manager_list:
            manager.update_widget()

    def get_command_by_type(
            self, command_type: Type[CommandBaseType]
    ) -> Optional[CommandBaseType]:
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
