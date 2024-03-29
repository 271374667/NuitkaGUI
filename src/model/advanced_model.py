from typing import Union

from src.common.manager.command_manager import CommandManager
from src.core import BoolCommands, IntCommands, StrCommands


class AdvancedModel:
    def __init__(self):
        self.command_manager = CommandManager()

    def set_default_options_status(self, status: bool) -> None:
        self.command_manager.set_option_value(BoolCommands.lto_no, status)
        self.command_manager.set_option_value(BoolCommands.remove_output, status)
        self.command_manager.set_option_value(BoolCommands.show_progress, status)

    def set_option_value(self, option_name: Union[IntCommands, StrCommands, BoolCommands],
                         value: Union[int, str, bool]) -> None:
        self.command_manager.set_option_value(option_name, value)

    def get_option_value(self, command_enum: Union[IntCommands, StrCommands, BoolCommands]) -> bool:
        return self.command_manager.get_option_value(command_enum)

    def add_command(self, command: Union[str, list]) -> None:
        self.command_manager.add_command(command)

    def remove_command(self, command: Union[str, list]) -> None:
        self.command_manager.remove_command(command)
