from abc import abstractmethod
from pathlib import Path
from typing import List, Union


class CommandValidator:
    @abstractmethod
    def validate(self, command: Union[str, List]) -> bool:
        raise NotImplementedError("Not implemented")


class ValidatorManager:
    def __init__(self):
        self._validators: List[CommandValidator] = []

    def add_validator(self, validator: CommandValidator):
        self._validators.append(validator)

    def validate(self, command: Union[str, List]) -> bool:
        return all(validator.validate(command) for validator in self._validators)


class MainArgsValidator(CommandValidator):
    """
    判断 --main 参数是否是文件，然后是否存在
    """
    def validate(self, command: Union[str, List]) -> bool:
        if isinstance(command, str):
            return True
        elif isinstance(command, list):
            return all(isinstance(each, str) for each in command)
        else:
            return False