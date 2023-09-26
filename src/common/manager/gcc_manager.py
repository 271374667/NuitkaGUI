import subprocess
from zipfile import ZipFile

import loguru

from src.common.download import Download
from src.conf import config
from src.conf import config_path
from src.utils import get_fastest_url


class GccManager:
    def __init__(self):
        self.download_base = Download()

    def download(self) -> None:
        """下载 gcc"""
        fastest_url = get_fastest_url.get_fastest_url([x.value for x in config.GCC])

        if not config_path.GCC_DIR.exists():
            loguru.logger.debug(f'下载目录不存在！创建下载目录: {config_path.GCC_DIR}')
            config_path.GCC_DIR.mkdir(parents=True, exist_ok=True)
        loguru.logger.debug(f'下载链接: {fastest_url}')
        self.download_base.download(fastest_url, config_path.DOWNLOAD_DIR)
        loguru.logger.info(f'GCC 下载完成: {fastest_url}')

    @staticmethod
    def install():
        loguru.logger.info(f'安装 GCC -> {config_path.GCC_DIR}')
        with ZipFile(config_path.DOWNLOAD_DIR / 'w64devkit-1.20.0.zip') as zipf:
            loguru.logger.debug(f'解压文件: {config_path.DOWNLOAD_DIR / "w64devkit-1.20.0.zip"}')
            zipf.extractall(config_path.GCC_DIR)
        gcc_save_path = config_path.GCC_DIR.joinpath("w64devkit").joinpath("bin")
        loguru.logger.info(f'添加环境变量: {gcc_save_path}')
        subprocess.run(f'setx "Path" "%Path%";"{gcc_save_path}" /m', shell=True)
