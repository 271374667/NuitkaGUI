import re
from pathlib import Path

import loguru

from src.common.manager.pip_manager import PipManager
from src.common.manager.settings_manager import SettingsManager
from src.conf import config
from src.core import JsonSettings
from src.utils.singleton import Singleton


@Singleton
class ModuleManager:
    def __init__(self):
        self.settings_manager = SettingsManager()
        self.fastest_pip_source = self.settings_manager.get(JsonSettings.FastestPipSrouce.value)
        self.avaliable_python = self.settings_manager.get(JsonSettings.PythonExe.value)
        self.pip_manager = PipManager()

    @staticmethod
    def get_all_package_in_dir(dir_path: Path) -> list[str]:
        """获取目录下所有的包

        Args:
            dir_path: 目录路径

        Returns:
            当前目录下所有的模块
        """
        p = re.compile(r'^import\s+(.*)|^from\s+(.*?)\s+import\s+(.*)')
        all_package_list = []

        # 分割其中的逗号和点
        for file in dir_path.glob('**/*.py'):
            print(f'正在分析文件:{file}')
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
        return list(set(all_package_list))

    def initialize(self):
        module_list = [x.name for x in config.ModuleVersion]  # ['nuitka']
        for each in module_list:
            self.pip_manager.install(each)
        loguru.logger.debug('第三方库模块初始化完成!')


if __name__ == '__main__':
    from src.conf import config_path
    from pprint import pprint

    m = ModuleManager()
    # m.enable_default_options()
    result = m.get_all_package_in_dir(config_path.SRC_HOME)
    pprint(result)
