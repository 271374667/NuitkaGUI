from PySide6.QtCore import Slot
from core import globalVar

"""
插件页面的槽函数和绑定
"""


@Slot()
def addPlugin():
    currentSelect = globalVar.mainWindow.ui.listUnselect.currentIndex().row()
    currentItem = globalVar.mainWindow.ui.listUnselect.takeItem(currentSelect)
    globalVar.mainWindow.ui.listSelect.addItem(currentItem)
    globalVar.mainWindow.statusBar().showMessage(f'添加了一个插件{currentItem.text()}', 3000)

    # 将参数启用
    for each in globalVar.argsDict:
        if currentItem.text() in each:
            globalVar.argsDict[each] = True


@Slot()
def removePlugin():
    currentSelect = globalVar.mainWindow.ui.listSelect.currentIndex().row()
    currentItem = globalVar.mainWindow.ui.listSelect.takeItem(currentSelect)
    globalVar.mainWindow.ui.listUnselect.addItem(currentItem)
    globalVar.mainWindow.statusBar().showMessage(f'移除了一个插件{currentItem.text()}', 3000)

    # 将参数停用
    for each in globalVar.argsDict:
        if currentItem.text() in each:
            globalVar.argsDict[each] = False

globalVar.mainWindow.ui.BTNAddPlugin.clicked.connect(addPlugin)
globalVar.mainWindow.ui.BTNRemovePlugin.clicked.connect(removePlugin)
globalVar.mainWindow.ui.listUnselect.itemDoubleClicked.connect(addPlugin)
globalVar.mainWindow.ui.listSelect.itemDoubleClicked.connect(removePlugin)