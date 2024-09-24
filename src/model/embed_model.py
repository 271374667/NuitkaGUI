from pathlib import Path
from typing import Optional

from src.common.nuitka_command.command_implement import command_multiple_times
from src.common.nuitka_command.command_manager import CommandManager


class EmbedModel:
    def __init__(self):
        self._command_manager = CommandManager()

    @property
    def source_script_path(self) -> Optional[Path]:
        return self._command_manager.source_script

    @source_script_path.setter
    def source_script_path(self, source_script: Optional[Path]) -> None:
        self._command_manager.source_script = source_script

    def add_include_data_files(self, value: str):
        include_data_files = self._command_manager.get_command_by_type(command_multiple_times.CommandIncludeDataFiles)
        include_data_files.add(value)

    def extend_include_data_files(self, values: list[str]):
        include_data_files = self._command_manager.get_command_by_type(command_multiple_times.CommandIncludeDataFiles)
        include_data_files.extend(values)

    def set_include_data_files(self, values: list[str]):
        include_data_files = self._command_manager.get_command_by_type(command_multiple_times.CommandIncludeDataFiles)
        include_data_files.value = values

    def add_include_data_dir(self, value: str):
        include_data_dir = self._command_manager.get_command_by_type(command_multiple_times.CommandIncludeDataDir)
        include_data_dir.add(value)

    def extend_include_data_dir(self, values: list[str]):
        include_data_dir = self._command_manager.get_command_by_type(command_multiple_times.CommandIncludeDataDir)
        include_data_dir.extend(values)

    def set_include_data_dir(self, values: list[str]):
        include_data_dir = self._command_manager.get_command_by_type(command_multiple_times.CommandIncludeDataDir)
        include_data_dir.value = values
