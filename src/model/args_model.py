from src.common.nuitka_command.command_manager import CommandManager


class ArgsModel:
    def __init__(self):
        self._command_manager: CommandManager = CommandManager()

    def get_command(self) -> str:
        return self._command_manager.current_command

    def parse_command(self, command: str) -> None:
        self._command_manager.parse_command(command)
