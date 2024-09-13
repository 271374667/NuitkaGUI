from pathlib import Path
from typing import Optional

from src.common.nuitka_command.command_multiple_times import CommandIncludeDataFiles, CommandIncludeDataDir
from src.common.nuitka_command.command_plugin import CommandPlugin
from src.utils.singleton import singleton


@singleton
class CommandManager:
    def __init__(self):
        self._source_script: Optional[Path] = None

        # multiple times
        self.include_data_files = CommandIncludeDataFiles()
        self.include_data_dir = CommandIncludeDataDir()

        # Plugins
        self.command_plugin = CommandPlugin()

    @property
    def source_script(self) -> Optional[Path]:
        return self._source_script

    @source_script.setter
    def source_script(self, source_script: Optional[Path]) -> None:
        self._source_script = source_script
