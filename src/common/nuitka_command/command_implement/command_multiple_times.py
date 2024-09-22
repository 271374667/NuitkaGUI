from src.common.nuitka_command.command import CommandMultipleTimesBase


class CommandIncludeDataDir(CommandMultipleTimesBase):
    name: str = "包含数据目录"
    description: str = "指定要包含数据文件的目录"
    command: str = "include-data-dir"


class CommandIncludeDataFiles(CommandMultipleTimesBase):
    name: str = "包含数据文件"
    description: str = "指定要包含的数据文件"
    command: str = "include-data-files"


class CommandIncludePackage(CommandMultipleTimesBase):
    name: str = "包含包"
    description: str = "指定要包含的包"
    command: str = "include-package"


class CommandNofollowImportTo(CommandMultipleTimesBase):
    name: str = "不跟随导入"
    description: str = "指定不跟随导入的模块"
    command: str = "nofollow-import-to"
