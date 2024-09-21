from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from typing import Optional

from PySide6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets.components import (
    CheckBox,
    StrongBodyLabel,
    LineEdit,
    ComboBox,
    SpinBox,
)
import contextlib


# 将Command写在前面，详情写在后面能够方便IDE进行代码提示


class CommandBase(ABC):
    enabled: bool = True  # 是否启用
    visible: bool = True  # 是否可见
    name: str = ""  # 名称
    description: str = ""  # 描述
    command: str = ""  # 命令
    widget: Optional[QWidget] = None  # 绑定的完整的widget(可能包括多个QWidget)
    bind_widget: Optional[QWidget] = None  # 绑定的widget(负责对外交互的widget)

    def __init__(self) -> None:
        # 如果create_widget返回None，则不绑定任何widget
        with contextlib.suppress(Exception):
            widget = self.create_widget()
            if widget is not None:
                self.widget = widget

    @abstractmethod
    def create_widget(self) -> Optional[QWidget]:
        """创建一个QWidget用于显示和编辑Command的值"""
        raise NotImplementedError("This method must be implemented in subclass")

    @abstractmethod
    def update_widget(self):
        """更新QWidget的值"""
        raise NotImplementedError("This method must be implemented in subclass")


class CommandFlagBase(CommandBase):
    _value: bool = False
    bind_widget: Optional[CheckBox] = None
    widget: Optional[CheckBox] = None

    @property
    def value(self) -> bool:
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value

    def create_widget(self) -> CheckBox:
        widget = CheckBox()
        widget.setChecked(self.value)
        widget.setText(f"{self.name}\n{self.command}")
        widget.setToolTip(self.description)
        self.bind_widget = widget
        return widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.value = self.bind_widget.isChecked()


class CommandValueBase(CommandBase):
    _value: str | int = ""

    @property
    def value(self) -> str | int:
        return self._value

    @value.setter
    def value(self, value: str | int):
        self._value = value


# 下面是CommandValue的子类，用于定义不同类型的Command


class CommandTextBase(CommandValueBase):
    _value: str = ""
    bind_widget: Optional[LineEdit] = None

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        if self.validate():
            self._value = value
            return
        raise ValueError(f"Value {value} is not valid")

    def validate(self) -> bool:
        return True

    def create_widget(self) -> QWidget:
        text_widget = QWidget()
        layout = QHBoxLayout(text_widget)
        self._label = StrongBodyLabel(self.name)
        self._label.setToolTip(self.description)
        self._line_edit = LineEdit(self.value)
        self._line_edit.setToolTip(self.description)

        layout.addWidget(self._label)
        layout.addWidget(self._line_edit)
        self.bind_widget = self._line_edit
        return text_widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setText(self.value)


class CommandChoiceBase(CommandValueBase):
    class Choice(Enum):
        pass

    _value: str = ""
    bind_widget: Optional[ComboBox] = None

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        if value in self.chocies:
            self._value = value
        else:
            raise ValueError(f"Value {value} is not valid")


    @property
    def chocies(self) -> list[str]:
        return [c.value for c in self.Choice]

    @property
    def selected_choice(self) -> Choice:
        return self.Choice(self.value)

    @selected_choice.setter
    def selected_choice(self, value: Choice):
        self.value = value.value

    @property
    def choice_index(self) -> int:
        return self.chocies.index(self.value)

    def create_widget(self) -> QWidget:
        choice_widget = QWidget()
        layout = QHBoxLayout(choice_widget)

        self._label = StrongBodyLabel(self.name)
        self._label.setToolTip(self.description)

        self._combo_box = ComboBox()
        self._combo_box.addItems(self.chocies)
        self._combo_box.setCurrentText(self.value)
        self._combo_box.setToolTip(self.description)

        layout.addWidget(self._label)
        layout.addWidget(self._combo_box)
        self.bind_widget = self._combo_box
        return choice_widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setCurrentText(self.value)


class CommandIntBase(CommandValueBase):
    _value: int = -1
    number_range: tuple[int, int] = (0, 100)
    bind_widget: Optional[SpinBox] = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        if self.number_range[0] <= value <= self.number_range[1]:
            self._value = value
        raise ValueError(f"Value must be in range {self.number_range}")

    def create_widget(self) -> QWidget:
        int_widget = QWidget()
        layout = QHBoxLayout(int_widget)

        self._label = StrongBodyLabel(self.name)
        self._label.setToolTip(self.description)

        self._spin_box = SpinBox(self.value)
        self._spin_box.setToolTip(self.description)

        layout.addWidget(self._label)
        layout.addWidget(self._spin_box)
        self.bind_widget = self._spin_box
        return int_widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setValue(self.value)


class CommandPathBase(CommandValueBase):
    _value: str = ""
    visible: bool = False

    @property
    def value(self) -> Optional[Path]:
        return Path(self._value) if self._value and Path(self._value).exists() else None

    @value.setter
    def value(self, value: str | Path | None):
        if value is None:
            self._value = ""
            return
        elif isinstance(value, Path):
            self._value = str(value)
            return
        self._value = value


class CommandMultipleTimesBase(CommandValueBase):
    _value: list[str] = []
    visible: bool = False

    @property
    def value(self) -> str:
        return ",".join(self._value)

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
