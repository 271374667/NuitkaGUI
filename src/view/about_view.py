from PySide6.QtWidgets import QWidget, QApplication
from src.interface.Ui_about_page_fluent import Ui_Form
import webbrowser


class AboutView(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.HyperlinkButton.clicked.connect(self._open_my_website)

    def _open_my_website(self):
        webbrowser.open("https://space.bilibili.com/282527875")


if __name__ == "__main__":
    app = QApplication([])
    w = AboutView()
    w.show()
    app.exec()
