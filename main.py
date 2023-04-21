from PySide6.QtWidgets import QApplication
from src.view import View
import subprocess

if __name__ == '__main__':
    app = QApplication()  # 启动一个应用
    window = View()  # 实例化主窗口
    window.setGeometry(300, 300, 500, 150)
    window.setWindowTitle('Nutika打包小工具')
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
