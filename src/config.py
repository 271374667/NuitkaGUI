import locale
import sys
from pathlib import Path

import loguru
from qfluentwidgets import (
    BoolValidator,
    ConfigItem,
    QConfig,
    qconfig,
    ConfigValidator,
    EnumSerializer,
    OptionsValidator,
    OptionsConfigItem
)

from enum import Enum
from src.core.paths import CONFIG_FILE
from src.utils.python_env_utils import PythonEnvUtils

if sys.getdefaultencoding() != "utf-8":
    import importlib

    importlib.reload(sys)
    loguru.logger.debug(
        f"系统默认编码: {sys.getdefaultencoding()}, 已经重新加载为UTF-8"
    )

# # 确保环境变量LANG设置为UTF-8
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


class Optimization(Enum):
    Disable = "Disable"
    Compatibility = "Compatibility"
    Speed = "Speed"
    Size = "Size"


class PythonExeValidator(ConfigValidator):
    """Config validator"""

    def validate(self, value):
        """Verify whether the value is legal"""
        python_exe_path: Path = Path(value)
        return PythonEnvUtils().is_python_available(python_exe_path)

    def correct(self, value):
        """correct illegal value"""
        python_exe_path: Path = Path(value)
        if PythonEnvUtils().is_python_available(python_exe_path):
            return value
        return str(sys.executable)


class Config(QConfig):
    # 全局设置
    is_first_run = ConfigItem("General", "首次运行", True, BoolValidator())
    global_python_exe_path = ConfigItem(
        "General", "可用的Python.exe的路径", str(sys.executable), PythonExeValidator()
    )
    project_python_exe_path = ConfigItem(
        "General", "项目Python.exe的路径", str(sys.executable), PythonExeValidator()
    )
    optimization = OptionsConfigItem(
        "General",
        "优化",
        Optimization.Compatibility,
        OptionsValidator(Optimization),
        EnumSerializer(Optimization),
    )


cfg = Config()
cfg.file = CONFIG_FILE
if not CONFIG_FILE.exists():
    cfg.save()
qconfig.load(CONFIG_FILE, cfg)
