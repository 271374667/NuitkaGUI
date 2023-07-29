import logging
import typing
from pathlib import Path

from PySide6.QtWidgets import QApplication


if typing.TYPE_CHECKING:
    from conf.initVar import MyWindow

# 全局app对象
app: QApplication = None

# 全局窗口变量
mainWindow: "MyWindow" = None

# 需要打包的Python文件路径
entryFilePath: str = ''

# 可执行的python.exe的路径
pythonExePath: str = ''

# 项目根路径
homePath: Path = None

# 当前默认的指令
argsDict = {
    '--onefile': False,
    '--standalone': True,
    '--show-progress': True,
    '--show-memory': False,
    '--remove-output': True,
    '--windows-disable-console': False,
    '--mingw64': False,
    '--quiet': False,
    '--lto=no': False,
    '--disable-ccache': False,
    '--assume-yes-for-downloads': True,
    '--clang': False,
    '--jobs': 8,
    '--output-dir': '',
    '--main': '',
    '--nofollow-import-to': [],
    '--windows-icon-from-ico': '',
    '--windows-company-name': '',
    '--windows-file-version': '',
    '--windows-product-version': '',
    '--windows-file-description': '',
    '--include-package': [],
}

# 添加插件列表
pluginList = []
for each in pluginList:
    argsDict[f'--plugin-enable={each}'] = False

# 是否正在运行
isRunning = False

# 创建一个日志记录器
logger: logging.Logger = None
