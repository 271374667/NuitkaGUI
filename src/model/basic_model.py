from pathlib import Path
from typing import Optional

from src.common.nuitka_command.command_manager import CommandManager


class BasicModel:
    def __init__(self):
        self._command_manager = CommandManager()

    @property
    def source_script_path(self) -> Optional[Path]:
        return self._command_manager.source_script

    @source_script_path.setter
    def source_script_path(self, source_script: Optional[Path]) -> None:
        self._command_manager.source_script = source_script

    @property
    def output_dir(self) -> Optional[Path]:
        return self._command_manager.output_dir

    @output_dir.setter
    def output_dir(self, output_dir: Optional[Path]) -> None:
        self._command_manager.output_dir.value = output_dir

    @property
    def icon_path(self) -> Optional[Path]:
        return self._command_manager.windows_icon_from_ico

    @icon_path.setter
    def icon_path(self, icon_path: Optional[Path]) -> None:
        self._command_manager.windows_icon_from_ico.value = icon_path

    @property
    def packaged_mode(self) -> str:
        if self._command_manager.standalone.value:
            return 'standalone'
        return 'onefile'

    @packaged_mode.setter
    def packaged_mode(self, mode: str) -> None:
        if mode == 'standalone':
            self._command_manager.standalone.value = True
            self._command_manager.onefile.value = False
        else:
            self._command_manager.standalone.value = False
            self._command_manager.onefile.value = True
