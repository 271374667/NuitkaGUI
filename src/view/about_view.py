from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QUrl, Slot

from src.interface.Ui_about_page import Ui_Form


class AboutView(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.bind()

    @Slot()
    def b_site_clicked(self) -> None:
        QDesktopServices.openUrl(QUrl("https://space.bilibili.com/282527875"))

    def bind(self):
        self.ui.TextPushButton.clicked.connect(self.b_site_clicked)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = AboutView()
    window.show()
    app.exec()
