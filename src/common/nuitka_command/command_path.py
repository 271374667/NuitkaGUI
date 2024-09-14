from src.common.nuitka_command.command import CommandPathBase


class CommandOutputDir(CommandPathBase):
    command: str = 'output-dir'


class CommandMain(CommandPathBase):
    command: str = 'main'


class CommandWindowsIconFromIco(CommandPathBase):
    command: str = 'windows-icon-from-ico'
