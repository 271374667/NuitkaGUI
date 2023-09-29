import subprocess

from src.conf import config_path

print('正在编译资源文件')
# 使用 pyside6-rcc 命令将 qrc 文件编译成 py 文件
subprocess.run(['pyside6-rcc', str(config_path.QRC_FILE), '-o', str(config_path.QRC_PY_FILE)])
print('编译完成')
