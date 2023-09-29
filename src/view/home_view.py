from PySide6.QtWidgets import QApplication, QWidget

from src.interface.Ui_basic_page import Ui_home_page


class BasicPage(QWidget, Ui_home_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = BasicPage()
    window.show()
    app.exec()
