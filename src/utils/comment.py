import subprocess
import threading
from pathlib import Path
from PySide6.QtCore import Slot

from core import globalVar


def threadRun(func):
    """装饰器，用于将函数放入线程中运行"""
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        globalVar.logger.debug(
            f'线程:{t.name}已启动,目标函数为:{func.__name__},参数为:{args},关键字参数为:{kwargs}')
    return wrapper


def isPythonAvailable(pythonExePath: str):
    try:
        output = subprocess.check_output([pythonExePath, "-V"], timeout=3)
    except (TimeoutError, FileNotFoundError):
        output = b""
    return output.startswith(b"Python 3.")

# 判断python模块是否大于某个版本


def isModuleBigger(moduleName: str, version: str) -> bool:
    """判断python模块是否大于某个版本"""
    try:
        import importlib
        module = importlib.import_module(moduleName)
        if module.__version__ > version:
            return True
        else:
            return False
    except:
        return False


def installModule(moduleName: str):
    """下载模块"""
    try:
        subprocess.run([globalVar.pythonExePath, '-m', 'pip', 'install',
                       moduleName, '-U'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except Exception as e:
        globalVar.logger.error(f'下载模块{moduleName}失败，原因：{e}')


def identifyThirdPartyLibraries(pythonExePath, pyFilePath: str) -> list:
    """
    函数“identifyThirdPartyLibraries”识别 Python 文件中使用的第三方库并返回需求列表。

    :param pythonExePath: `pythonExePath` 参数是 Python 可执行文件的路径。如果尚未安装，它用于安装“pipreqs”库。
    :param pyFilePath: 您要识别第三方库的 Python 文件的路径。
    :type pyFilePath: str
    :return: 函数“identifyThirdPartyLibraries”返回由“pipreqs”工具识别的第三方库的列表。
    """
    """识别第三方库"""
    requirementsFile = Path(pyFilePath).parent.joinpath('requirements.txt')
    # 使用pipreqs识别第三方库
    print(Path(pyFilePath).parent)

    process = subprocess.check_output(['pipreqs', Path(
        pyFilePath).parent, '--encoding=utf-8', '--force'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # 读取requirements.txt文件
    with open(requirementsFile, 'r', encoding='utf-8') as f:
        requirements = f.readlines()
        return requirements


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
