import subprocess
from typing import List

import loguru
from PySide6.QtCore import QProcess


class ProcessManager:
    def __init__(self):
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.setReadChannel(QProcess.StandardOutput)

    def pyqt_run(self, cmd: List[str]) -> None:
        self.process.start(cmd[0], cmd[1:])

    @loguru.logger.catch
    def new_window_run(self, cmd: List[str]) -> None:
        # subprocess.run(cmd)
        subprocess.run(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
