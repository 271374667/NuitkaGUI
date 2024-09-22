from PySide6.QtWidgets import QApplication

from src.model.args_model import ArgsModel
from src.view.args_view import ArgsView


class ArgsPresenter:
    def __init__(self):
        self._view = ArgsView()
        self._model = ArgsModel()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model


if __name__ == "__main__":
    app = QApplication([])
    presenter = ArgsPresenter()
    presenter.view.show()
    app.exec()
