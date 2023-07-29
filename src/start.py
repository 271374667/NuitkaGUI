from core import globalVar, initVar
from pathlib import Path

globalVar.homePath = Path(__file__).parent

if __name__ == "__main__":
    initVar.initLogger()
    initVar.initWindow()
    print(Path(__file__).parent)

    globalVar.mainWindow.show()
    globalVar.app.exec()