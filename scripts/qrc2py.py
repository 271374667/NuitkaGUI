import subprocess

from src.core.paths import QRC_PY_FILE, QRC_FILE

print('正在编译资源文件')
# 使用 pyside6-rcc 命令将 qrc 文件编译成 py 文件
subprocess.run(['pyside6-rcc', str(QRC_FILE), '-o', str(QRC_PY_FILE)])
print('编译完成')
