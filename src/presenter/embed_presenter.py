from src.model.embed_model import EmbedModel
from src.view.embed_view import EmbedView


class EmbedPresenter:
    def __init__(self):
        self._view = EmbedView()
        self._model = EmbedModel()

    @property
    def view(self) -> EmbedView:
        return self._view

    @property
    def model(self) -> EmbedModel:
        return self._model
