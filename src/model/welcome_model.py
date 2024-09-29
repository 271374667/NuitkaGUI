from pathlib import Path
from typing import Optional

from src.common.manager.env_manager import EnvManager
from src.common.manager.pip_manager import PipManager
from src.config import cfg, PipSrouce
from src.utils.python_env_utils import PythonEnvUtils


class WelcomeModel:
    def __init__(self):
        self._env_manager = EnvManager()
        self._pip_manager = PipManager()
        self._python_env_utils = PythonEnvUtils()

    @property
    def pip_source(self) -> PipSrouce:
        return cfg.get(cfg.pip_source)

    @pip_source.setter
    def pip_source(self, value: PipSrouce) -> None:
        cfg.set(cfg.pip_source, value)

    @property
    def default_pip_source(self) -> PipSrouce:
        return PipSrouce.Default

    @property
    def python_exe_path(self) -> Optional[str]:
        return cfg.get(cfg.python_exe_path)

    @python_exe_path.setter
    def python_exe_path(self, value: Optional[str]) -> None:
        if value:
            cfg.set(cfg.global_python_exe_path, value)
        else:
            cfg.set(cfg.global_python_exe_path, "")

    def auto_pip_source(self) -> Optional[str]:
        return self._pip_manager.get_fastest_url([i.value for i in PipSrouce])

    def is_python_available(self, python_exe_path: str) -> bool:
        return self._python_env_utils.is_python_available(python_exe_path)

    def auto_python_exe_path(self) -> Optional[str]:
        python_exe_path_found: list[Path] = self._python_env_utils.find_available_python_exe_python()
        for each in python_exe_path_found:
            if self.is_python_available(str(each)):
                return str(each)

    def install_dependence_by_os(self) -> bool:
        self._env_manager.add_dependence_to_env_by_os()
        return True

    def install_dependence_by_bat(self) -> bool:
        self._env_manager.add_dependence_to_env_by_bat()
        return self._env_manager.is_all_dependence_in_env()

    def finished(self):
        cfg.set(cfg.is_first_run, False)


if __name__ == '__main__':
    model = WelcomeModel()
