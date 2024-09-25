from PySide6.QtWidgets import QApplication

from src.config import cfg, Optimization
from src.model.main_model import MainModel
from src.presenter.about_presenter import AboutPresenter
from src.presenter.advanced_presenter import AdvancedPresenter
from src.presenter.args_presenter import ArgsPresenter
from src.presenter.basic_presenter import BasicPresenter
from src.presenter.embed_presenter import EmbedPresenter
from src.presenter.plugin_presenter import PluginPresenter
from src.presenter.setting_presenter import SettingPresenter
from src.view.main_view import MainView


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
        self._default_optimization()

    @property
    def view(self) -> MainView:
        return self._view

    @property
    def model(self) -> MainModel:
        return self._model

    def _default_optimization(self):
        optimization: Optimization = cfg.get(cfg.optimization)
        match optimization:
            case Optimization.Normal:
                self._model.normal_optimization()
            case Optimization.Compatibility:
                self._model.compatibility_optimization()
            case Optimization.Speed:
                self._model.speed_optimization()
            case Optimization.Size:
                self._model.size_optimization()
            case _:
                raise ValueError(f"Unknown optimization: {optimization}")
        self._model.update_all_widget()


if __name__ == "__main__":
    app = QApplication([])
    w = MainPresenter()
    w.view.show()
    app.exec()
