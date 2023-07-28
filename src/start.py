from PySide6.QtWidgets import QApplication, QMainWindow
from Ui_nuitkaGUI import Ui_MainWindow
from core import globalVar
from conf import config, initVar
from pathlib import Path

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{config.SOFTWARE_NAME}-{config.__version__}")


app = QApplication([])
window = MyWindow()

# 传入参数给全局变量
globalVar.mainWindow = window
globalVar.homePath = Path(__file__).parent

if __name__ == "__main__":
    #globalVar.mainWindow.show()
    #app.exec()
    initVar.initLogger()
    globalVar.logger.info('test')
    pass