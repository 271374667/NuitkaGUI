from src.common.manager.pip_manager import PipManager
from src.common.manager.runtime_config_manager import RuntimeManager
from src.conf import config


class ModuleManager:
    def __init__(self):
        self.fastest_pip_source = RuntimeManager.read(RuntimeManager.FASTEST_PIP_SOURCE)
        self.avaliable_python_list = RuntimeManager.read(RuntimeManager.AVAILABLE_PYTHON_LIST)
        self.pip_manager = PipManager()

    def _install_nuitka(self):
        self.pip_manager.install(f'{config.ModuleVersion.nuitka.name}=={config.ModuleVersion.nuitka.value}')

    def initialize(self):
        pass
