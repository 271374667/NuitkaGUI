import time
from typing import List

import loguru
from PySide6.QtCore import QProcess, QTextStream, QTimer
from PySide6.QtWidgets import QApplication, QPlainTextEdit, QVBoxLayout, QWidget

from src.conf import config
from src.custom_widget.bubble_tip import BubbleLabel


class ProcessWindow(QWidget):
    def __init__(self, app: QApplication, window: QWidget, is_auto_close=False):
        super().__init__()
        self.is_auto_close = is_auto_close
        self._app = app
        self._window = window
        self.process = QProcess
        self.bubble = BubbleLabel()
        self.start_time = time.time()

        self.resize(1000, 600)
        self.setWindowTitle("命令行")
        self.text_edit = QPlainTextEdit()
        # 设置文本框最大长度
        self.text_edit.setMaximumBlockCount(config.MAX_OUTPUT_LINE)
        self.text_edit.setReadOnly(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.setLayout(self.layout)

    def run(self, command: List[str]):
        if not self.isVisible():
            self.show()
        self.text_edit.appendPlainText("Please wait,Running".center(50, "-"))
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.start(command[0], command[1:])
        self.process.readyReadStandardOutput.connect(self.readStdOutput)
        self.process.readyReadStandardError.connect(self.readStdError)
        self.process.finished.connect(self.run_finished)

    def readStdOutput(self):
        data = self.process.readAllStandardOutput()
        text = QTextStream(data).readAll()
        self.text_edit.appendPlainText(text)

    def readStdError(self):
        data = self.process.readAllStandardError()
        text = QTextStream(data).readAll()
        self.text_edit.appendPlainText(text)

    def run_finished(self):
        self.text_edit.appendPlainText("Finished".center(50, "-"))
        if self.is_auto_close:
            self.bubble.showMessage("程序运行结束即将自动关闭\nFinished")
            QTimer.singleShot(5000, self.close)
        else:
            self.bubble.showMessage("程序运行结束\nFinished")

        use_time = round(time.time() - self.start_time, 2)
        loguru.logger.info(f'程序运行结束，耗时{use_time}秒')
        self.text_edit.appendPlainText(f'程序运行结束，耗时{use_time}秒')
        self._app.alert(self._window, 0)
