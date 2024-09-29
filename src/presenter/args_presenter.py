from PySide6.QtWidgets import QApplication

from src.model.args_model import ArgsModel
from src.view.args_view import ArgsView


class ArgsPresenter:
    def __init__(self):
        self._view = ArgsView()
        self._model = ArgsModel()

        self.bind()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

    def update_command(self):
        self._view.get_output_args_textedit().setText(self._model.get_command())

    def _clear(self):
        self._view.get_output_args_textedit().clear()
        self._view.get_input_args_textedit().clear()

    def bind(self):
        self._view.get_output_args_btn().clicked.connect(self.update_command)
        self._view.get_clear_btn().clicked.connect(self._clear)


if __name__ == "__main__":
    app = QApplication([])
    presenter = ArgsPresenter()
    presenter.view.show()
    app.exec()
