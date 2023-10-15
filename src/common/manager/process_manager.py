import subprocess
from typing import List

from PySide6.QtCore import QProcess


class ProcessManager:
    def __init__(self):
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.setReadChannel(QProcess.StandardOutput)

    def pyqt_run(self, cmd: List[str]) -> None:
        self.process.start(cmd[0], cmd[1:])

    @staticmethod
    def new_window_run(cmd: List[str]) -> None:
        subprocess.check_output(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE, encoding='gbk')
