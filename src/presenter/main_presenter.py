from PySide6.QtWidgets import QApplication
from src.view.main_view import MainView
from src.model.main_model import MainModel
from src.presenter.basic_presenter import BasicPresenter
from src.presenter.advanced_presenter import AdvancedPresenter
from src.presenter.plugin_presenter import PluginPresenter
from src.presenter.embed_presenter import EmbedPresenter
from src.presenter.args_presenter import ArgsPresenter
from src.presenter.about_presenter import AboutPresenter
from src.presenter.setting_presenter import SettingPresenter


class MainPresenter:
    def __init__(self):
        self._basic_presenter = BasicPresenter()
        self._advanced_presenter = AdvancedPresenter()
        self._plugin_presenter = PluginPresenter()
        self._embed_presenter = EmbedPresenter()
        self._args_presenter = ArgsPresenter()
        self._about_presenter = AboutPresenter()
        self._setting_presenter = SettingPresenter()

        self._view = MainView(
            self._basic_presenter.view,
            self._advanced_presenter.view,
            self._plugin_presenter.view,
            self._embed_presenter.view,
            self._args_presenter.view,
            self._about_presenter.view,
            self._setting_presenter.view,
        )
        self._model = MainModel()

    @property
    def view(self) -> MainView:
        return self._view

    @property
    def model(self) -> MainModel:
        return self._model


if __name__ == "__main__":
    app = QApplication([])
    w = MainPresenter()
    w.view.show()
    app.exec()
