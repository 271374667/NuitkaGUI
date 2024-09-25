from src.common.nuitka_command.command import CommandPathBase
from src.core.paths import LOGO_FILE


class CommandOutputDir(CommandPathBase):
    name: str = "输出目录"
    description: str = "指定输出目录"
    command: str = "output-dir"


class CommandMain(CommandPathBase):
    name: str = "主文件"
    description: str = "指定主文件"
    command: str = "main"


class CommandWindowsIconFromIco(CommandPathBase):
    _value = str(LOGO_FILE)
    name: str = "Windows图标"
    description: str = "指定Windows图标"
    command: str = "windows-icon-from-ico"
