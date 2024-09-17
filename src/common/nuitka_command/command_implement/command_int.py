from src.common.nuitka_command.command import CommandIntBase


class CommandJobs(CommandIntBase):
    command: str = 'jobs'
    name: str = 'jobs'
    description: str = '编译时使用的并行工作数'
    _value: int = -1
