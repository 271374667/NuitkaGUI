from src.common.nuitka_command.command import CommandMultipleTimesBase


class CommandIncludeDataDir(CommandMultipleTimesBase):
    command: str = 'include-data-dir'


class CommandIncludeDataFiles(CommandMultipleTimesBase):
    command: str = 'include-data-files'


class CommandIncludePackage(CommandMultipleTimesBase):
    command: str = 'include-package'


class CommandNofollowImportTo(CommandMultipleTimesBase):
    command: str = 'nofollow-import-to'
