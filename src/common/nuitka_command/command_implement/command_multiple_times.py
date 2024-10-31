from src.common.nuitka_command.command import CommandMultipleTimesBase


class CommandIncludeDataDir(CommandMultipleTimesBase):
    _value: list[str] = []

    name: str = "包含数据目录"
    description: str = "指定要包含数据文件的目录"
    command: str = "include-data-dir"


class CommandIncludeDataFiles(CommandMultipleTimesBase):
    _value: list[str] = []

    name: str = "包含数据文件"
    description: str = "指定要包含的数据文件"
    command: str = "include-data-files"


class CommandIncludePackage(CommandMultipleTimesBase):
    _value: list[str] = []

    name: str = "包含包"
    description: str = "指定要包含的包"
    command: str = "include-package"


class CommandNofollowImportTo(CommandMultipleTimesBase):
    _value: list[str] = []

    name: str = "不跟随导入"
    description: str = "指定不跟随导入的模块"
    command: str = "nofollow-import-to"


class CommandEnablePlugins(CommandMultipleTimesBase):
    _value: list[str] = []

    name = "启用插件"
    description = "启用nuitka的插件"
    command = "enable-plugins"
