from enum import Enum

from core import globalVar

# 软件名称
SOFTWARE_NAME = 'NuitkaGUI'

# 当前版本号
__version__ = '0.0.5'


class ModuleVersion(Enum):
    nuitka = "1.7.0"
    pyside6 = "6.5.0"
    pipreqs = "0.4.0"
