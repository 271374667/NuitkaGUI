from PySide6.QtCore import Slot

from src.core import globalVar


def getArgs() -> list:
    argsList = [globalVar.pythonExePath, '-m', 'nuitka']
    for key, value in globalVar.argsDict.items():
        if value != '' and isinstance(value, str):
            argsList.append(f'{key}={value}')
        elif value is True and isinstance(value, bool):
            argsList.append(key)

        # 特殊处理 --nofollow-import-to
        elif key == '--nofollow-import-to' and globalVar.argsDict['--nofollow-import-to'] != []:
            moduleList = globalVar.argsDict['--nofollow-import-to']
            req = ','.join([x.split('==')[0] for x in moduleList])
            argsList.append(f'{key}={req}')
    if globalVar.inputArgsExtended != []:
        argsList.extend(globalVar.inputArgsExtended)
    argsList = [x.replace('\\', '/') for x in argsList]
    globalVar.inputArgs = argsList
    globalVar.logger.debug(f'输出命令为:{argsList}')
    return argsList


@Slot()
def updateOutputPlainText():
    """通过刷新输出控件，显示新地输出命令"""
    globalVar.mainWindow.ui.PTEArgsOutput.setPlainText(' '.join(getArgs()))
