import contextlib
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from typing import Optional

import loguru
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy
from qfluentwidgets.components import (
    CheckBox,
    StrongBodyLabel,
    LineEdit,
    ComboBox,
    SpinBox,
)


# 将Command写在前面，详情写在后面能够方便IDE进行代码提示


class CommandBase(ABC):
    enabled: bool = True  # 是否启用
    visible: bool = True  # 是否可见
    name: str = ""  # 名称
    description: str = ""  # 描述
    command: str = ""  # 命令
    value: str = ""  # 值

    def __new__(cls, *args, **kwargs):
        # 单例
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    @abstractmethod
    def get_command(self) -> str:
        """获取命令"""
        raise NotImplementedError("This method must be implemented in subclass")

    def __repr__(self) -> str:
        return f"[{self.name}: {self.value} ({self.command})]"


class WidgetBindMixin(ABC):
    """有一些命令需要动态创建widget，这个mixin用于绑定widget"""
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
        raise NotImplementedError("This method must be implemented in subclass")

    @abstractmethod
    def update_widget(self):
        raise NotImplementedError("This method must be implemented in subclass")

    @abstractmethod
    def update_value(self):
        raise NotImplementedError("This method must be implemented in subclass")


class CommandFlagBase(CommandBase, WidgetBindMixin):
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
        if self.widget is not None:
            return self.widget

        widget = CheckBox()
        widget.setChecked(self.value)
        widget.setText(f"{self.name}\n{self.command}")
        widget.setToolTip(self.description)
        widget.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        widget.setMinimumSize(QSize(45, 60))
        self.bind_widget = widget
        self.bind_widget.stateChanged.connect(self.update_value)
        return widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setEnabled(self.enabled)
            self.bind_widget.setChecked(self._value)
            self.bind_widget.repaint()
            self.bind_widget.update()

    def update_value(self):
        if self.bind_widget is not None:
            self.value = self.bind_widget.isChecked()
            self.enabled = self.bind_widget.isEnabled()

    def get_command(self) -> str:
        if not self.command:
            raise ValueError("Command must be set")
        return f"--{self.command}"


class CommandValueBase(CommandBase):
    _value: str | int = ""

    @property
    def value(self) -> str | int:
        return self._value

    @value.setter
    def value(self, value: str | int):
        self._value = value

    def get_command(self) -> str:
        raise NotImplementedError("This method must be implemented in subclass")


# 下面是CommandValue的子类，用于定义不同类型的Command


class CommandTextBase(CommandValueBase, WidgetBindMixin):
    _value: str = ""
    bind_widget: Optional[LineEdit] = None
    widget: Optional[QWidget] = None

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        if self.validate():
            self._value = value
            loguru.logger.debug(f"CommandTextBase: {self.name} = {self.value}")
            return
        raise ValueError(f"Value {value} is not valid")

    def validate(self) -> bool:
        return True

    def create_widget(self) -> QWidget:
        if self.widget is not None:
            return self.widget

        text_widget = QWidget()
        layout = QHBoxLayout(text_widget)

        self._label = StrongBodyLabel()
        self._label.setText(self.name)
        self._label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self._label.setToolTip(self.description)
        self._line_edit = LineEdit()
        self._line_edit.setText(self.value)
        self._line_edit.setToolTip(self.description)
        self._line_edit.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        self._line_edit.setPlaceholderText(self.description)
        layout.addWidget(self._label)

        layout.addWidget(self._line_edit)
        self.bind_widget = self._line_edit
        self._line_edit.textChanged.connect(self.update_value)
        self.widget = text_widget
        return text_widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setEnabled(self.enabled)
            self.bind_widget.setText(self.value)

    def update_value(self):
        if self.bind_widget is not None:
            self.value = self.bind_widget.text()

    def get_command(self) -> str:
        if not self.command:
            raise ValueError("Command must be set")
        return f'--{self.command}="{self.value}"'


class CommandChoiceBase(CommandValueBase, WidgetBindMixin):
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
            loguru.logger.debug(f"CommandChoiceBase: {self.name} = {self.value}")
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
        if self.widget is not None:
            return self.widget

        choice_widget = QWidget()
        layout = QHBoxLayout(choice_widget)

        self._label = StrongBodyLabel()
        self._label.setText(self.name)
        self._label.setToolTip(self.description)
        self._label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self._combo_box = ComboBox()
        self._combo_box.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self._combo_box.addItems(self.chocies)
        self._combo_box.setCurrentText(self.value)
        self._combo_box.setToolTip(self.description)

        layout.addWidget(self._label)
        layout.addWidget(self._combo_box)
        self.bind_widget = self._combo_box
        self.widget = choice_widget
        self._combo_box.currentTextChanged.connect(self.update_value)
        return choice_widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setEnabled(self.enabled)
            self.bind_widget.setCurrentText(self.value)

    def update_value(self):
        if self.bind_widget is not None:
            self.value = self.bind_widget.currentText()

    def get_command(self) -> str:
        if not self.command:
            raise ValueError("Command must be set")
        return f"--{self.command}={self.value}"


class CommandIntBase(CommandValueBase, WidgetBindMixin):
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
            loguru.logger.debug(f"CommandIntBase: {self.name} = {self.value}")
        else:
            raise ValueError(f"Value must be in range {self.number_range}")

    def create_widget(self) -> QWidget:
        if self.widget is not None:
            return self.widget

        int_widget = QWidget()
        layout = QHBoxLayout(int_widget)

        self._label = StrongBodyLabel()
        self._label.setText(self.name)
        self._label.setToolTip(self.description)
        self._label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self._spin_box = SpinBox()
        self._spin_box.setRange(self.number_range[0], self.number_range[1])
        self._spin_box.setSingleStep(1)
        self._spin_box.setValue(self.value)
        self._spin_box.setToolTip(self.description)
        self._spin_box.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout.addWidget(self._label)
        layout.addWidget(self._spin_box)
        self.bind_widget = self._spin_box
        self.widget = int_widget
        self._spin_box.valueChanged.connect(self.update_value)
        return int_widget

    def update_widget(self):
        if self.bind_widget is not None:
            self.bind_widget.setEnabled(self.enabled)
            self.bind_widget.setValue(self.value)

    def update_value(self):
        if self.bind_widget is not None:
            self.value = self.bind_widget.value()

    def get_command(self) -> str:
        if not self.command:
            raise ValueError("Command must be set")
        return f"--{self.command}={self.value}"


class CommandPathBase(CommandValueBase):
    _value: str = ""
    visible: bool = False

    @property
    def value(self) -> Optional[Path]:
        return Path(self._value) if self._value else None

    @value.setter
    def value(self, value: str | Path | None):
        if value is None:
            self._value = ""
            return
        elif isinstance(value, Path):
            self._value = str(value)
            return
        self._value = value

    def get_command(self) -> str:
        if not self.command:
            raise ValueError("Command must be set")
        return f'--{self.command}="{self.value}"'


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

    def get_command(self) -> str:
        if not self.command:
            raise ValueError("Command must be set")
        return f"--{self.command}={self.value}"
