import subprocess
from pathlib import Path
from typing import List

from src.conf import config


class PythonModel:
    """
    TODO:
        [x] check current python is available
        [x] get the available pyhton.exe path
        [x] get current python version
    """

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
        # TODO: add loguru here
        result = result.stdout.splitlines()
        available_python = []
        for each in result:
            current_python_path = Path(each)
            if self.is_python_available(current_python_path):
                available_python.append(current_python_path)
        return available_python

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
