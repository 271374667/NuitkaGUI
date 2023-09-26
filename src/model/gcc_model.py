import subprocess
from zipfile import ZipFile

from src.common import logger as lg
from src.conf import config
from src.model.download_model import DownloadModel
from src.utils import get_fastest_url

import loguru



class GccModel:
    def __init__(self):
        self.download_model = DownloadModel()

    def download(self) -> None:
        """下载 gcc"""
        fastest_url = get_fastest_url.get_fastest_url([x.value for x in config.GCC])

        if not config.GCC_DIR.exists():
            loguru.logger.debug(f'下载目录不存在！创建下载目录: {config.GCC_DIR}')
            config.GCC_DIR.mkdir(parents=True, exist_ok=True)
        loguru.logger.debug(f'下载链接: {fastest_url}')
        self.download_model.download(fastest_url, config.DOWNLOAD_DIR)
        loguru.logger.info(f'GCC 下载完成: {fastest_url}')

    @staticmethod
    def install():
        loguru.logger.info(f'安装 GCC -> {config.GCC_DIR}')
        with ZipFile(config.DOWNLOAD_DIR / 'w64devkit-1.20.0.zip') as zipf:
            logger.debug(f'解压文件: {config.DOWNLOAD_DIR / "w64devkit-1.20.0.zip"}')
            zipf.extractall(config.GCC_DIR)
        gcc_save_path = config.GCC_DIR.joinpath("w64devkit").joinpath("bin")
        loguru.logger.info(f'添加环境变量: {gcc_save_path}')
        subprocess.run(f'setx "Path" "%Path%";"{gcc_save_path}" /m', shell=True)
