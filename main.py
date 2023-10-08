from src.common.manager.logger_manager import LoggerManager
from src.common.manager.settings_manager import SettingsManager

LoggerManager().initialize()  # 初始化日志

# 初始化配置管理器
settings_manager = SettingsManager()
settings_manager.initialize()
