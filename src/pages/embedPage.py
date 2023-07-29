from utils import windowFunc
from core import globalVar
from pathlib import Path
from PySide6.QtCore import Slot


@Slot()
def reflushEmbed() -> None:
    getEmbedFile()
    windowFunc.updateOutputPlainText()

@Slot()
def setRootPath() -> None:
    globalVar.mainWindow.ui.treeWidget.set_root_path(Path(globalVar.entryFilePath).parent)


@Slot()
def getEmbedFile() -> list[str]:
    globalVar.inputArgsExtended = globalVar.mainWindow.ui.treeWidget.get_nuitka_cmd()
    return globalVar.mainWindow.ui.treeWidget.get_nuitka_cmd()


globalVar.mainWindow.ui.BTNFlushDir.clicked.connect(setRootPath)
globalVar.mainWindow.ui.treeWidget.itemClicked.connect(reflushEmbed)

