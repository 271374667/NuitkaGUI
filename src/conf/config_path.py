from pathlib import Path

SRC_HOME = Path(__file__).parent.parent

# 文件夹路径
DOWNLOAD_DIR = SRC_HOME / 'download'  # 下载目录
GCC_DIR = SRC_HOME / 'resource' / 'gcc'  # GCC 的安装目录
RUNTIME_PYTHON_FILE = SRC_HOME / 'conf' / 'runtime_config.pkl'  # 运行时的全局变量配置

# 文件路径
ARIA2C_FILE = SRC_HOME / 'resource' / 'aria2c.exe'  # aria2c.exe 的路径
