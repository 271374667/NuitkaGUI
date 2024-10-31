from enum import Enum
from pathlib import Path

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

from src.core.paths import CONFIG_FILE
from src.utils.python_env_utils import PythonEnvUtils

AVAILABLE_PYTHON_EXE_LIST: list[Path] = PythonEnvUtils().find_available_python_exe_python()


class Optimization(Enum):
    Normal = "Normal"
    Compatibility = "Compatibility"
    Speed = "Speed"
    Size = "Size"


class PipSrouce(Enum):
    Default = 'https://pypi.org/simple/'
    QingHua = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    ALiYun = 'https://mirrors.aliyun.com/pypi/simple/'
    ZhongGuoKeJiDaXue = 'https://pypi.mirrors.ustc.edu.cn/simple/'
    DouBan = 'https://pypi.douban.com/simple/'

    @classmethod
    def from_value(cls, value: str):
        for item in cls:
            if item.value == value:
                return item
        return cls.Default


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
        result: list[Path] = AVAILABLE_PYTHON_EXE_LIST
        if result:
            return str(result[0])
        return ''


class Config(QConfig):
    # 全局设置
    is_first_run = ConfigItem("General", "首次运行", True, BoolValidator())
    global_python_exe_path = ConfigItem(
        "General", "可用的Python.exe的路径", '', PythonExeValidator()
    )
    project_python_exe_path = ConfigItem(
        "General", "项目Python.exe的路径", '', PythonExeValidator()
    )
    keep_unsupported_command = ConfigItem("General", "保留不支持的命令", True, BoolValidator())
    auto_update_plugin = ConfigItem("General", "自动更新插件", False, BoolValidator())
    optimization = OptionsConfigItem(
        "General",
        "优化",
        Optimization.Compatibility,
        OptionsValidator(Optimization),
        EnumSerializer(Optimization),
    )
    pip_source = OptionsConfigItem(
        "General",
        "pip源",
        PipSrouce.Default,
        OptionsValidator(PipSrouce),
        EnumSerializer(PipSrouce)
    )


cfg = Config()
cfg.file = CONFIG_FILE
if not CONFIG_FILE.exists():
    cfg.save()
qconfig.load(CONFIG_FILE, cfg)
