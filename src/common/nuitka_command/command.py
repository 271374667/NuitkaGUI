from abc import ABC
from enum import Enum
from pathlib import Path
from typing import Optional

from PySide6.QtWidgets import QWidget


# 将Command写在前面，详情写在后面能够方便IDE进行代码提示

class CommandBase(ABC):
    enabled: bool = False
    name: str = ''
    description: str = ''
    command: str = ''
    bind_widget: Optional[QWidget] = None


class CommandFlagBase(CommandBase):
    _value: bool = False

    @property
    def value(self) -> bool:
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value


class CommandValueBase(CommandBase):
    _value: str | int = ''

    @property
    def value(self) -> str | int:
        return self._value

    @value.setter
    def value(self, value: str | int):
        self._value = value


# 下面是CommandValue的子类，用于定义不同类型的Command

class CommandTextBase(CommandValueBase):
    _value: str = ''

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        if self.validate():
            self._value = value
            return
        raise ValueError(f'Value {value} is not valid')

    def validate(self) -> bool:
        return True


class CommandChoiceBase(CommandValueBase):
    class Choice(Enum):
        pass

    _value: str = ''

    @property
    def chocies(self) -> list[str]:
        return [choice.value for choice in self.Choice]

    @property
    def choice(self) -> Choice:
        return self.Choice(self.value)

    @choice.setter
    def choice(self, value: Choice):
        self.value = value.value

    @property
    def choice_index(self) -> int:
        return self.chocies.index(self.value)


class CommandIntBase(CommandValueBase):
    _value: int = 0
    number_range: tuple[int, int] = (0, 100)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        if self.number_range[0] <= value <= self.number_range[1]:
            self._value = value
        raise ValueError(f'Value must be in range {self.number_range}')


class CommandPathBase(CommandValueBase):
    _value: str = ''

    @property
    def value(self) -> Optional[Path]:
        return Path(self._value) if self._value and Path(self._value).exists() else None

    @value.setter
    def value(self, value: str | Path | None):
        if value is None:
            self._value = ''
            return
        elif isinstance(value, Path):
            self._value = str(value)
            return
        self._value = value


class CommandMultipleTimesBase(CommandValueBase):
    _value: list[str] = []

    @property
    def value(self) -> str:
        return ','.join(self._value)

    @value.setter
    def value(self, value: list[str]):
        self._value = value

    def add(self, value: str):
        self._value.append(value)

    def extend(self, value: list[str]):
        self._value.extend(value)

    def remove(self, value: str):
        self._value.remove(value)

    def clear(self):
        self._value.clear()
