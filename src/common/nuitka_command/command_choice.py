from enum import Enum

from src.common.nuitka_command.command import CommandChoiceBase


class CommandWindowsDisableConsole(CommandChoiceBase):
    command: str = 'windows-disable-console'
    _value: str = 'force'

    class Choice(Enum):
        Force = 'force'
        Disable = 'disable'
        Attach = 'attach'