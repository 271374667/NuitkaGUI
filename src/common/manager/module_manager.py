import loguru

from src.common.manager.pip_manager import PipManager
from src.common.manager.runtime_config_manager import RuntimeManager
from src.conf import config


class ModuleManager:
    def __init__(self):
        self.fastest_pip_source = RuntimeManager.read(RuntimeManager.FASTEST_PIP_SOURCE)
        self.avaliable_python_list = RuntimeManager.read(RuntimeManager.AVAILABLE_PYTHON_LIST)
        self.pip_manager = PipManager()

    def initialize(self):
        module_list = [x.name for x in config.ModuleVersion]  # ['nuitka', 'pipreqs']
        for each in module_list:
            self.pip_manager.install(each)
        loguru.logger.debug('第三方库模块初始化完成!')


if __name__ == '__main__':
    m = ModuleManager()
    m.initialize()