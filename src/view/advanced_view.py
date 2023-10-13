from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget
from qmaterialwidgets.components import CheckBox, LineEdit, SpinBox, ToolTipFilter

from src.interface.Ui_advanced_page import Ui_Form


class AdvancedView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        # self.enable_default_options()
        self.initialize()

    def get_jobs(self) -> SpinBox:
        return self.ui.jobs

    def set_jobs(self, value: int) -> None:
        self.ui.jobs.setValue(value)

    def get_low_memory(self) -> CheckBox:
        return self.ui.CBLowMemory

    def set_low_memory(self, value: bool) -> None:
        self.ui.CBLowMemory.setChecked(value)

    def get_clang(self) -> CheckBox:
        return self.ui.CBClang

    def set_clang(self, value: bool) -> None:
        self.ui.CBClang.setChecked(value)

    def get_mingw64(self) -> CheckBox:
        return self.ui.CBMingw64

    def set_mingw64(self, value: bool) -> None:
        self.ui.CBMingw64.setChecked(value)

    def get_remove_output(self) -> CheckBox:
        return self.ui.CBRemoveOutput

    def set_remove_output(self, value: bool) -> None:
        self.ui.CBRemoveOutput.setChecked(value)

    def get_show_progress(self) -> CheckBox:
        return self.ui.CBShowProgress

    def set_show_progress(self, value: bool) -> None:
        self.ui.CBShowProgress.setChecked(value)

    def get_windows_disable_console(self) -> CheckBox:
        return self.ui.CBDisableConsole

    def set_windows_disable_console(self, value: bool) -> None:
        self.ui.CBDisableConsole.setChecked(value)

    def get_lto(self) -> CheckBox:
        return self.ui.CBLto

    def set_lto(self, value: bool) -> None:
        self.ui.CBLto.setChecked(value)

    def get_disable_ccache(self) -> CheckBox:
        return self.ui.CBDisableCcache

    def set_disable_ccache(self, value: bool) -> None:
        self.ui.CBDisableCcache.setChecked(value)

    def get_quiet(self) -> CheckBox:
        return self.ui.CBQuiet

    def set_quiet(self, value: bool) -> None:
        self.ui.CBQuiet.setChecked(value)

    def get_show_memory(self) -> CheckBox:
        return self.ui.CBShowMemory

    def set_show_memory(self, value: bool) -> None:
        self.ui.CBShowMemory.setChecked(value)

    def get_clean_cache(self) -> CheckBox:
        return self.ui.CBCleanCache

    def set_clean_cache(self, value: bool) -> None:
        self.ui.CBCleanCache.setChecked(value)

    def get_windows_uac_admin(self) -> CheckBox:
        return self.ui.CBwindowsUacAdmin

    def set_windows_uac_admin(self, value: bool) -> None:
        self.ui.CBwindowsUacAdmin.setChecked(value)

    def get_windows_company_name(self) -> LineEdit:
        return self.ui.LECompanyName

    def get_windows_company_name_text(self) -> str:
        return self.ui.LECompanyName.text()

    def set_windows_company_name(self, value: str) -> None:
        self.ui.LECompanyName.setText(value)

    def get_windows_file_version(self) -> LineEdit:
        return self.ui.LEFileVersion

    def get_windows_file_version_text(self) -> str:
        return self.ui.LEFileVersion.text()

    def set_windows_file_version(self, value: str) -> None:
        self.ui.LEFileVersion.setText(value)

    def get_windows_product_version(self) -> LineEdit:
        return self.ui.LEProductVersion

    def get_windows_product_version_text(self) -> str:
        return self.ui.LEProductVersion.text()

    def set_windows_product_version(self, value: str) -> None:
        self.ui.LEProductVersion.setText(value)

    def get_windows_file_description(self) -> LineEdit:
        return self.ui.LEFileDescription

    def get_windows_file_description_text(self) -> str:
        return self.ui.LEFileDescription.text()

    def set_windows_file_description(self, value: str) -> None:
        self.ui.LEFileDescription.setText(value)

    def enable_default_options(self):
        # 默认开启一些选项(这样子设置可以触发信号)
        self.get_lto().setChecked(True)
        self.get_remove_output().setChecked(True)
        self.get_show_progress().setChecked(True)

    def initialize(self) -> None:
        # 找到界面内所有的控件,然后对他们installEventFilter
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 0))


if __name__ == '__main__':
    app = QApplication([])
    window = AdvancedView()
    window.show()
    app.exec()
