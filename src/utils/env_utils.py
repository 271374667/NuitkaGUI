import os
from tkinter import N
import winreg
from pathlib import Path
from shutil import which
from typing import Optional

import loguru


class EnvUtils:
    def __init__(self):
        self._writeable_env_path_list: list[Path] = self.get_writeable_env()

    def get_writeable_env(self) -> list[Path]:
        """获取所有有写入权限的环境变量PATH中的路径"""
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            current_path = winreg.QueryValueEx(key, "PATH")[0]
        paths = current_path.split(";")
        result = [Path(p) for p in paths if os.access(p, os.W_OK)]
        loguru.logger.debug(f"获取到的可写入的环境变量路径: {result}")
        return result

    def add_path_to_user_env_by_os(self, dir_path: Path) -> None:
        """使用os模块将路径添加到用户环境变量

        使用该方法添加的环境变量只在当前进程中有效, 程序结束后失效
        """
        os.environ["PATH"] = f"{dir_path};{os.environ['PATH']}"
        loguru.logger.debug(f"向用户环境变量中添加了路径: {dir_path}")

    def append_path_to_user_env_by_os(self, dir_path: Path, var_name: str) -> None:
        """使用os模块将路径追加到已有的用户环境变量
        Args:
            dir_path: 要追加的路径
            var_name: 被追加的环境变量名
        """
        os.environ[var_name] = f"{os.environ.get(var_name, '')};{dir_path}"
        loguru.logger.debug(f"向用户环境变量中追加了路径: {dir_path}")

    def remove_path_from_user_env_by_os(self, dir_path: Path) -> None:
        """使用os模块将路径从用户环境变量中移除"""
        paths = os.environ["PATH"].split(";")
        paths = [p for p in paths if p != str(dir_path)]
        os.environ["PATH"] = ";".join(paths)
        loguru.logger.debug(f"从用户环境变量中移除了路径: {dir_path}")

    def add_file_path_to_user_env_by_bat(
        self, file_path: Path, target_dir_path: Optional[Path] = None
    ) -> Path:
        """使用注册表将路径添加到用户环境变量

        使用该方法添加的环境变量永久有效
        """
        writeable_env_path = (
            self._writeable_env_path_list[0] if self._writeable_env_path_list else None
        )
        if writeable_env_path is None:
            raise ValueError(
                f"写入地址必须是一个合法的地址，当前为: {writeable_env_path}"
            )
        target_dir_path = (
            writeable_env_path if target_dir_path is None else target_dir_path
        )
        bat_path = target_dir_path / f"{file_path.stem}.bat"
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(self._get_bat_cmd(str(file_path.resolve())))
        loguru.logger.debug(f"向用户环境变量中添加了bat文件: {bat_path}")
        return bat_path

    def is_exe_in_env(self, exe_name: str) -> bool:
        """判断exe是否在环境变量中"""
        return which(exe_name) is not None

    def _get_bat_cmd(self, app_name: str) -> str:
        """
        使用bat可以将一个小的bat添加进已有的环境变量中,
        从而实现在任何地方都可以调用该程序,而不需要在程序所在的目录下调用
        """
        content: list[str] = [
            "@echo off",
            "chcp 65001",
            f'"{app_name}" %*',
        ]
        return "\n".join(content)


if __name__ == "__main__":
    from src.core.paths import GCC_EXE_FILE

    env_uitls = EnvUtils()
    # paths = env_uitls.get_writeable_env()
    # print(paths)
    env_uitls.add_file_path_to_user_env_by_bat(GCC_EXE_FILE)
    # print(env_uitls.is_exe_in_env("gcc"))
