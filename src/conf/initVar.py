from utils import log
from core import globalVar

def initLogger():
    # 初始化日志记录器
    globalVar.logger = log.initLogger()
    globalVar.logger.info('日志记录器初始化完成')

    # 清除日志文件
    log.deleteLog10More()
    