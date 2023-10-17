from pathlib import Path
from typing import List

from src.common.manager.command_manager import CommandManager
from src.common.manager.plugin_manager import PluginManager
from src.core import StrCommands


class PluginModel:
    def __init__(self):
        self._plugin_manager: PluginManager = PluginManager()
        self._command_manager: CommandManager = CommandManager()

    def get_plugin_status(self, plugin_name: str) -> bool:
        return self._plugin_manager.get_plugin_status(plugin_name)

    def set_plugin_status(self, plugin_name: str, status: bool) -> None:
        self._plugin_manager.set_plugin_status(plugin_name, status)
        self._command_manager.set_plugins_cmd(self._plugin_manager.get_cmd())

    def fetch_plugin_from_cmd(self) -> List[tuple[str, str]]:
        return self._plugin_manager.fetch_plugin_from_cmd()

    def get_selected_plugins(self) -> List[str]:
        return self._plugin_manager.get_selected_plugins()

    def get_cmd(self) -> List[str]:
        return self._plugin_manager.get_cmd()

    def get_py_file(self) -> str:
        return self._command_manager.get_option_value(StrCommands.main)

    def initialize(self):
        self._plugin_manager.initialize()

    def get_all_packages_by_py_file(self, py_file: Path) -> List[str]:
        return self._plugin_manager.get_all_plugin_in_dir(py_file.parent)
