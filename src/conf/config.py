from enum import Enum

system_encoding = 'gbk'  # if chinese character in username, use utf8 will fail

# 软件名称
SOFTWARE_NAME = 'NuitkaGUI'

# 当前版本号
__version__ = '0.0.7'

# 设置输出命令行最大行号
MAX_OUTPUT_LINE = 1500


class ModuleVersion(Enum):
    nuitka = "1.8.0"
    pipreqs = "0.4.10"


class PipSource(Enum):
    QingHua = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    ALiYun = 'http://mirrors.aliyun.com/pypi/simple/'
    ZhongGuoKeJiDaXue = 'https://pypi.mirrors.ustc.edu.cn/simple/'
    DouBan = 'http://pypi.douban.com/simple/'
    ZhongGuoKeJiJiShuDaXue = 'http://pypi.mirrors.ustc.edu.cn/simple/'
    Default = 'https://pypi.org/simple/'


class GCC(Enum):
    lanzouyun = "https://s-51.lanzog.com:446/10052200132145295bb/2023/08/17/a65fe06970e2e01befc340361b415e6b.zip?st=_oHTYWrEHjjXIzCNEOAnhA&e=1696519833&b=VXBZbwA0B2ZSYl9_aCjEAbQEgAHEDM1B4B2YPMgIrAzEBfVwmBWxRJA_c_c&fi=132145295&pid=140-249-188-241&up=2&mp=1&co=0"
    Yzuu = 'https://download.yzuu.cf/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip'
    site1 = "https://gh.api.99988866.xyz/https://github.com/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip"
    site2 = "https://ghproxy.com/https://github.com/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip"
    site3 = "https://hub.yzuu.cf/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip"


if __name__ == '__main__':
    print([x.value for x in GCC])
