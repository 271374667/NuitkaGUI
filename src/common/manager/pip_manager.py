import subprocess
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

import loguru

from src.common.nuitka_command.command_manager import CommandManager


class PipManager:
    def __init__(self):
        self.install_module: list[str] = ['nuitka', 'PyQt5', 'PyQt5-stubs', 'loguru']
        self._command_manager = CommandManager()
        self._pool = ThreadPoolExecutor()

    def is_module_installed(self, module_name_list: list[str]) -> dict[str, bool]:
        """判断给定的模块是否已安装"""
        loguru.logger.debug(f'判断模块是否已安装: {module_name_list}')
        result: dict[str, bool] = {}

        def check_module(module_name: str) -> tuple[str, bool]:
            # command = [str(self._command_manager.python_exe_path), '-m', 'pip', 'show', module_name]
            command = ['pip', 'show', module_name]
            output = subprocess.run(command, capture_output=True, text=True)
            return module_name, output.returncode == 0

        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(check_module, module_name): module_name for module_name in module_name_list}
            for future in futures:
                module_name, is_installed = future.result()
                result[module_name] = is_installed

        loguru.logger.debug(f'模块是否已安装的结果: {result}')
        return result

    def install_module(self, module_list: list[str]):
        """安装模块"""
        loguru.logger.debug(f'安装模块: {module_list}')

        def install(module: str):
            command = ['pip', 'install', module]
            output = subprocess.run(command, capture_output=True, text=True)
            loguru.logger.debug(f'安装模块: {module}, 结果: {output}')

        with ThreadPoolExecutor() as executor:
            executor.map(install, module_list)

        loguru.logger.debug(f'安装模块完成')

    def get_fastest_url(self, url_list: list[str]) -> Optional[str]:
        loguru.logger.debug(f'正在获取最快的链接: {url_list}')

        def test_speed(url):
            try:
                start_time = time.time()
                with urllib.request.urlopen(url, timeout=3) as response:
                    response.read()
                return url, time.time() - start_time
            except Exception:
                return url, float('inf')

        with ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(test_speed, url): url for url in url_list}
            for future in as_completed(future_to_url):
                url, response_time = future.result()
                if response_time != float('inf'):
                    loguru.logger.debug(f'最快的链接: {url}')
                    return url
        return None


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from src.config import PipSrouce

    app = QApplication([])
    pip_manager = PipManager()
    print(pip_manager.is_module_installed(pip_manager.install_module))
    print(pip_manager.get_fastest_url([i.value for i in PipSrouce]))
    app.exec()
