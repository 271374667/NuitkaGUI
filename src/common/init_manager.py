from src.common.manager.gcc_manager import GccManager
from src.common.manager.logger_manager import LoggerManager
from src.common.manager.module_manager import ModuleManager
from src.common.manager.python_manager import PythonManager

LoggerManager().initialize()  # 初始化日志
PythonManager().initialize()  # 初始化 Python 管理器
ModuleManager().initialize()  # 初始化第三方库模块
GccManager().initialize()  # 初始化 GCC 管理器
