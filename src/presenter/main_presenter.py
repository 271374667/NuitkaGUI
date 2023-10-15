from src.presenter.advanced_presenter import AdvancedPresenter
from src.presenter.basic_presenter import BasicPresenter
from src.presenter.embed_presenter import EmbedPresenter
from src.presenter.output_presenter import OutputPresenter
from src.presenter.plugin_presenter import PluginPresenter
from src.presenter.settings_presenter import SettingsPresenter
from src.view.main_view import MainView


class MainPresenter:
    def __init__(self):
        self.basic_presenter: BasicPresenter = BasicPresenter()
        self.plugin_presenter: PluginPresenter = PluginPresenter()
        self.advanced_presenter: AdvancedPresenter = AdvancedPresenter()
        self.embed_presenter: EmbedPresenter = EmbedPresenter()
        self.output_presenter: OutputPresenter = OutputPresenter()
        self.settings_presenter: SettingsPresenter = SettingsPresenter()

        self._view = MainView(self.basic_presenter.get_view(),
                              self.advanced_presenter.get_view(),
                              self.plugin_presenter.get_view(),
                              self.embed_presenter.get_view(),
                              self.output_presenter.get_view(),
                              self.settings_presenter.get_view()
                              )

        self.bind()

    def get_view(self) -> MainView:
        return self._view

    def bind(self) -> None:
        pass


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = MainPresenter().get_view()
    w.show()
    app.exec()
