from contextlib import suppress

from src.common.nuitka_command.command_manager import CommandManager
from src.core.settings import DEFAULT_OPTIMIZATION_OPTIONS


class MainModel:
    def __init__(self):
        self._command_manager = CommandManager()

    @property
    def command_manager(self) -> CommandManager:
        return self._command_manager

    def normal_optimization(self):
        for i in DEFAULT_OPTIMIZATION_OPTIONS["Normal"]:
            with suppress(AttributeError):
                self._command_manager.get_command_by_command(i).value = True

    def compatibility_optimization(self):
        for i in DEFAULT_OPTIMIZATION_OPTIONS["Compatibility"]:
            with suppress(AttributeError):
                self._command_manager.get_command_by_command(i).value = True

    def speed_optimization(self):
        for i in DEFAULT_OPTIMIZATION_OPTIONS["Speed"]:
            with suppress(AttributeError):
                self._command_manager.get_command_by_command(i).value = True

    def size_optimization(self):
        for i in DEFAULT_OPTIMIZATION_OPTIONS["Size"]:
            with suppress(AttributeError):
                self._command_manager.get_command_by_command(i).value = True

        # 开启UPX插件
        self._command_manager.manager_plugin.set_plugin_enable("upx", True)

    def update_all_widget(self):
        self._command_manager.update_widget()
