import loguru

from src.conf import config_path

LOG_DIR = config_path.LOG_DIR
LOG_FILE = config_path.LOG_FILE


class LoggerManager:
    @staticmethod
    def initialize():
        if not LOG_DIR.exists():
            LOG_DIR.mkdir(parents=True, exist_ok=True)

        loguru.logger.add(LOG_FILE, rotation='10 MB', encoding='utf-8')
        loguru.logger.info(f'日志文件设置: {LOG_FILE}')


if __name__ == '__main__':
    LoggerManager.initialize()
