from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget
from src.utils.plugin_register import PluginRegister
from src.core.paths import COMMAND_IMPLEMENT_DIR

from src.common.nuitka_command.command import CommandBase
from typing import Type, Optional, TypeVar, Generic
from src.utils.class_utils import ClassUtils

T = TypeVar('T', bound='CommandBase')

class ManagerBase(ABC, Generic[T]):
    gourp_name: str = ""  # 管理器对应的组名(会显示在UI上)
    visible: bool = True  # 管理器是否可见
    layout_weight: int = 0  # 管理器在UI中占的比例
    command_type: Type[CommandBase] = CommandBase  # 管理器对应的命令类型
    _command_list: list[CommandBase] = []  # 管理器对应的命令列表

    def __new__(cls, *args, **kwargs):
        # 单例
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._command_list = PluginRegister.load_plugins(
            COMMAND_IMPLEMENT_DIR, self.command_type
        )

    @property
    def command_list(self) -> list[CommandBase]:
        return self._command_list

    @command_list.setter
    def command_list(self, command_list: list[CommandBase]):
        self._command_list = command_list

    @property
    def enabled_command_list(self) -> list[CommandBase]:
        return [command for command in self._command_list if command.enabled]

    def update_widget(self):
        """用于更新管理器对应的UI组件"""
        for command in self._command_list:
            command.update_widget()

    @abstractmethod
    def create_widget(self) -> QWidget:
        """用于创建管理器对应的UI组件"""
        raise NotImplementedError("create_widget method must be implemented")

    def get_command_by_type(
        self, command_type: Type[T]
    ) -> Optional[T]:
        """通过类型获取命令"""
        for each in self.command_list:
            if ClassUtils.is_the_same_class(each.__class__, command_type):
                return each # type: ignore
        return None

    def get_command_by_name(self, command_name: str) -> Optional[T]:
        """通过名称获取命令"""
        for each in self.command_list:
            if each.name == command_name:
                return each # type: ignore
        return None

    def get_command_by_command(self, command: str) -> Optional[T]:
        """通过命令获取命令"""
        for each in self.command_list:
            if each.command == command:
                return each # type: ignore
        return None
