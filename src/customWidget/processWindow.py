import time
from typing import List

from PySide6.QtCore import QProcess, QTextStream, QTimer
from PySide6.QtWidgets import QPlainTextEdit, QVBoxLayout, QWidget

from src.conf import config
from src.core import globalVar
from src.customWidget.bubbleTips import BubbleLabel


class ProcessWindow(QWidget):
    def __init__(self, isAutoClose=False):
        super().__init__()
        self.isAutoClose = isAutoClose
        self.process = QProcess
        self.bubble = BubbleLabel()
        self.systemEncoding = 'uft-8'
        self.startTime = time.time()

        self.resize(1000, 600)
        self.setWindowTitle("命令行")
        self.textEdit = QPlainTextEdit()
        # 设置文本框最大长度
        self.textEdit.setMaximumBlockCount(config.MAX_OUTPUT_LINE)
        self.textEdit.setReadOnly(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textEdit)
        self.setLayout(self.layout)

    def run(self, command: List[str]):
        if not self.isVisible():
            self.show()
        self.textEdit.appendPlainText("Please wait,Running".center(50, "-"))
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.start(command[0], command[1:])
        self.process.readyReadStandardOutput.connect(self.readStdOutput)
        self.process.readyReadStandardError.connect(self.readStdError)
        self.process.finished.connect(self.runFinished)

    def readStdOutput(self):
        data = self.process.readAllStandardOutput()
        text = QTextStream(data).readAll()
        self.textEdit.appendPlainText(text)
        # self.textEdit.appendPlainText(
        #         str(self.process.readAllStandardOutput(), encoding=globalVar.systemEncoding, errors='ignore'))

    def readStdError(self):
        data = self.process.readAllStandardError()
        text = QTextStream(data).readAll()
        self.textEdit.appendPlainText(text)
        # self.textEdit.appendPlainText(
        #         str(self.process.readAllStandardError(), encoding=globalVar.systemEncoding, errors='ignore'))

    def runFinished(self):
        self.textEdit.appendPlainText("Finished".center(50, "-"))
        if self.isAutoClose:
            self.bubble.showMessage("程序运行结束即将自动关闭\nFinished")
            QTimer.singleShot(5000, self.close)
        else:
            self.bubble.showMessage("程序运行结束\nFinished")

        useTime = round(time.time() - self.startTime, 2)
        globalVar.logger.info(f'程序运行结束，耗时{useTime}秒')
        self.textEdit.appendPlainText(f'程序运行结束，耗时{useTime}秒')
        globalVar.app.alert(globalVar.mainWindow, 0)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ProcessWindow(isAutoClose=True)
    app.alert(window.bubble, 0)
    window.run(['ping', '-n', '5', 'www.baidu.com'])
    sys.exit(app.exec())
