from src.core import BoolCommands, IntCommands, StrCommands
from src.model.advanced_model import AdvancedModel
from src.utils.singleton import Singleton
from src.view.advanced_view import AdvancedView


@Singleton
class AdvancedPresenter:
    def __init__(self):
        self._model = AdvancedModel()
        self._view = AdvancedView()

        self.bind()

    def get_model(self) -> AdvancedModel:
        return self._model

    def get_view(self) -> AdvancedView:
        return self._view

    def bind(self) -> None:
        self._view.get_jobs().valueChanged.connect(lambda x: self.get_model().set_option_value(IntCommands.jobs, x))
        self._view.get_low_memory().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.low_memory, bool(x)))
        self._view.get_clang().stateChanged.connect(
            lambda x: self.get_model().set_option_value(BoolCommands.clang, bool(x)))
        self._view.get_mingw64().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.mingw64, bool(x)))
        self._view.get_remove_output().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.remove_output, bool(x)))
        self._view.get_show_progress().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.show_progress, bool(x)))
        self._view.get_windows_disable_console().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.windows_disable_console, bool(x)))
        self._view.get_lto().stateChanged.connect(
            lambda x: self.get_model().set_option_value(BoolCommands.lto_no, bool(x)))
        self._view.get_disable_ccache().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.disable_ccache, bool(x)))
        self._view.get_quiet().stateChanged.connect(
            lambda x: self.get_model().set_option_value(BoolCommands.quiet, bool(x)))
        self._view.get_show_memory().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.show_memory, bool(x)))
        self._view.get_clean_cache().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.clean_cache, bool(x)))
        self._view.get_windows_uac_admin().stateChanged.connect(
                lambda x: self.get_model().set_option_value(BoolCommands.windows_uac_admin, bool(x)))
        # self._view.get_windows_uac_admin().stateChanged.connect(lambda: print(self._model.get_cmd())) # 调试用

        self._view.get_windows_company_name().editingFinished.connect(
                lambda: self.get_model().set_option_value(StrCommands.windows_company_name,
                                                          self._view.get_windows_company_name_text()))
        self._view.get_windows_file_version().editingFinished.connect(
                lambda: self.get_model().set_option_value(StrCommands.windows_file_version,
                                                          self._view.get_windows_file_version_text()))
        self._view.get_windows_product_version().editingFinished.connect(
                lambda: self.get_model().set_option_value(StrCommands.windows_product_version,
                                                          self._view.get_windows_product_version_text()))
        self._view.get_windows_file_description().editingFinished.connect(
                lambda: self.get_model().set_option_value(StrCommands.windows_file_description,
                                                          self._view.get_windows_file_description_text()))


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    presenter = AdvancedPresenter()
    presenter.get_view().show()
    app.exec()
