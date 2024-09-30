from src.model.about_model import AboutModel
from src.utils.singleton import singleton
from src.view.about_view import AboutView


@singleton
class AboutPresenter:
    def __init__(self):
        self._view = AboutView()
        self._model = AboutModel()

    @property
    def view(self) -> AboutView:
        return self._view

    @property
    def model(self) -> AboutModel:
        return self._model
