from PySide6.QtCore import Slot

from src.model.output_model import OutputModel
from src.view.output_view import OutputView


class OutputPresenter:
    def __init__(self):
        self.model = OutputModel()
        self.view = OutputView()

        self.bind()

    def get_model(self) -> OutputModel:
        return self.model

    def get_view(self) -> OutputView:
        return self.view

    @Slot()
    def set_output_text_by_model(self) -> None:
        text = ' '.join(self.get_model().get_cmd())
        self.get_view().set_output_text(text)

    @Slot()
    def clear_output_and_input_text(self) -> None:
        self.get_view().clear_input_text()
        self.get_view().clear_output_text()

    def bind(self) -> None:
        self.get_view().get_get_cmd_btn().clicked.connect(lambda: self.set_output_text_by_model())
        self.get_view().get_clear_btn().clicked.connect(lambda: self.clear_output_and_input_text())


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = OutputPresenter().get_view()
    w.show()
    app.exec()
