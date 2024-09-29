from src.utils.env_utils import EnvUtils
from src.utils.python_env_utils import PythonEnvUtils


class EnvManager:
    def __init__(self):
        self._env_utils = EnvUtils()
        self._python_env_utils = PythonEnvUtils()
