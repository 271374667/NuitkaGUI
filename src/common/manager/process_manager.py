from PySide6.QtCore import QProcess
from typing import List

class ProcessManager:
    def __init__(self):
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.setReadChannel(QProcess.StandardOutput)
        self.process.setReadChannelMode(QProcess.MergedChannels)

    def run(self, cmd: List[str]) -> None:
        self.process.start(cmd[0], cmd[1:])