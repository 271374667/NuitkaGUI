from src.common.manager.command_manager import CommandManager
from src.common.manager.plugin_manager import PluginManager
from src.common.manager.process_manager import ProcessManager
from src.core import BoolCommands, StrCommands


class BasicModel:
    def __init__(self):
        self.command_manager: CommandManager = CommandManager()
        self.plugin_manager: PluginManager = PluginManager()
        self.process_manager: ProcessManager = ProcessManager()

    def get_py_file(self) -> str:
        return self.command_manager.get_option_value(StrCommands.main)

    def set_py_file(self, py_file: str) -> None:
        self.command_manager.set_option_value(StrCommands.main, py_file)

    def set_output_dir(self, output_path: str) -> None:
        self.command_manager.set_option_value(StrCommands.output_dir, output_path)

    def get_icon(self) -> str:
        return self.command_manager.get_option_value(StrCommands.windows_icon_from_ico)

    def set_icon(self, icon: str) -> None:
        self.command_manager.set_option_value(StrCommands.windows_icon_from_ico, icon)

    def set_onefile_mode(self, mode: bool) -> None:
        self.command_manager.set_option_value(BoolCommands.onefile, mode)

    def start(self) -> None:
        print(self.command_manager.get_cmd())
        # self.process_manager.new_window_run(self.command_manager.get_cmd())
