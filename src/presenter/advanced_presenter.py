from src.view.advanced_view import AdvancedView
from src.model.advanced_model import AdvancedModel


class AdvancedPresenter:
    def __init__(self):
        self._view = AdvancedView()
        self._model = AdvancedModel()

    @property
    def view(self) -> AdvancedView:
        return self._view

    @property
    def model(self) -> AdvancedModel:
        return self._model
