from pathlib import Path
from zipfile import ZipFile

import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QProgressDialog

from src.core import globalVar


class DownloadProgressDialog(QProgressDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('下载进度')
        self.setLabelText('正在下载中……')
        self.setCancelButtonText("取消下载")
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI"
                }

    def download(self, url: str, save_path: Path = Path.cwd()) -> Path:
        try:

            response = requests.get(url, stream=True, headers=self.headers)
        except Exception:
            return Path('.')
        total_length = int(response.headers.get("Content-Length", 0))
        already_downloaded = 0
        file_name = url.split('/')[-1]
        save_path = Path(save_path) / file_name
        self.setMaximum(total_length)
        globalVar.logger.info(f'正在下载{file_name}到{save_path},文件大小{total_length / 1024 / 1024:.2f}MB')
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    if total_length != 0:
                        self.setValue(self.value() + len(chunk))
                    already_downloaded += len(chunk)
                    self.setLabelText(f'正在下载{file_name}……\n当前已经下载{already_downloaded / 1024 / 1024:.2f}MB')
                    if self.wasCanceled():
                        globalVar.logger.debug(f'用户取消了下载,当前已经下载了{already_downloaded / 1024 / 1024:.2f}MB')
                        break
        self.setValue(total_length)
        self.close()
        self.deleteLater()
        globalVar.logger.info(f'文件{file_name}下载完成')
        return save_path


class ExtractProgressDialog(QProgressDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('解压中……')
        self.setLabelText('解压中……')
        self.setCancelButtonText('取消')
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)

    def extract(self, zipFilePath: Path, extractPath: Path):
        with ZipFile(zipFilePath) as zipFile:
            self.setMaximum(len(zipFile.namelist()))
            for index, zipInfo in enumerate(zipFile.infolist()):
                if self.wasCanceled():
                    break
                self.setValue(index)
                self.setLabelText(f'解压中{zipInfo.filename[:30]}……')
                zipFile.extract(zipInfo, extractPath)
                globalVar.app.processEvents()
            self.setValue(self.maximum())
            self.close()
            self.deleteLater()


if __name__ == "__main__":
    app = QApplication([])
    window = DownloadProgressDialog()
    window.download(
            'https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-win32/seh/x86_64-8.1.0-release-win32-seh-rt_v6-rev0.7z')
    app.exec()
