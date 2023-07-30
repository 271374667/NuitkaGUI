from utils import windowFunc
from core import globalVar
from pathlib import Path
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog


@Slot()
def reflushEmbed() -> None:
    getEmbedFile()
    windowFunc.updateOutputPlainText()

@Slot()
def setRootPath() -> None:
    # 选择文件夹
    dirPath = QFileDialog.getExistingDirectory(
        globalVar.mainWindow, '选择文件夹', str(Path(globalVar.entryFilePath).parent))
    if dirPath:
        globalVar.mainWindow.ui.treeWidget.set_root_path(dirPath)


@Slot()
def getEmbedFile() -> list[str]:
    globalVar.inputArgsExtended = globalVar.mainWindow.ui.treeWidget.get_nuitka_cmd()
    return globalVar.mainWindow.ui.treeWidget.get_nuitka_cmd()


globalVar.mainWindow.ui.BTNFlushDir.clicked.connect(setRootPath)
globalVar.mainWindow.ui.treeWidget.itemClicked.connect(reflushEmbed)

