import socket
import subprocess
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import loguru

from src.common.nuitka_command.command_manager import CommandManager
from src.config import cfg
from src.core.settings import INSTALL_PACKAGE


class PipManager:
    def __init__(self):
        self.install_module: list[str] = INSTALL_PACKAGE
        self._command_manager = CommandManager()
        self._pool = ThreadPoolExecutor()

    def is_module_installed(self, module_name_list: list[str]) -> dict[str, bool]:
        """判断给定的模块是否已安装"""
        loguru.logger.debug(f"判断模块是否已安装: {module_name_list}")
        result: dict[str, bool] = {}

        def check_module(module_name: str) -> tuple[str, bool]:
            # command = [str(self._command_manager.python_exe_path), '-m', 'pip', 'show', module_name]
            command = ["pip", "show", module_name]
            output = subprocess.run(command, capture_output=True, text=True)
            return module_name, output.returncode == 0

        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(check_module, module_name): module_name
                for module_name in module_name_list
            }
            for future in futures:
                module_name, is_installed = future.result()
                result[module_name] = is_installed

        loguru.logger.debug(f"模块是否已安装的结果: {result}")
        return result

    def install(self, module_list: list[str]):
        """安装模块"""
        loguru.logger.debug(f"安装模块: {module_list}")

        def install(module: str):
            command = ["pip", "install", module]
            output = subprocess.run(command, capture_output=True, text=True)
            loguru.logger.debug(f"安装模块: {module}, 结果: {output}")

        with ThreadPoolExecutor() as executor:
            executor.map(install, module_list)

        loguru.logger.debug("安装模块完成")

    def get_fastest_url(self, url_list: list[str]) -> Optional[str]:
        loguru.logger.debug(f"正在获取最快的链接: {url_list}")

        def test_speed(url: str) -> tuple[str, float]:
            host = urllib.parse.urlparse(url).hostname
            port = 80  # 默认 HTTP 端口
            start_time = time.time()
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)  # 设置超时时间
                sock.connect((host, port))
                sock.close()
                response_time = time.time() - start_time
                return url, response_time
            except Exception as e:
                loguru.logger.error(f"连接 {url} 失败: {e}")
                return url, float("inf")

        with ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(test_speed, url): url for url in url_list}
            results = []
            for future in as_completed(future_to_url):
                url, response_time = future.result()
                results.append((url, response_time))

        # 按响应时间排序
        results.sort(key=lambda x: x[1])
        fastest_url = results[0][0] if results else None

        loguru.logger.debug(f"最快的链接: {fastest_url}")
        return fastest_url

    def install_package(self, package: str) -> bool:
        python_exe_path: Path = self._command_manager.python_exe_path
        pip_source: PipSrouce = cfg.get(cfg.pip_source)
        commands = [
            [str(python_exe_path), "pip", "install", package, '-U', '-i', pip_source.value],
            ["pip", "install", package, '-U', '-i', pip_source.value],
            ["pip3", "install", package, '-U', '-i', pip_source.value]
        ]

        for command in commands:
            loguru.logger.debug(f"安装包: {package}, 命令: {command}")
            output = subprocess.run(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
            if output.returncode == 0:
                loguru.logger.debug(f"安装包: {package}, 结果: {output}")
                return True

        loguru.logger.error(f"安装包: {package}安装错误")
        return False


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    from src.config import PipSrouce

    app = QApplication([])
    pip_manager = PipManager()
    # pip_manager.install_module = ['nuitka', 'PyQt5', 'PyQt5-stubs', 'loguru']
    # print(pip_manager.is_module_installed(pip_manager.install_module))
    print(pip_manager.get_fastest_url([i.value for i in PipSrouce]))
    app.exec()
