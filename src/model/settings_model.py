from src.common.manager.pip_manager import PipManager
from src.common.manager.python_manager import PythonManager
from src.common.manager.settings_manager import SettingsManager
from src.conf import config_path
from src.core import JsonSettings


class SettingsModel:
    def __init__(self):
        self.settings_manager: SettingsManager = SettingsManager()
        self.pip_manager: PipManager = PipManager()
        self.python_manager: PythonManager = PythonManager()

    def set_pythonexe(self, pythonexe: str) -> None:
        self.settings_manager.set(JsonSettings.PYTHONEXE.value, pythonexe)

    def get_auto_pythonexe(self) -> str:
        """返回一个可用的 Python.exe 路径"""
        pythonexe_auto = self.python_manager.find_available_python_exe_python()
        if pythonexe_auto:
            return str(pythonexe_auto[0])
        return ''

    def set_pip_source(self, pip_source: str) -> None:
        self.settings_manager.set(JsonSettings.FASTEST_PIP_SOURCE.value, pip_source)

    def set_optimization_enabled(self, optimization_enabled: bool) -> None:
        self.settings_manager.set(JsonSettings.OPTIMIZATION_ENABLED.value, optimization_enabled)

    def get_fastest_pip_source(self) -> str:
        return self.pip_manager.get_fastest_pip_source_by_network()

    def initialize_settings_json_file(self) -> None:
        settings_file = config_path.SETTINGS_FILE
        if settings_file.exists():
            settings_file.unlink(missing_ok=True)
        self.settings_manager.initialize()
