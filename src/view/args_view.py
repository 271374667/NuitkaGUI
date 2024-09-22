from src.interface.Ui_args_page_fluent import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication


class ArgsView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    w = ArgsView()
    w.show()
    app.exec()
