from PySide6.QtWidgets import QApplication
from qfluentwidgets import PrimaryPushButton

from src.component.embed_file_tree import EmbedFileTree
from src.interface.Ui_embed_page_fluent import Ui_Form
from src.view.message_base_view import MessageBaseView


class EmbedView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def get_open_new_dir_btn(self) -> PrimaryPushButton:
        return self.ui.BTNFlushDir

    def get_file_tree(self) -> EmbedFileTree:
        return self.ui.treeWidget


if __name__ == '__main__':
    app = QApplication([])
    view = EmbedView()
    view.show()
    app.exec()
