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

    def download(self):
        """下载 gcc"""
        loguru.logger.info('开始下载 GCC')
        fastest_url = get_fastest_url.get_fastest_url([x.value for x in config.GCC])

        if not config_path.GCC_DIR.exists():
            loguru.logger.debug(f'下载目录不存在！创建下载目录: {config_path.GCC_DIR}')
            config_path.GCC_DIR.mkdir(parents=True, exist_ok=True)
        loguru.logger.debug(f'下载链接: {fastest_url}')
        self.download_base.download(fastest_url, config_path.DOWNLOAD_DIR)
        loguru.logger.info(f'GCC 下载完成: {fastest_url}')

    @staticmethod
    def install():  # sourcery skip: use-named-expression
        loguru.logger.info(f'安装 GCC -> {config_path.GCC_DIR}')
        with ZipFile(config_path.DOWNLOAD_DIR / 'w64devkit-1.20.0.zip') as zipf:
            loguru.logger.debug(f'解压文件: {config_path.DOWNLOAD_DIR / "w64devkit-1.20.0.zip"}')
            zipf.extractall(config_path.GCC_DIR)
        gcc_save_path = config_path.GCC_DIR.joinpath("w64devkit").joinpath("bin")

        loguru.logger.info(f'添加环境变量: {gcc_save_path}')
        result = subprocess.check_output(f'setx "Path" "%Path%";"{gcc_save_path}" /m', shell=True)
        if result:
            loguru.logger.info('GCC 环境变量已添加')
            return
        loguru.logger.error('GCC 环境变量添加失败')

    @staticmethod
    def is_gcc_available() -> bool:
        try:
            output = subprocess.check_output(['gcc', "--version"], timeout=5)
        except Exception:
            output = b""
        return output.startswith(b"gcc") if output else False

    def initialize(self):
        if GccManager.is_gcc_available():
            loguru.logger.debug('GCC 已安装，跳过安装')
            return

        self.download()
        self.install()
        loguru.logger.debug('GCC 初始化完成!')


if __name__ == '__main__':
    print(GccManager.is_gcc_available())
