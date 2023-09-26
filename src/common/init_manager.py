from src.common.manager.logger_manager import LoggerManager
from src.common.manager.python_manager import PythonManager

# 初始化日志
LoggerManager.initialize()

# 初始化 Python 管理器
python_manager = PythonManager().initialize()
