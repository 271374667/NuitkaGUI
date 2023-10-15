# sourcery skip: swap-nested-ifs
from pathlib import Path

SRC_HOME = Path(__file__).parent.parent

# 文件夹路径
PROJECT_DIR = SRC_HOME.parent  # 项目目录
ASSETS_DIR = PROJECT_DIR / 'assets'  # 资源目录
DOWNLOAD_DIR = SRC_HOME / 'download'  # 下载目录
RESOURCE_DIR = SRC_HOME / 'resource'  # 资源目录
LOG_DIR = PROJECT_DIR / 'logs'  # 日志目录
GCC_DIR = RESOURCE_DIR / 'gcc'  # GCC 的安装目录

# 文件路径
ARIA2C_FILE = SRC_HOME / 'resource' / 'aria2c.exe'  # aria2c.exe 的路径
QRC_FILE = PROJECT_DIR / 'assets' / 'res.qrc'  # 资源文件的路径
QRC_PY_FILE = RESOURCE_DIR / f'rc_{QRC_FILE.stem}.py'  # 资源文件编译后的路径
RUNTIME_PYTHON_FILE = SRC_HOME / 'conf' / 'runtime_config.pkl'  # 运行时的全局变量配置
LOG_FILE = LOG_DIR / 'log.log'  # 日志文件
SETTINGS_FILE = PROJECT_DIR / 'settings.json'  # 程序永久配置文件,有了这个就不用每一次都去选择python.exe了


# sourcery skip: merge-nested-ifs
if __name__ == '__main__':
    if QRC_FILE.exists():
        print('资源文件存在')
