import pickle
import typing

from src.conf import config_path


class Runtime:
    """
    这个类负责管理运行时的全局变量,将他们存储到本地
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.file_path = config_path.RUNTIME_PYTHON_FILE

    def append(self, key: str, value: typing.Any):
        with open(self.file_path, 'rb') as f:
            data = pickle.load(f)
        data[key] = value
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)

    def read(self, key: str):
        with open(self.file_path, 'rb') as f:
            data = pickle.load(f)
        return data[key]

    def read_all(self):
        with open(self.file_path, 'rb') as f:
            data = pickle.load(f)
        return data

    def remove(self, key: str):
        with open(self.file_path, 'rb') as f:
            data = pickle.load(f)
        data.pop(key)
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)

    def remove_all(self):
        with open(self.file_path, 'wb') as f:
            pickle.dump({}, f)

    def initialize(self):
        if not self.file_path.exists():
            self.file_path.touch()
        self.remove_all()
