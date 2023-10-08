import pickle
import typing

from src.conf import config_path

T = typing.TypeVar('T', str, typing.Sequence, typing.Mapping, int, float, bool, object)


class RuntimeManager:
    """
    这个类负责管理运行时的全局变量,将他们存储到本地
    TODO:
        [ ]: 增加一个记忆上一次设置的功能，每一次开始的时候不要直接清空，而是读取上一次的设置，当程序被成功运行的时候才清空
    """
    _instance = None

    # 自带的属性
    file_path = config_path.RUNTIME_PYTHON_FILE

    # 下面是 config 可用参数
    AVAILABLE_PYTHON_LIST = 'avaliable_python_list'
    SELECTED_PYTHON = 'selected_python'
    FASTEST_PIP_SOURCE = 'fastest_pip_source'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def append(key: str, value: T):
        with open(RuntimeManager.file_path, 'rb') as f:
            data: dict = pickle.load(f)
        data[key] = value
        with open(RuntimeManager.file_path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def insert2first(key: str, value: T):
        with open(RuntimeManager.file_path, 'rb') as f:
            data: dict = pickle.load(f)

        key_value = data.get(key)
        if isinstance(key_value, list):
            key_value.insert(0, value)
        elif key_value is None:
            return

        with open(RuntimeManager.file_path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def set(key: str, value: T):
        RuntimeManager.append(key, value)

    @staticmethod
    def read(key: str):
        with open(RuntimeManager.file_path, 'rb') as f:
            data: dict = pickle.load(f)
        return data.get(key)

    @staticmethod
    def read_all():
        with open(RuntimeManager.file_path, 'rb') as f:
            data: dict = pickle.load(f)
        return data

    @staticmethod
    def get(key: str):
        return RuntimeManager.read(key)

    def __getitem__(self, item):
        return RuntimeManager.read(item)

    @staticmethod
    def remove(key: str):
        with open(RuntimeManager.file_path, 'rb') as f:
            data: dict = pickle.load(f)
        data.pop(key)
        with open(RuntimeManager.file_path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def remove_all():
        with open(RuntimeManager.file_path, 'wb') as f:
            pickle.dump({}, f)

    @staticmethod
    def initialize():
        if not RuntimeManager.file_path.exists():
            RuntimeManager.file_path.touch()
        RuntimeManager.remove_all()


if __name__ == '__main__':
    RuntimeManager.initialize()
    print(RuntimeManager.read_all())
    print(RuntimeManager.read(RuntimeManager.AVAILABLE_PYTHON_LIST))
