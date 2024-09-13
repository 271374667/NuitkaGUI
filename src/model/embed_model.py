from pathlib import Path
from typing import Optional

from src.common.nuitka_command.command_manager import CommandManager


class EmbedModel:
    def __init__(self):
        self._command_manager = CommandManager()

    def get_source_script_path(self) -> Optional[Path]:
        return self._command_manager.source_script

    def add_include_data_files(self, value: str):
        self._command_manager.include_data_files.add(value)

    def extend_include_data_files(self, values: list[str]):
        self._command_manager.include_data_files.extend(values)

    def add_include_data_dir(self, value: str):
        self._command_manager.include_data_dir.add(value)

    def extend_include_data_dir(self, values: list[str]):
        self._command_manager.include_data_dir.extend(values)
