import json
from pathlib import Path

import loguru

from src.core.paths import CCACHE_DEPENDENCE_FILE, DEPENDS_DLL_DEPENDENCE_FILE, DEPENDS_EXE_DEPENDENCE_FILE, \
    UPX_DEPENDENCE_FILE, GCC_EXE_FILE, DEPENDENCE_SAVE_PATH_FILE, CLANG_EXE_FILE
from src.utils.env_utils import EnvUtils


class EnvManager:
    def __init__(self):
        self._dependence_list: list[Path] = [
            CCACHE_DEPENDENCE_FILE,
            DEPENDS_DLL_DEPENDENCE_FILE,
            DEPENDS_EXE_DEPENDENCE_FILE,
            UPX_DEPENDENCE_FILE,
            GCC_EXE_FILE,
            CLANG_EXE_FILE
        ]
        self._save_path_dict: dict[str, str] = {}
        self._env_utils = EnvUtils()

    def add_dependence_to_env_by_bat(self) -> None:
        for each in self._dependence_list:
            if not self._env_utils.is_exe_in_env(each.stem):
                bat_path: Path = self._env_utils.add_file_path_to_user_env_by_bat(each)
                self._save_path_dict[each.stem] = str(bat_path)
                loguru.logger.info(f"向系统环境添加了依赖: {each}")
        self._save_dependence_save_path()

    def add_dependence_to_env_by_os(self) -> None:
        for each in self._dependence_list:
            if not self._env_utils.is_exe_in_env(each.stem):
                self._env_utils.add_path_to_user_env_by_os(each)

    def remove_bat_dependence_from_env(self) -> None:
        self._load_dependence_save_path()

        for key, value in self._save_path_dict:
            if self._env_utils.is_exe_in_env(key):
                Path(value).unlink(missing_ok=True)
                loguru.logger.info(f"从系统环境移除了依赖: {key},路径: {value}")

    def is_all_dependence_in_env(self) -> bool:
        for each in self._dependence_list:
            if not self._env_utils.is_exe_in_env(each.stem):
                loguru.logger.error(f"依赖 {each} 不在系统环境中")
                return False
        return True

    def _load_dependence_save_path(self) -> None:
        if DEPENDENCE_SAVE_PATH_FILE.exists():
            json.loads(DEPENDENCE_SAVE_PATH_FILE.read_text(encoding="utf-8"))

    def _save_dependence_save_path(self) -> None:
        if not self._save_path_dict:
            return

        DEPENDENCE_SAVE_PATH_FILE.write_text(json.dumps(self._save_path_dict,
                                                        ensure_ascii=False,
                                                        indent=4),
                                             encoding="utf-8")


if __name__ == '__main__':
    env_manager = EnvManager()
    env_manager.remove_bat_dependence_from_env()
    # env_manager.is_all_dependence_in_env()
