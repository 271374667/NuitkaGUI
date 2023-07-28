import logging
import datetime
from pathlib import Path

def initLogger():
    logger = logging.getLogger("logger")

    handler1 = logging.StreamHandler()
    handler2 = logging.FileHandler(filename=f'logs/{datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")}.txt', encoding="utf-8", mode="w")
    logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.DEBUG)
    handler2.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(levelname)s - %(lineno)d - %(asctime)s - %(message)s")
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.setLevel(logging.DEBUG)

    return logger

# 检测日志文件夹内的日志文件数量，如果超过10个就删除最早的一个
def deleteLog10More():
    logPath = Path('log')
    if not logPath.exists():
        logPath.mkdir()
    logList = list(logPath.glob('*.txt'))
    if len(logList) > 10:
        logList.sort(key=lambda x: x.stat().st_mtime)
        logList[0].unlink()
