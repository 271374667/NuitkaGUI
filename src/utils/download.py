import subprocess
from core import globalVar

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

def __downloadMoudle(moduleName: str):
    """下载模块"""
    try:
        subprocess.run([globalVar.pythonExePath, '-m', 'pip', 'install', moduleName, '-U'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except:
        pass