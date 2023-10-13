from pathlib import Path
from typing import List

from src.common.manager.plugin_manager import PluginManager


class PluginModel:
    def __init__(self):
        self._plugin_manager = PluginManager()

    def get_plugin_manager(self) -> PluginManager:
        return self._plugin_manager

    def get_plugin_status(self, plugin_name: str) -> bool:
        return self._plugin_manager.get_plugin_status(plugin_name)

    def set_plugin_status(self, plugin_name: str, status: bool) -> None:
        self._plugin_manager.set_plugin_status(plugin_name, status)

    def fetch_plugin_from_cmd(self) -> List[tuple[str, str]]:
        return self._plugin_manager.fetch_plugin_from_cmd()

    def get_selected_plugins(self) -> List[str]:
        return self._plugin_manager.get_selected_plugins()

    def get_cmd(self) -> List[str]:
        return [self._plugin_manager.get_plugins_command()]

    def initialize(self):
        self._plugin_manager.initialize()

    def get_all_packages_by_py_file(self, py_file: Path) -> List[str]:
        return self._plugin_manager.get_all_plugin_in_dir(py_file.parent)
