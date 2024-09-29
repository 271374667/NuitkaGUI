from pathlib import Path
from typing import List, Tuple, Optional

from src.common.nuitka_command.command_manager import CommandManager
from src.core.settings import IGNORE_DIRS
from src.utils.dependence_utils import DependenceUtils
from src.utils.window_explorer_utils import WindowExplorerUtils


class PluginModel:
    def __init__(self):
        self._command_manager = CommandManager()
        self._window_explorer_utils = WindowExplorerUtils()

    def get_source_script(self) -> Optional[Path]:
        return self._command_manager.source_script

    def get_enable_plugins(self) -> List[str]:
        return self._command_manager.manager_plugin.enable_plugins

    def get_all_packages_by_py_file(self, py_file: Path) -> List[str]:
        dependence_list: list[str] = []
        all_py_file_in_dir = self._window_explorer_utils.find_files_in_dir_recursive_by_fnmatch(py_file.parent, '*.py',
                                                                                                self._window_explorer_utils.FileType.FILES)
        all_py_file_in_dir = [i for i in all_py_file_in_dir if
                              not any(self._is_substring_in_path(j, str(i)) for j in IGNORE_DIRS)]
        for i in all_py_file_in_dir:
            dependence_list.extend(DependenceUtils().get_import_name_from_py_file(i))
        return self._command_manager.manager_plugin.filter_plugins(list(set(dependence_list)))

    def set_plugin_status(self, plugin_name: str, status: bool) -> None:
        self._command_manager.manager_plugin.set_plugin_enable(plugin_name, status)

    def disable_all_plugin(self) -> None:
        self._command_manager.manager_plugin.disable_all_plugin()

    def fetch_plugin_from_cmd(self) -> List[Tuple[str, str]]:
        return self._command_manager.manager_plugin.fetch_plugin_from_cmd()

    def _is_substring_in_path(self, search_term: str, path: str) -> bool:
        path_obj = Path(path)
        return any(part == search_term for part in path_obj.parts)


if __name__ == '__main__':
    m = PluginModel()
    print(m.get_all_packages_by_py_file(Path(r"E:\load\python\Project\nuitkaGUIOld\githubOpenSource2\main.py")))
