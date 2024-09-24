from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets.components import TextEdit, HyperlinkButton, PrimaryPushButton

from src.interface.Ui_args_page_fluent import Ui_Form


class ArgsView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def get_output_args_textedit(self) -> TextEdit:
        return self.ui.TextEdit

    def get_output_args_btn(self) -> HyperlinkButton:
        return self.ui.HyperlinkButton_2

    def get_input_args_textedit(self) -> TextEdit:
        return self.ui.TextEdit_2

    def get_input_args_btn(self) -> HyperlinkButton:
        return self.ui.HyperlinkButton

    def get_clear_btn(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton


if __name__ == "__main__":
    app = QApplication([])
    w = ArgsView()
    w.show()
    app.exec()
