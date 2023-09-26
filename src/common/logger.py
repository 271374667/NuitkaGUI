import datetime
import logging
import sys
from pathlib import Path

from src.conf import config

logger = None
LOG_DIR = config.HOME.parent / 'logs'
if not LOG_DIR.exists():
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def initLogger():
    log_path = Path('logs')
    if not log_path.exists():
        log_path.mkdir()
    logger = logging.getLogger("logger")

    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler(filename=f'logs/{datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")}.txt',
                                   encoding="utf-8", mode="w")
    logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.DEBUG)
    handler2.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
            "%(levelname)s - %(filename)s - %(lineno)d - %(asctime)s - %(message)s")
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    sys.stderr = handler2.stream
    sys.stdout = handler2.stream

    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.setLevel(logging.DEBUG)

    return logger


# 检测日志文件夹内的日志文件数量，如果超过10个就删除最早的一个
def deleteLog10More():
    log_path = Path('logs')
    if not log_path.exists():
        log_path.mkdir()
    log_list = list(log_path.glob('*.txt'))
    if len(log_list) > 10:
        log_list.sort(key=lambda x: x.stat().st_mtime)
        log_list[0].unlink()


def get_logger() -> logging.Logger:
    global logger
    if logger is None:
        logger = initLogger()
        return logger
    return logger
