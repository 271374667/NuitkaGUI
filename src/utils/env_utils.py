import os
import winreg
from pathlib import Path


class EnvUtils:
    def get_writeable_env(self) -> list[Path]:
        """获取所有有写入权限的环境变量PATH中的路径"""
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            current_path = winreg.QueryValueEx(key, "PATH")[0]
        paths = current_path.split(";")
        return [Path(p) for p in paths if os.access(p, os.W_OK)]

    def add_path_to_user_env_by_os(self, dir_path: Path) -> None:
        """使用os模块将路径添加到用户环境变量

        使用该方法添加的环境变量只在当前进程中有效, 程序结束后失效
        """
        os.environ["PATH"] = f"{dir_path};{os.environ['PATH']}"

    def add_path_to_user_env_by_bat(self, dir_path: Path) -> None:
        """使用注册表将路径添加到用户环境变量

        使用该方法添加的环境变量永久有效
        """
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
            current_path = winreg.QueryValueEx(key, "PATH")[0]
            new_path = f"{dir_path};{current_path}"
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)

    def append_path_to_user_env_by_os(self, dir_path: Path, var_name: str) -> None:
        """使用os模块将路径追加到已有的用户环境变量
        Args:
            dir_path: 要追加的路径
            var_name: 被追加的环境变量名
        """
        os.environ[var_name] = f"{os.environ.get(var_name, '')};{dir_path}"

    def append_path_to_user_env_by_bat(self, dir_path: Path, var_name: str) -> None:
        """使用注册表将路径追加到已有的用户环境变量
        Args:
            dir_path: 要追加的路径
            var_name: 被追加的环境变量名
        """
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
            current_value = winreg.QueryValueEx(key, var_name)[0]
            new_value = f"{current_value};{dir_path}"
            winreg.SetValueEx(key, var_name, 0, winreg.REG_EXPAND_SZ, new_value)

    def remove_path_from_user_env_by_os(self, dir_path: Path) -> None:
        """使用os模块将路径从用户环境变量中移除"""
        paths = os.environ["PATH"].split(";")
        paths = [p for p in paths if p != str(dir_path)]
        os.environ["PATH"] = ";".join(paths)

    def remove_path_from_user_env_by_bat(self, dir_path: Path) -> None:
        """使用注册表将路径从用户环境变量中移除"""
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
            current_path = winreg.QueryValueEx(key, "PATH")[0]
            paths = current_path.split(";")
            paths = [p for p in paths if p != str(dir_path)]
            new_path = ";".join(paths)
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)

    def _get_bat_cmd(self, app_name: str) -> str:
        """
        使用bat可以将一个小的bat添加进已有的环境变量中,
        从而实现在任何地方都可以调用该程序,而不需要在程序所在的目录下调用
        """
        content: list[str] = [
            '@echo off',
            'chcp 65001',
            f'"{app_name}" %*',
            'exit'
        ]
        return '\n'.join(content)

if __name__ == '__main__':
    env_uitls = EnvUtils()
    paths = env_uitls.get_writeable_env()
    print(paths)