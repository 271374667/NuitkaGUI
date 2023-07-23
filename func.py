import subprocess
import threading
from pathlib import Path


def threadRun(func):
    """装饰器，用于将函数放入线程中运行"""
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
    return wrapper

def identifyThirdPartyLibraries(pythonExePath, pyFilePath: str) -> list:
    """
    函数“identifyThirdPartyLibraries”识别 Python 文件中使用的第三方库并返回需求列表。
    
    :param pythonExePath: `pythonExePath` 参数是 Python 可执行文件的路径。如果尚未安装，它用于安装“pipreqs”库。
    :param pyFilePath: 您要识别第三方库的 Python 文件的路径。
    :type pyFilePath: str
    :return: 函数“identifyThirdPartyLibraries”返回由“pipreqs”工具识别的第三方库的列表。
    """
    """识别第三方库"""
    # 检测是否安装pipreqs
    try:
        import pipreqs
    except Exception:
        subprocess.check_call(
            [pythonExePath, '-m', 'pip', 'install', 'pipreqs', '-U'])

    requirementsFile = Path(pyFilePath).parent.joinpath('requirements.txt')
    # 使用pipreqs识别第三方库
    print(Path(pyFilePath).parent)

    process = subprocess.Popen(['pipreqs', Path(
        pyFilePath).parent, '--encoding=utf8', '--force'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    process.wait()

    # 读取requirements.txt文件
    with open(requirementsFile, 'r', encoding='utf-8') as f:
        requirements = f.readlines()
        return requirements
    
def isPythonAvailable(pythonExePath:str):
    try:
        output = subprocess.check_output([pythonExePath, "-V"], timeout=3)
    except (TimeoutError, FileNotFoundError):
        output = b""
    return output.startswith(b"Python 3.")