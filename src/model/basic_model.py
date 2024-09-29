from pathlib import Path
from typing import Optional

from src.common.nuitka_command.command_manager import CommandManager
from src.config import cfg


class BasicModel:
    def __init__(self):
        self._command_manager = CommandManager()
        self._output_command = self._command_manager.get_command_by_command('output-dir')
        self._windows_icon_command = self._command_manager.get_command_by_command('windows-icon-from-ico')

    @property
    def source_script_path(self) -> Optional[Path]:
        return self._command_manager.source_script

    @source_script_path.setter
    def source_script_path(self, source_script: Optional[Path]) -> None:
        self._command_manager.source_script = source_script

    @property
    def project_python_exe_path(self) -> Path:
        return Path(cfg.get(cfg.project_python_exe_path))

    @project_python_exe_path.setter
    def project_python_exe_path(self, project_python_exe_path: Path) -> None:
        cfg.set(cfg.project_python_exe_path, str(project_python_exe_path))

    @property
    def output_dir(self) -> Optional[Path]:
        return Path(self._output_command.value)

    @output_dir.setter
    def output_dir(self, output_dir: Optional[Path]) -> None:
        self._output_command.value = output_dir

    @property
    def icon_path(self) -> Optional[Path]:
        return Path(self._windows_icon_command.value)

    @icon_path.setter
    def icon_path(self, icon_path: Optional[Path]) -> None:
        self._windows_icon_command.value = icon_path

    @property
    def packaged_mode(self) -> str:
        standalone_command = self._command_manager.get_command_by_command('standalone')
        if standalone_command.value:
            return 'standalone'
        return 'onefile'

    @packaged_mode.setter
    def packaged_mode(self, mode: str) -> None:
        standalone_command = self._command_manager.get_command_by_command('standalone')
        onefile_command = self._command_manager.get_command_by_command('onefile')
        if mode == 'standalone':
            standalone_command.value = True
            onefile_command.value = False
        else:
            standalone_command.value = False
            onefile_command.value = True

    def start(self):
        ...
