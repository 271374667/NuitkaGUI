from PySide6.QtCore import Qt, Slot

from src.core import globalVar


@Slot(int)
def jobsChange(value):
    globalVar.argsDict['--jobs'] = str(value)


@Slot(int)
def showProgressChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--show-progress'] = True
        return
    globalVar.argsDict['--show-progress'] = False


@Slot(int)
def showMemoryChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--show-memory'] = True
        return
    globalVar.argsDict['--show-memory'] = False


@Slot(int)
def removeOutputChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--remove-output'] = True
        return
    globalVar.argsDict['--remove-output'] = False


@Slot(int)
def lowMemoryChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--low-memory'] = True
        return
    globalVar.argsDict['--low-memory'] = False


@Slot(int)
def disableCcacheChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--disable-ccache'] = True
        return
    globalVar.argsDict['--disable-ccache'] = False


@Slot(int)
def disableConsoleChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--disable-console'] = True
        return
    globalVar.argsDict['--disable-console'] = False


@Slot(int)
def cleanCacheChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--clean-cache'] = True
        return
    globalVar.argsDict['--clean-cache'] = False


@Slot(int)
def quietChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--quiet'] = True
        return
    globalVar.argsDict['--quiet'] = False


@Slot(int)
def mingw64Change(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--mingw64'] = True
        return
    globalVar.argsDict['--mingw64'] = False


@Slot(int)
def clangChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--clang'] = True
        return
    globalVar.argsDict['--clang'] = False


@Slot(int)
def ltoChange(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--lto=no'] = True
        return
    globalVar.argsDict['--lto=no'] = False


@Slot(int)
def windowsUacAdminChang(value):
    if value == Qt.CheckState.Checked.value:
        globalVar.argsDict['--windows-uac-admin'] = True
        return
    globalVar.argsDict['--windows-uac-admin'] = False


@Slot(str)
def companyNameChanged(value: str):
    """当公司名改变时，更新输出命令"""
    globalVar.argsDict['--windows-company-name'] = value.strip()


@Slot(str)
def fileVersionChange(value: str):
    globalVar.argsDict['--windows-file-version'] = value.strip()


@Slot(str)
def productVersionChange(value: str):
    globalVar.argsDict['--windows-product-version'] = value.strip()


@Slot(str)
def fileDescriptionChange(value: str):
    globalVar.argsDict['--windows-file-description'] = value.strip()


globalVar.mainWindow.ui.CBShowProgress.stateChanged.connect(showProgressChange)
globalVar.mainWindow.ui.CBShowMemory.stateChanged.connect(showMemoryChange)
globalVar.mainWindow.ui.CBRemoveOutput.stateChanged.connect(removeOutputChange)
globalVar.mainWindow.ui.CBLowMemory.stateChanged.connect(lowMemoryChange)
globalVar.mainWindow.ui.CBDisableCcache.stateChanged.connect(
        disableCcacheChange)
globalVar.mainWindow.ui.CBDisableConsole.stateChanged.connect(
        disableConsoleChange)
globalVar.mainWindow.ui.CBCleanCache.stateChanged.connect(cleanCacheChange)
globalVar.mainWindow.ui.CBQuiet.stateChanged.connect(quietChange)
globalVar.mainWindow.ui.jobs.valueChanged.connect(jobsChange)
globalVar.mainWindow.ui.CBMingw64.stateChanged.connect(mingw64Change)
globalVar.mainWindow.ui.CBClang.stateChanged.connect(clangChange)
globalVar.mainWindow.ui.CBwindowsUacAdmin.stateChanged.connect(windowsUacAdminChang)
globalVar.mainWindow.ui.CBLto.stateChanged.connect(ltoChange)

globalVar.mainWindow.ui.LECompanyName.textChanged.connect(companyNameChanged)
globalVar.mainWindow.ui.LEFileVersion.textChanged.connect(fileVersionChange)
globalVar.mainWindow.ui.LEProductVersion.textChanged.connect(
        productVersionChange)
globalVar.mainWindow.ui.LEFileDescription.textChanged.connect(
        fileDescriptionChange)
