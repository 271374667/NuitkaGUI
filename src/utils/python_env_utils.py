import subprocess
from pathlib import Path
from typing import List, Union

import loguru

from src.utils.singleton import singleton


@singleton
class PythonEnvUtils:
    avaliable_python: List[Path] = []

    def find_available_python_exe_python(self) -> List[Path]:
        """get available python.exe Path

        use `where python` find python.exe and then check is it avialable,then return all available poth

        Returns:
            List[Path]: list of available python.exe path
        """
        result = subprocess.run("where python",
                                shell=True,
                                timeout=5,
                                stdout=subprocess.PIPE,
                                encoding='utf-8')
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
        result = subprocess.check_output([python_path, "-V"], timeout=3, encoding='utf-8')
        return str(result.strip('\r\n'))

    @staticmethod
    def is_python_available(python_path: Union[Path, str]) -> bool:
        """check current python is available

        Args:
            python_path: the python.exe path

        Returns:
            bool: is current python.exe is avialable
        """
        python_path = Path(python_path)

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        try:
            output = subprocess.check_output([python_path, "-V"], timeout=3, startupinfo=startupinfo)
        except Exception:
            output = b""
        return output.startswith(b"Python 3.")


if __name__ == '__main__':
    pm = PythonEnvUtils()
    pm.find_available_python_exe_python()
    print(pm.avaliable_python)
    print(pm.is_python_available(pm.avaliable_python[0]))
    print(pm.get_python_version(pm.avaliable_python[0]))
