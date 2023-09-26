import os
import sys
from pathlib import Path


class SystemManager:

    def __init__(self):
        self.system_encoding = sys.getfilesystemencoding()

    @staticmethod
    def get_system_save_path() -> Path:
        """
        get a Path to save userdata
        Returns:
            Path: save path
        """

        system_path_dict = os.environ.keys()
        if 'TMP' in system_path_dict:
            return Path(os.environ['TMP'].split(';')[0])
        elif 'TEMP' in system_path_dict:
            return Path(os.environ['TEMP'].split(';')[0])
        else:
            return Path.home()

    @staticmethod
    def check_platform_window() -> bool:
        """
        check current platform is window, if is not, raise Error
        Returns:
            Bool: is platform window
        Raises:
            if current platform is not window
        """
        current_platform = sys.platform
        if current_platform.startswith('win32'):
            return True
        raise SystemError("nuitkaGUI must run in Windows platform")
