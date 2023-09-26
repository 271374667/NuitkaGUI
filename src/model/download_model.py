import subprocess
import sys
from pathlib import Path

from PySide6.QtCore import QThread, Signal

from src.common import logger as lg

logger = lg.get_logger()


class DownloadModel(QThread):
    isFinished = Signal(bool)
    """
    Methods:
        download(url:str) -> Path: absoult Path
    """

    def download(self, url: str, target_dir: Path) -> None:
        """使用 aria2 下载文件
        Args:
            url: 下载链接
            target_dir: 下载目录
        """
        logger.debug(f'下载链接: {url}')
        if not target_dir.exists():
            logger.debug(f'创建下载目录: {target_dir}')
            target_dir.mkdir(parents=True, exist_ok=True)

        args_list = [Path('./aria2c.exe'), url, '-d', target_dir]
        logger.debug(f'执行命令: {args_list}')
        subprocess.run(args_list,
                       stdin=sys.stdin,
                       stderr=sys.stderr,
                       stdout=sys.stdout,
                       encoding='gbk')
        logger.debug(f'下载完成: {url}')
        self.isFinished.emit(True)
