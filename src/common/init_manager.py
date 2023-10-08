from src.common.manager.settings_manager import SettingsManager

from src.common.manager.gcc_manager import GccManager
from src.common.manager.logger_manager import LoggerManager
from src.common.manager.module_manager import ModuleManager
from src.common.manager.python_manager import PythonManager

LoggerManager().initialize()  # 初始化日志

# 初始化配置管理器
settings_manager = SettingsManager()
settings_manager.initialize()
pythonexe = settings_manager.get(SettingsManager.PYTHONEXE)
pypi_url = settings_manager.get(SettingsManager.FASTEST_PIP_SOURCE)
gcc_available = settings_manager.get(SettingsManager.GCC_AVAILABLE)

# 初始化 Python 管理器
python_manager = PythonManager()
PythonManager().initialize()
ModuleManager().initialize()  # 初始化第三方库模块
# GccManager().initialize()  # 初始化 GCC 管理器
