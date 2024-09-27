import sys
from pathlib import Path

from src.config import cfg


class SettingModel:
    @property
    def project_python_exe_path(self) -> Path:
        return Path(cfg.get(cfg.project_python_exe_path))

    @project_python_exe_path.setter
    def project_python_exe_path(self, project_python_exe_path: Path) -> None:
        cfg.set(cfg.project_python_exe_path, str(project_python_exe_path))

    @property
    def global_python_exe_path(self) -> Path:
        return Path(cfg.get(cfg.global_python_exe_path))

    @global_python_exe_path.setter
    def global_python_exe_path(self, global_python_exe_path: Path) -> None:
        cfg.set(cfg.global_python_exe_path, str(global_python_exe_path))

    def exit(self):
        """重启应用"""
        sys.exit()
