import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import loguru

from src.common.manager.settings_manager import SettingsManager
from src.core import JsonSettings
from src.core import Plugin
from src.utils.singleton import Singleton


@Singleton
class PluginManager:
    def __init__(self):
        self._plugin_list = None
        self.settings_manager = SettingsManager()
        self._pythonexe_path = self.settings_manager.get(JsonSettings.PythonExe.value)
        self._plugin_enable_dict: Dict[Union[Plugin, str], bool] = {}

        self.trans = {'PySide6': 'pyside6',
                'PySide2': 'pyside2',
                'PyQt6': 'pyqt6',
                'PyQt5': 'pyqt5',
                'tkinter': 'tk-inter',
                'Pmw': 'pmw-freezer',
                'pbr': 'pbr-compat',
                'dill': 'dill-compat',
                'support': 'delvewheel',
                }

    def get_selected_plugins(self) -> List[str]:
        """获取当前选中的插件列表，比如['tk-inter', 'pyside6', 'pyqt5']

        获取当前选中的插件列表，比如['tk-inter', 'pyside6', 'pyqt5']

        """
        return [key for key, value in self._plugin_enable_dict.items() if value is True]

    def get_cmd(self) -> List[str]:
        """获取插件命令

        获取插件命令，比如 --enable-plugin=tk-inter,pyside6,pyqt5

        """
        enable_plugin_list = self.get_selected_plugins()
        return [f'--enable-plugin={",".join(enable_plugin_list)}']

    def get_all_plugin_in_dir(self, dir_path: Path) -> list[str]:
        """获取目录下所有可能用到的插件

        Args:
            dir_path: 目录路径

        Returns:
            当前目录下可开启的插件
        """
        p = re.compile(r'^import\s+(.*)|^from\s+(.*?)\s+import\s+(.*)', re.MULTILINE)
        all_package_list = []
        plugins_list = []

        # 分割其中的逗号和点
        for file in dir_path.glob('**/*.py'):
            content = file.read_text(encoding='utf-8', errors='ignore')
            find_result = p.findall(content)
            for each_group in find_result:
                for each in each_group:
                    if '.' in each:
                        all_package_list.extend(each.split('.'))
                    elif ',' in each:
                        all_package_list.extend(each.split(','))
                    elif each != '':
                        all_package_list.append(each)

        all_package_list = list(set(all_package_list))
        for each in all_package_list:
            if each in self.trans:
                each = self.trans[each]
            plugin = self._find_enum_by_value(each)
            if plugin is not None:
                plugins_list.append(plugin.value)

        return plugins_list

    def fetch_plugin_from_cmd(self) -> List[Tuple[str, str]]:
        """从命令行获取插件列表"""
        if not self._pythonexe_path:
            self._pythonexe_path = 'python'
        try:
            arg = [self._pythonexe_path, '-m', 'nuitka', '--plugin-list']
            result = subprocess.check_output(arg)
            result_list = result.decode('utf-8').splitlines()[2:]
            result_list = [(x.split(maxsplit=1)[0], x.split(maxsplit=1)[1]) for x in result_list]
            self._plugin_list = result_list
            loguru.logger.debug(f'获取到{len(self._plugin_list)}个插件')
            return self._plugin_list
        except TimeoutError:
            loguru.logger.error('获取插件列表超时')
        except Exception as e:
            loguru.logger.critical(f'获取插件列表失败，错误信息: {e}')
        return [('', '')]

    def set_plugin_status(self, plugin_name: Union[Plugin, str], enable: bool) -> None:
        """设置插件状态

        通过字典的方式添加插件，插件的名字作为键，插件的状态作为值，True 为启用，False 为禁用

        Args:
            plugin_name: 插件的名字，从core.Plugin获取
            enable: 是否开启

        Returns:
            None
        """

        # 因为在nuitka的插件里面有一些插件的名字和包名不一致，比如:
        # PySide6 -> pyside6, tkinter -> tk-inter
        # 所以需要做一些转换
        if isinstance(plugin_name, Plugin):
            plugin_name = plugin_name.value

        if plugin_name in self.trans:
            self._plugin_enable_dict[self.trans[plugin_name]] = enable
            return
        self._plugin_enable_dict[plugin_name] = enable

    def get_plugin_status(self, plugin_name: Union[Plugin, str]) -> bool:
        """获取插件状态

        Args:
            plugin_name: 插件的名字，从类属性中获取

        Returns:
            插件的状态
        """
        if isinstance(plugin_name, Plugin):
            plugin_name = plugin_name.value

        if plugin_name in self.trans:
            plugin_name = self.trans[plugin_name]

        return self._plugin_enable_dict.get(plugin_name, False)

    def set_plugins_enable(self, plugins: List[str]) -> None:
        """设置插件状态

        Args:
            plugins: 插件列表

        Returns:
            None
        """
        for plugin in plugins:
            self.set_plugin_status(plugin, True)

    def set_plugins_disable(self, plugins: List[str]) -> None:
        """设置插件状态

        Args:
            plugins: 插件列表

        Returns:
            None
        """
        for plugin in plugins:
            self.set_plugin_status(plugin, False)

    def clear_plugin(self) -> None:
        """清空插件"""
        self._plugin_enable_dict = {}

    def _find_enum_by_value(self, value: str) -> Optional[Plugin]:
        for i in Plugin:
            if i.value == value:
                return i
        return None

    @staticmethod
    def initialize():
        """初始化插件管理器"""
        loguru.logger.success('插件参数初始化完成')


if __name__ == '__main__':
    a = PluginManager()
    # result = a.fetch_plugin_from_cmd()
    # print(result)
    a.set_plugin_status(Plugin.ANTI_BLOAT, True)
    a.set_plugin_status(Plugin.TK_INTER, True)
    a.set_plugin_status(Plugin.PYQT5, True)
    a.set_plugin_status(Plugin.ANTI_BLOAT, False)
    print(a.get_cmd())
    # result = a.get_all_plugin_in_dir(config_path.SRC_HOME)
    # print(result)
    # a.set_plugins_enable(result)
    # print(a.get_cmd())
