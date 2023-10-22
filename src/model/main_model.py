from src.common.manager.settings_manager import SettingsManager
from src.core import JsonSettings


class MainModel:
    def __init__(self):
        self.settings_manager: SettingsManager = SettingsManager()

    def get_pythonexe(self) -> str:
        return self.settings_manager.get(JsonSettings.PythonExe.value)

    def set_optimization_enabled(self, status: bool) -> None:
        self.settings_manager.set(JsonSettings.OptimizationEnabled.value, status)

    def is_pythonexe_available(self) -> bool:
        pythonexe = self.get_pythonexe()
        if not pythonexe or pythonexe == '':
            return False
        return True

    def is_optimization_enabled(self) -> bool:
        return self.settings_manager.get(JsonSettings.OptimizationEnabled.value)
