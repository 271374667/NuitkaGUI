from abc import ABC
from typing import Optional

from PySide6.QtWidgets import QWidget


# 将Command写在前面，详情写在后面能够方便IDE进行代码提示

class CommandBase(ABC):
    enabled: bool = False
    command: str = ''
    bind_widget: Optional[QWidget] = None


class CommandBoolBase(CommandBase):
    value: bool = False

    def __init__(self, value: bool):
        self.value = value


class CommandTextBase(CommandBase):
    value: str = ''

    def __init__(self, value: str):
        self.value = value
