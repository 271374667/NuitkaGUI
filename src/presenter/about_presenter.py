from src.model.about_model import AboutModel
from src.view.about_view import AboutView


class AboutPresenter:
    def __init__(self):
        self._model = AboutModel()
        self._view = AboutView()

    def get_view(self) -> AboutView:
        return self._view

    def get_model(self):
        return self._model
