import loguru
from PySide6.QtCore import Slot

from src.model.main_model import MainModel
from src.presenter.about_presenter import AboutPresenter
from src.presenter.advanced_presenter import AdvancedPresenter
from src.presenter.basic_presenter import BasicPresenter
from src.presenter.embed_presenter import EmbedPresenter
from src.presenter.output_presenter import OutputPresenter
from src.presenter.plugin_presenter import PluginPresenter
from src.presenter.settings_presenter import SettingsPresenter
from src.view.main_view import MainView


class MainPresenter:
    def __init__(self):
        self._model = MainModel()

        self.basic_presenter: BasicPresenter = BasicPresenter()
        self.plugin_presenter: PluginPresenter = PluginPresenter()
        self.advanced_presenter: AdvancedPresenter = AdvancedPresenter()
        self.embed_presenter: EmbedPresenter = EmbedPresenter()
        self.output_presenter: OutputPresenter = OutputPresenter()
        self.settings_presenter: SettingsPresenter = SettingsPresenter()
        self.about_presenter: AboutPresenter = AboutPresenter()
        self._view = MainView(self.basic_presenter.get_view(),
                              self.advanced_presenter.get_view(),
                              self.plugin_presenter.get_view(),
                              self.embed_presenter.get_view(),
                              self.output_presenter.get_view(),
                              self.settings_presenter.get_view(),
                              self.about_presenter.get_view()
                              )

        self.bind()
        self.initialize()

    def get_model(self) -> MainModel:
        return self._model

    def get_view(self) -> MainView:
        return self._view

    def show(self) -> None:
        self.get_view().show()

    @Slot()
    def optimization_clicked(self, status: bool) -> None:
        self.get_model().set_optimization_enabled(status)

    def bind(self) -> None:
        self.settings_presenter.get_view().get_optimization_enabled().checkedChanged.connect(
                lambda x: self.optimization_clicked(x))

    def initialize(self) -> None:
        is_pythonexe_available = self.get_model().is_pythonexe_available()
        if not is_pythonexe_available:
            self.get_view().show_error_info('软件无法正常工作！', 'Python解释器未设置,请在设置中设置Python解释器后重启',
                                            duration=-1)

        # 判断当前需要启动优化
        if self.get_model().is_optimization_enabled():
            loguru.logger.debug('启动选项优化')
            self.advanced_presenter.set_defalut_options_status(True)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = MainPresenter().get_view()
    w.show()
    app.exec()
