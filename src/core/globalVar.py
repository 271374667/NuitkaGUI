import logging
import typing
from pathlib import Path

from PySide6.QtWidgets import QApplication

if typing.TYPE_CHECKING:
    from src.core.initVar import MyWindow

# 全局app对象
app: QApplication

# 全局窗口变量
mainWindow: "MyWindow"

# 需要打包的Python文件路径
entryFilePath: str = ''

# 可执行的python.exe的路径
pythonExePath: str = ''

# 项目根路径
homePath: Path

# 当前输入的参数
inputArgs: list = []

# 当前可能会扩展的参数
inputArgsExtended: list = []

# 插件列表
pluginList: typing.List[typing.Tuple[str, str]] = []

# 是否正在运行
isRunning = False

# 创建一个日志记录器
logger: logging.Logger

# 系统编码格式
systemEncoding: str = 'utf-8'

# 默认的pip下载源
defaultPipSource: str = 'https://pypi.tuna.tsinghua.edu.cn/simple'

# 判断当前是否需要重启
isRestart = False

# 当前7zip console的路径
sevenZipConsolePath: str = ''

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
        '--lto=no': True,
        '--disable-ccache': False,
        '--assume-yes-for-downloads': True,
        '--clang': False,
        '--jobs': 8,
        '--output-dir': '',
        '--main': '',
        '--nofollow-import-to': [],
        '--include-package': [],
        '--windows-icon-from-ico': '',
        '--windows-company-name': '',
        '--windows-file-version': '',
        '--windows-product-version': '',
        '--windows-file-description': '',
        }
