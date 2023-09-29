import subprocess
from pathlib import Path
from typing import List

import loguru

from src.common.manager.runtime_config_manager import RuntimeManager
from src.conf import config


class PythonManager:
    avaliable_python: List[Path] = []

    @staticmethod
    def is_python_available(python_path: Path) -> bool:
        """check current python is available

        Args:
            python_path: the python.exe path

        Returns:
            bool: is current python.exe is avialable
        """
        if isinstance(python_path, str):
            python_path = Path(python_path)

        try:
            output = subprocess.check_output([python_path, "-V"], timeout=3)
        except (TimeoutError, FileNotFoundError, subprocess.CalledProcessError):
            output = b""
        return output.startswith(b"Python 3.")

    def find_available_python_exe_python(self) -> List[Path]:
        """get available python.exe Path

        use `where python` find python.exe and then check is it avialable,then return all available poth

        Returns:
            List[Path]: list of available python.exe path
        """
        system_encoding = config.system_encoding
        result = subprocess.run("where python",
                                shell=True,
                                timeout=5,
                                stdout=subprocess.PIPE,
                                encoding=system_encoding)
        result = result.stdout.splitlines()
        available = []
        for each in result:
            current_python_path = Path(each)
            if self.is_python_available(current_python_path):
                available.append(current_python_path)
                self.avaliable_python.append(current_python_path)
                loguru.logger.debug(f'寻找到可用的 Python: {current_python_path}')
        loguru.logger.debug(f'一共有 {len(available)} 个可用的 Python')
        return available

    @staticmethod
    def get_python_version(python_path: Path) -> str:
        """get python version

        Args:
            python_path: python.exe path

        Returns:
            str: the version of Python like `Python 3.10.11`
        """
        result = subprocess.check_output([python_path, "-V"], timeout=3, encoding=config.system_encoding)
        return result.strip('\r\n')

    def initialize(self):
        """初始化 Python 管理器, 保存可用的 Python 路径到文件中"""
        if not self.avaliable_python:
            self.find_available_python_exe_python()

        if not self.avaliable_python:
            loguru.logger.error('没有找到可用的 Python')
            return

        loguru.logger.debug(f'可用的 Python: {self.avaliable_python}')
        RuntimeManager.set(RuntimeManager.AVAILABLE_PYTHON_LIST,
                           self.avaliable_python)

        if self.avaliable_python:
            RuntimeManager.set(RuntimeManager.SELECTED_PYTHON,
                               self.avaliable_python[0])
            loguru.logger.debug(f'设置默认 Python: {self.avaliable_python[0]}')
