from PySide6.QtWidgets import QWidget, QApplication
from qfluentwidgets import ToolTipFilter
from qfluentwidgets.components import TextEdit, HyperlinkButton, PrimaryPushButton, CardWidget

from src.interface.Ui_args_page_fluent import Ui_Form


class ArgsView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initialize()

        # TODO: 未来更新反向分析命令的功能，现在先隐藏
        self.get_input_args_card_widget().setVisible(False)

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

    def get_input_args_card_widget(self) -> CardWidget:
        return self.ui.CardWidget_2

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    app = QApplication([])
    w = ArgsView()
    w.show()
    app.exec()
