import subprocess
from typing import List, Tuple

import loguru

from src.common.manager.runtime_config_manager import RuntimeManager


class PluginManager:
    def __init__(self):
        self.runtime_manager = RuntimeManager()
        self._pythonexe_path = self.runtime_manager.get(RuntimeManager.AVAILABLE_PYTHON_LIST)[0]
        print(self._pythonexe_path)
        self._plugin_list = []

    def get_plugin_from_cmd(self) -> List[Tuple[str, str]]:
        try:
            result = subprocess.check_output([self._pythonexe_path, '-m', 'nuitka', '--plugin-list'])
            result_list = result.decode('utf-8').splitlines()[2:]
            result_list = [(x.split(maxsplit=1)[0], x.split(maxsplit=1)[1]) for x in result_list]
            self._plugin_list = result_list
            loguru.logger.debug(f'获取到{len(self._plugin_list)}个插件')
            return self._plugin_list
        except TimeoutError:
            loguru.logger.error('获取插件列表超时')
        return [('', '')]

    def initialize(self):
        """初始化插件管理器"""
        loguru.logger.success('插件参数初始化完成')


if __name__ == '__main__':
    a = PluginManager()
    result = a.get_plugin_from_cmd()
    print(result)
