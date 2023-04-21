#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Author  :   B-E-MAKE,KmBase
@Version :   1.0
@License :   (C)Copyright 2022, B-E-MAKE,KmBase
@Desc    :   None
"""


from PySide6.QtWidgets import QApplication

from ui.nuitkaGUI import MyWindow
import os

if __name__ == "__main__":
    pjPath = os.path.dirname(os.path.abspath(__file__))
    print("当前路径为：", pjPath)
    app = QApplication([])
    window = MyWindow(pjPath)
    window.show()
    app.exec()
