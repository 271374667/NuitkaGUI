from enum import Enum

# 软件名称
SOFTWARE_NAME = 'NuitkaGUI'

# 当前版本号
__version__ = '0.0.5'

# 可用的插件列表
PLUGIN_LIST = ['pyside6', 'pyside2', 'pyqt5', 'pyqt6', 'tk-inter', 'matplotlib',
               'tensorflow', 'pywebview', 'multiprocessing', 'trio', 'kivy', 'transformers',
               'glfw', 'gevent', 'upx'
               ]

# 需要的模块版本
moduleVersion = {"nuitka": "1.7.0"}
