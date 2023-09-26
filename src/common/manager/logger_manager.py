import loguru

from src.conf import config_path

LOG_DIR = config_path.SRC_HOME.parent / 'logs'


class LoggerManager:
    @staticmethod
    def initialize():
        if not LOG_DIR.exists():
            LOG_DIR.mkdir(parents=True, exist_ok=True)

        loguru.logger.add(LOG_DIR, rotation='10 MB', encoding='utf-8')
        loguru.logger.info(f'日志目录设置: {LOG_DIR}')
