import subprocess
from typing import List, Tuple, Dict

import loguru

from src.config import cfg


class ManagerPlugin:
    def __init__(self):
        self._plugin_list = None
        self._pythonexe_path: str = cfg.get(cfg.global_python_exe_path)
        self._plugin_enable_dict: Dict[str, bool] = {}

        self._plugin_mapping = {
            "anti-bloat": "anti-bloat",
            "data-files": "data-files",
            "support": "delvewheel",
            "dill": "dill-compat",
            "dll-files": "dll-files",
            "enum": "enum-compat",
            "eventlet": "eventlet",
            "gevent": "gevent",
            "gi": "gi",
            "glfw": "glfw",
            "implicit-imports": "implicit-imports",
            "kivy": "kivy",
            "matplotlib": "matplotlib",
            "multiprocessing": "multiprocessing",
            "no-qt": "no-qt",
            "options-nanny": "options-nanny",
            "pbr": "pbr-compat",
            "pkg-resources": "pkg-resources",
            "Pmw": "pmw-freezer",
            "pylint-warnings": "pylint-warnings",
            "PyQt5": "pyqt5",
            "PyQt6": "pyqt6",
            "PySide2": "pyside2",
            "PySide6": "pyside6",
            "pywebview": "pywebview",
            "spacy": "spacy",
            "tkinter": "tk-inter",
            "transformers": "transformers",
            "upx": "upx",
        }

        self._plugin_mapping_reverse = {v: k for k, v in self._plugin_mapping.items()}

    @property
    def enable_plugins(self) -> list[str]:
        return [k for k, v in self._plugin_enable_dict.items() if v]

    def set_plugin_enable(self, plugin_name: str, status: bool) -> None:
        """设置插件的状态"""
        self._plugin_enable_dict[plugin_name] = status

    def disable_all_plugin(self) -> None:
        """禁用所有插件"""
        for k in self._plugin_enable_dict:
            self._plugin_enable_dict[k] = False

    def fetch_plugin_from_cmd(self) -> List[Tuple[str, str]]:
        """从命令行获取插件列表"""
        if not self._pythonexe_path:
            self._pythonexe_path = "python"
        try:
            arg = [self._pythonexe_path, "-m", "nuitka", "--plugin-list"]
            result = subprocess.check_output(arg)
            result_list = result.decode("utf-8").splitlines()[2:]
            result_list = [
                (x.split(maxsplit=1)[0], x.split(maxsplit=1)[1]) for x in result_list
            ]
            self._plugin_list = result_list
            loguru.logger.debug(f"获取到{len(self._plugin_list)}个插件")
            return self._plugin_list
        except TimeoutError:
            loguru.logger.error("获取插件列表超时")
        except Exception as e:
            loguru.logger.critical(f"获取插件列表失败，错误信息: {e}")
        return [("", "")]
    
    def filter_plugins(self, plugin_list: list[str]) -> list[str]:
        """过滤掉不支持的插件"""
        filter_plugin_list: list[str] = []
        for i in plugin_list:
            if i in self._plugin_mapping:
                filter_plugin_list.append(self._plugin_mapping[i])
            elif i in self._plugin_mapping_reverse:
                filter_plugin_list.append(i)
        return filter_plugin_list


if __name__ == "__main__":
    pm = ManagerPlugin()
    print(pm.fetch_plugin_from_cmd())
