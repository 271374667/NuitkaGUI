from PySide6.QtWidgets import QApplication, QWidget
from qmaterialwidgets.components import FilledPushButton, InfoBar

from src.component.embedFileTree import EmbedFileTree
from src.interface.Ui_embed_page import Ui_Form


class EmbedView(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def get_open_new_dir_btn(self) -> FilledPushButton:
        return self.ui.BTNFlushDir

    def get_file_tree(self) -> EmbedFileTree:
        return self.ui.treeWidget

    def show_success_info(self, title: str, content: str, duration: int = 15000) -> None:
        InfoBar.success(title, content, parent=self, duration=duration)

    def show_error_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.error(title, content, parent=self, duration=duration)


if __name__ == '__main__':
    app = QApplication([])
    view = EmbedView()
    view.show()
    app.exec()
