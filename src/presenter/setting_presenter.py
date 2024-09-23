from src.view.setting_view import SettingView
from src.model.setting_model import SettingModel


class SettingPresenter:
    def __init__(self):
        self._view = SettingView()
        self._model = SettingModel()

    @property
    def view(self) -> SettingView:
        return self._view

    @property
    def model(self) -> SettingModel:
        return self._model
