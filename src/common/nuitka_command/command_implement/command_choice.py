from enum import Enum

from src.common.nuitka_command.command import CommandChoiceBase


class CommandWindowsDisableConsole(CommandChoiceBase):
    name: str = "打包后禁用控制台"
    description: str = (
        "force: 强制禁用控制台; disable: 禁用控制台; attach: 打包后附加到控制台"
    )
    command: str = "windows-disable-console"

    _value: str = "force"

    class Choice(Enum):
        DoNothing = ""
        Force = "force"
        Disable = "disable"
        Attach = "attach"
