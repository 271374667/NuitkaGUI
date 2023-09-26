from enum import Enum
from pathlib import Path

HOME = Path(__file__).parent.parent

system_encoding = 'gbk'  # if chinese character in username, use utf8 will fail

# 软件名称
SOFTWARE_NAME = 'NuitkaGUI'

# 当前版本号
__version__ = '0.0.7'

# 设置输出命令行最大行号
MAX_OUTPUT_LINE = 1500

# 下载目录
DOWNLOAD_DIR = HOME / 'download'

# GCC 的安装目录
GCC_DIR = HOME / 'resource' / 'gcc'


class ModuleVersion(Enum):
    nuitka = "1.7.9"
    pipreqs = "0.4.0"


class PipSource(Enum):
    QingHua = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    ALiYun = 'http://mirrors.aliyun.com/pypi/simple/'
    ZhongGuoKeJiDaXue = 'https://pypi.mirrors.ustc.edu.cn/simple/'
    DouBan = 'http://pypi.douban.com/simple/'
    ZhongGuoKeJiJiShuDaXue = 'http://pypi.mirrors.ustc.edu.cn/simple/'


class GCC(Enum):
    Yzuu = 'https://download.yzuu.cf/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip'
    site1 = "https://gh.api.99988866.xyz/https://github.com/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip"
    site2 = "https://ghproxy.com/https://github.com/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip"


if __name__ == '__main__':
    print([x.value for x in GCC])
