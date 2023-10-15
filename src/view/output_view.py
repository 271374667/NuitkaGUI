from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCharFormat
from PySide6.QtWidgets import QWidget
from qmaterialwidgets.components import (FilledPushButton, TextEdit, TextPushButton, ToolTipFilter)

from src.interface.Ui_output_page import Ui_Form


class OutputView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setObjectName('OutputView')

        self.initialize()

    def get_output_textedit(self) -> TextEdit:
        return self.ui.TextEdit

    def get_input_textedit(self) -> TextEdit:
        return self.ui.TextEdit_2

    def get_output_text(self) -> str:
        return self.get_output_textedit().toPlainText()

    def set_output_text(self, text: str) -> None:
        self.get_output_textedit().setPlainText(text)

    def clear_output_text(self) -> None:
        self.get_output_textedit().clear()

    def get_input_text(self) -> str:
        return self.get_input_textedit().toPlainText()

    def set_input_text(self, text: str) -> None:
        self.get_input_textedit().setPlainText(text)

    def clear_input_text(self) -> None:
        self.get_input_textedit().clear()

    def get_analysis_btn(self) -> TextPushButton:
        return self.ui.TextPushButton

    def get_clear_btn(self) -> FilledPushButton:
        return self.ui.FilledPushButton

    def get_get_cmd_btn(self) -> TextPushButton:
        return self.ui.TextPushButton_2

    def set_text_color(self, text: str, color: Qt.GlobalColor) -> None:
        # 创建一个QTextCharFormat对象，并设置所需的颜色
        red_format = QTextCharFormat()
        red_format.setForeground(color)

        # 获取QTextEdit的文档对象
        document = self.get_input_textedit().document()

        # 获取文档的光标对象
        cursor = document.find(text)
        print(text)

        # 使用光标对象的mergeCharFormat方法将指定文本的格式设置为所需的格式
        cursor.mergeCharFormat(red_format)

        # 将光标移动到文档的末尾，以便保持其他文本的颜色不变
        cursor.setPosition(document.characterCount())

        # 设置光标的格式为默认格式，以便其他文本不受影响
        cursor.mergeCharFormat(QTextCharFormat())

    def set_text_color_red(self, text: str) -> None:
        self.set_text_color(text, Qt.GlobalColor.red)

    def set_text_color_blue(self, text: str) -> None:
        self.set_text_color(text, Qt.GlobalColor.blue)

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = OutputView()
    window.set_output_text('测试')
    window.set_input_text('1234567890')
    window.set_text_color_red('123')
    window.set_text_color_blue('456')
    window.get_get_cmd_btn().clicked.connect(lambda: print(window.get_output_text()))
    window.show()
    app.exec()
