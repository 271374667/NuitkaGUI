from pathlib import Path
from typing import List, Tuple, Optional

from src.common.nuitka_command.command_manager import CommandManager
from src.utils.dependence_utils import DependenceUtils


class PluginModel:
    def __init__(self):
        self._command_manager = CommandManager()

    def get_source_script(self) -> Optional[Path]:
        return self._command_manager.source_script

    def get_enable_plugins(self) -> List[str]:
        return self._command_manager.manager_plugin.enable_plugins

    def get_all_packages_by_py_file(self, py_file: Path) -> List[str]:
        dependence_list: list[str] = []
        all_py_file_in_dir = py_file.parent.rglob('*.py')
        for i in all_py_file_in_dir:
            dependence_list.extend(DependenceUtils().get_import_name_from_py_file(i))
        return self._command_manager.manager_plugin.filter_plugins(list(set(dependence_list)))

    def set_plugin_status(self, plugin_name: str, status: bool) -> None:
        self._command_manager.manager_plugin.set_plugin_enable(plugin_name, status)

    def disable_all_plugin(self) -> None:
        self._command_manager.manager_plugin.disable_all_plugin()

    def fetch_plugin_from_cmd(self) -> List[Tuple[str, str]]:
        return self._command_manager.manager_plugin.fetch_plugin_from_cmd()


if __name__ == '__main__':
    m = PluginModel()
    print(m.get_all_packages_by_py_file(Path(r"E:\load\python\Project\nuitkaGUIOld\githubOpenSource2\main.py")))
