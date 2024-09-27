from src.model.setting_model import SettingModel
from src.view.setting_view import SettingView


class SettingPresenter:
    def __init__(self):
        self._view = SettingView()
        self._model = SettingModel()

        self.bind()

    @property
    def view(self) -> SettingView:
        return self._view

    @property
    def model(self) -> SettingModel:
        return self._model

    def _exit(self):
        if self.view.show_mask_dialog("重启应用", "设置已经生效，重启应用后生效"):
            self.model.exit()

    def bind(self):
        self.view.optimization_card.comboBox.currentIndexChanged.connect(self._exit)
