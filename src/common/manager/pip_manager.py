import subprocess

import loguru

from src.common.manager.settings_manager import SettingsManager
from src.conf import config
from src.utils.get_fastest_url import get_fastest_url


class PipManager:
    DEFAULT_PIP_SOURCE = config.PipSource.Default.value

    def __init__(self):
        self.settings_manager = SettingsManager()

        self.fastest_pip_source = self.settings_manager.get(SettingsManager.FASTEST_PIP_SOURCE)
        self.pythonexe = self.settings_manager.get(SettingsManager.PYTHONEXE)

    def install(self, package_name: str):
        """安装 pip 包
        Args:
            package_name: 包名
        """
        loguru.logger.debug(f'安装 pip 包: {package_name}')

        # 如果没有设置 pip 源,则默认使用清华源
        if self.fastest_pip_source is None:
            self.fastest_pip_source = config.PipSource.QingHua.value

        available_python = self.pythonexe
        command_args_list = [available_python, '-m', 'pip', 'install', package_name, '-i',
                self.fastest_pip_source, '-U']
        loguru.logger.debug(f'执行命令: {command_args_list}')

        try:
            subprocess.run(command_args_list,
                           stdin=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           encoding=config.system_encoding)
            loguru.logger.debug(f'安装完成: {package_name}')
        except Exception as e:
            loguru.logger.error(f'安装失败: {package_name} {e}')

    def get_module_version(self, module_name: str):
        """该方法目前是冗余方法，没有实际上被使用"""
        response = subprocess.run([self.pythonexe, '-m', 'pip', 'show', module_name],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, encoding='gbk')
        if response.stderr:
            return ''
        return response.stdout.splitlines()[1].split(maxsplit=1)[1]

    @staticmethod
    def get_fastest_pip_source_by_network() -> str:
        """现在通过requests获取最快的 pypi 源"""
        return get_fastest_url([x.value for x in config.PipSource])

    def get_fastest_pip_source_by_settings(self) -> str:
        """从本地配置文件获取最快的 pypi 源"""
        return self.fastest_pip_source

    def set_pip_source(self, value: str) -> None:
        self.settings_manager.set(SettingsManager.FASTEST_PIP_SOURCE, value)

    @staticmethod
    def get_default_pip_source() -> str:
        """获取默认的 pypi 源"""
        return config.PipSource.Default.value

    def initialize(self):
        self.fastest_pip_source = get_fastest_url([x.value for x in config.PipSource])
        self.settings_manager.set(SettingsManager.FASTEST_PIP_SOURCE, self.fastest_pip_source)
        loguru.logger.debug(f'pip 源初始化完成!最快的 pip 源: {self.fastest_pip_source}')


if __name__ == '__main__':
    a = PipManager()
    a.initialize()
    print(a.fastest_pip_source)