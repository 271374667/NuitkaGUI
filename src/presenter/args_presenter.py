from PySide6.QtWidgets import QApplication

from src.model.args_model import ArgsModel
from src.utils.singleton import singleton
from src.view.args_view import ArgsView


@singleton
class ArgsPresenter:
    def __init__(self):
        self._view = ArgsView()
        self._model = ArgsModel()

        self.bind()

    @property
    def view(self) -> ArgsView:
        return self._view

    @property
    def model(self) -> ArgsModel:
        return self._model

    def update_command(self):
        self._view.get_output_args_textedit().setText(self._model.get_command())

    def parse_command(self, command: str):
        self._model.parse_command(command)
        self.update_command()
        self._model.update_widget()

    def _clear(self):
        self._view.get_output_args_textedit().clear()
        self._view.get_input_args_textedit().clear()

    def bind(self):
        self._view.get_output_args_btn().clicked.connect(self.update_command)
        self._view.get_clear_btn().clicked.connect(self._clear)
        self.view.get_input_args_btn().clicked.connect(
            lambda: self.parse_command(self.view.get_input_args_textedit().toPlainText()))


if __name__ == "__main__":
    app = QApplication([])
    presenter = ArgsPresenter()
    presenter.view.show()
    app.exec()
