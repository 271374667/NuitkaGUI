import loguru

from src.common.manager.gcc_manager import GccManager
from src.common.manager.pip_manager import PipManager
from src.common.manager.python_manager import PythonManager
from src.common.manager.settings_manager import SettingsManager


class WelcomeModel:
    def __init__(self):
        self._settings_manager = SettingsManager()
        self._python_manager = PythonManager()
        self._pip_manager = PipManager()
        self._gcc_manager = GccManager()

    def get_pythonexe_path(self) -> str:
        """获取一个可用的 python.exe 路径"""
        pythonexe_list = self._python_manager.find_available_python_exe_python()
        return str(pythonexe_list[0]) if pythonexe_list else ""

    def set_pythonexe_path(self, pythonexe: str) -> None:
        """将 python.exe 路径写入配置文件"""
        self._settings_manager.set(SettingsManager.PYTHONEXE, pythonexe)
        loguru.logger.info(f'设置本地配置文件的 python.exe 路径: {pythonexe}')

    def is_pythonexe_avialable(self, pythonexe: str) -> bool:
        """检查当前的 python.exe 是否可用"""
        return self._python_manager.is_python_available(pythonexe)

    def get_default_pip_source(self) -> str:
        """获取默认的 pip 源(官方源)"""
        return self._pip_manager.get_default_pip_source()

    def get_fastest_pip_source(self) -> str:
        """获取一个最快的 pip 源"""
        return self._pip_manager.get_fastest_pip_source_by_network()

    def set_pip_source(self, value: str) -> None:
        """设置 pip 源"""
        self._pip_manager.set_pip_source(value)

    def get_gcc_available(self) -> bool:
        """检查当前的 gcc 是否可用"""
        return self._gcc_manager.is_gcc_available()

    def set_gcc_available(self, gcc_available: bool) -> None:
        """设置 gcc 是否可用"""
        self._settings_manager.set(SettingsManager.GCC_AVAILABLE, gcc_available)

    def download_gcc(self) -> None:
        """下载 gcc"""
        self._gcc_manager.initialize()
