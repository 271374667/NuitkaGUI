from src.common.nuitka_command.command import CommandBoolBase


class CommandOneFile(CommandBoolBase):
    command: str = 'onefile'


class CommandStandAlone(CommandBoolBase):
    command: str = 'standalone'


class CommandShowProgress(CommandBoolBase):
    command: str = 'show-progress'


class CommandShowMemory(CommandBoolBase):
    command: str = 'show-memory'


class CommandRemoveOutput(CommandBoolBase):
    command: str = 'remove-output'


class CommandLowMemory(CommandBoolBase):
    command: str = 'low-memory'


class CommandWindowsDisableConsole(CommandBoolBase):
    command: str = 'windows-disable-console'


class CommandMingw64(CommandBoolBase):
    command: str = 'mingw64'


class CommandQuiet(CommandBoolBase):
    command: str = 'quiet'


class CommandLtoNo(CommandBoolBase):
    command: str = 'lto=no'


class CommandDisableCcache(CommandBoolBase):
    command: str = 'disable-ccache'


class CommandAssumeYesForDownloads(CommandBoolBase):
    command: str = 'assume-yes-for-downloads'


class CommandClang(CommandBoolBase):
    command: str = 'clang'


class CommandWindowsUacAdmin(CommandBoolBase):
    command: str = 'windows-uac-admin'


class CommandCleanCache(CommandBoolBase):
    command: str = 'clean-cache'
