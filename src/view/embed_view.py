from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import PrimaryPushButton, ToolTipFilter

from src.component.embed_file_tree import EmbedFileTree
from src.interface.Ui_embed_page_fluent import Ui_Form
from src.view.message_base_view import MessageBaseView


class EmbedView(MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initialize()

    def get_load_dir_btn(self) -> PrimaryPushButton:
        return self.ui.BTNFlushDir

    def get_file_tree(self) -> EmbedFileTree:
        return self.ui.treeWidget

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == '__main__':
    app = QApplication([])
    view = EmbedView()
    view.show()
    app.exec()
