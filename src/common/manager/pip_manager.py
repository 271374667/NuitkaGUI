import subprocess

import loguru

from src.common.manager.runtime_config_manager import RuntimeManager
from src.conf import config
from src.utils.get_fastest_url import get_fastest_url


class PipManager:
    def __init__(self):
        self.fastest_pip_source = RuntimeManager.read(RuntimeManager.FASTEST_PIP_SOURCE)

    def install(self, package_name: str):
        """安装 pip 包
        Args:
            package_name: 包名
        """
        loguru.logger.debug(f'安装 pip 包: {package_name}')

        # 如果没有设置 pip 源,则默认使用清华源
        if self.fastest_pip_source is None:
            self.fastest_pip_source = config.PipSource.QingHua.value

        available_python = RuntimeManager.read(RuntimeManager.AVAILABLE_PYTHON_LIST[0])
        command_args_list = [available_python, 'install', package_name, '-i',
                self.fastest_pip_source]
        loguru.logger.debug(f'执行命令: {command_args_list}')
        subprocess.run(command_args_list,
                       stdin=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       encoding=config.system_encoding)
        loguru.logger.debug(f'安装完成: {package_name}')

    def initialize(self):
        self.fastest_pip_source = get_fastest_url([x.value for x in config.PipSource])
        RuntimeManager.set(RuntimeManager.FASTEST_PIP_SOURCE, self.fastest_pip_source)
        loguru.logger.debug(f'pip 源初始化完成!最快的 pip 源: {self.fastest_pip_source}')


if __name__ == '__main__':
    a = PipManager()
    a.initialize()
    print(a.fastest_pip_source)
