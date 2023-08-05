import os
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from src.conf import config
from src.core import globalVar
from src.customWidget import myProgressDialog


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
    except (TimeoutError, FileNotFoundError, subprocess.CalledProcessError):
        output = b""
    return output.startswith(b"Python 3.")


def installModule(moduleName: str):
    """下载模块"""
    try:
        subprocess.run([globalVar.pythonExePath, '-m', 'pip', 'install',
                               moduleName, '-U', '-i', globalVar.defaultPipSource],
                       creationflags=subprocess.CREATE_NEW_CONSOLE)
    except Exception as e:
        globalVar.logger.error(f'下载模块{moduleName}失败，原因：{e}')


def getModuleVersion(moduleName: str) -> str:
    try:
        response = subprocess.run([globalVar.pythonExePath, '-m', 'pip', 'show', moduleName], stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, encoding='utf-8')
    except Exception:
        response = subprocess.run([globalVar.pythonExePath, '-m', 'pip', 'show', moduleName], stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, encoding='gbk')
    if response.stderr:
        return ''
    return response.stdout.splitlines()[1].split(maxsplit=1)[1]


def identifyThirdPartyLibraries(pyFilePath: str) -> list:
    """
    函数“identifyThirdPartyLibraries”识别 Python 文件中使用的第三方库并返回需求列表。
    :param pyFilePath: 您要识别第三方库的 Python 文件的路径。
    :type pyFilePath: str
    :return: 函数“identifyThirdPartyLibraries”返回由“pipreqs”工具识别的第三方库的列表。
    """
    """识别第三方库"""
    requirementsFile = Path(pyFilePath).parent.joinpath('requirements.txt')
    # 使用pipreqs识别第三方库
    print(Path(pyFilePath).parent)

    subprocess.check_output(['pipreqs', Path(
            pyFilePath).parent, '--encoding=utf-8', '--force'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # 读取requirements.txt文件
    with open(requirementsFile, 'r', encoding='utf-8') as f:
        return f.readlines()


def getDefaultPipSource() -> str:
    return getBestSource([x.value for x in config.PipSource])


def getSystemPath() -> Path:
    # 获取系统环境变量
    systemPathDict = os.environ.keys()
    # 将系统环境变量转换为列表
    if 'TMP' in systemPathDict:
        return Path(os.environ['TMP'].split(';')[0])
    elif 'TEMP' in systemPathDict:
        return Path(os.environ['TEMP'].split(';')[0])
    else:
        return Path.home()


def getBestSource(urlList) -> str:
    def test_speed(url):
        try:
            response = requests.head(url, timeout=5)
            return url, response.elapsed.total_seconds()
        except requests.exceptions.RequestException:
            return url, float('inf')

    def find_fastest_url(urls):
        globalVar.logger.debug('正在测试源的响应速度...')
        fastest_url = None
        fastest_time = float('inf')
        with ThreadPoolExecutor() as executor:
            results = executor.map(test_speed, urls)
            for url, response_time in results:
                globalVar.logger.debug(f'{url}的响应时间为{response_time}秒')
                if response_time < fastest_time:
                    fastest_url = url
                    fastest_time = response_time
        return fastest_url

    return find_fastest_url(urlList)


def isGccAvailable():
    try:
        output = subprocess.check_output(['gcc', "--version"], timeout=5)
    except Exception:
        output = b""
    return output.startswith(b"gcc") if output else False


def getBestGccSource() -> str:
    return getBestSource([x.value for x in config.GCC])


def downloadGcc() -> Path:
    gccSavePath = getSystemPath().joinpath('GCC')
    if not gccSavePath.exists():
        gccSavePath.mkdir(exist_ok=True, parents=True)

    # 判断是否已下载
    downloadedFilePath = gccSavePath.joinpath('w64devkit-1.20.0.zip')
    if downloadedFilePath.exists():
        return downloadedFilePath
    downloadWidget = myProgressDialog.DownloadProgressDialog()
    # TODO: 将来下载前先测速,选择最快的下载源
    downloadWidget.setWindowTitle('下载GCC中……')
    return downloadWidget.download(getBestGccSource(), gccSavePath)


def installGcc(downloadCachePath: Path):
    gccSavePath = getSystemPath().joinpath('GCC')
    if not gccSavePath.exists():
        gccSavePath.mkdir(exist_ok=True, parents=True)
    # 解压
    globalVar.logger.debug('正在解压GCC压缩包...')
    extractGcc = myProgressDialog.ExtractProgressDialog()
    extractGcc.extract(downloadCachePath, gccSavePath)
    globalVar.logger.debug('解压完成')

    # 将gcc中的bin目录通过cmd添加到环境变量中
    globalVar.logger.debug('正在将GCC添加到环境变量中...')
    # subprocess.run(['setx', 'Path', f'%Path%;"{gccSavePath.joinpath("w64devkit").joinpath("bin")}"', '/m'], shell=True)
    subprocess.run(f'setx Path %Path%;{gccSavePath.joinpath("w64devkit").joinpath("bin")} /m', shell=True)
    globalVar.logger.debug('已将GCC添加到环境变量中')


def is7zrAvailable():
    try:
        output = subprocess.check_output(['7zr'], timeout=5)
    except Exception:
        output = b""
    return output.startswith(b"\r\n7-Zip") if output else False


def download7zr() -> Path:
    # 获取一个临时系统环境路径用来保存7zr
    sevenZipParentSavePath = getSystemPath()
    if not sevenZipParentSavePath.exists():
        sevenZipParentSavePath.mkdir(exist_ok=True, parents=True)
    downloadWidget = myProgressDialog.DownloadProgressDialog()
    downloadWidget.setWindowTitle('下载7zr中……')
    sevenZipSavePath = downloadWidget.download(config.DownLoadResource.SevenZip.value, sevenZipParentSavePath)
    globalVar.sevenZipConsolePath = sevenZipSavePath
    globalVar.logger.debug('正在将7zr添加到环境变量中...')
    subprocess.run(['setx', 'NuitkaGUISystemPath', f'%Path%;{sevenZipSavePath.parent}', '/m'])
    globalVar.logger.debug(f'7zr当前是否可用：{is7zrAvailable()}')
    return sevenZipSavePath
