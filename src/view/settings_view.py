from PySide6.QtWidgets import QWidget
from qmaterialwidgets.components import InfoBar, OutlinedPushButton, SwitchButton

from src.interface.Ui_settings_page import Ui_Form


class SettingsView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setObjectName('SettingsView')

    def get_pythonexe(self) -> OutlinedPushButton:
        return self.ui.OutlinedPushButton

    def get_pythonexe_auto(self) -> OutlinedPushButton:
        return self.ui.OutlinedPushButton_3

    def get_pip_source(self) -> OutlinedPushButton:
        return self.ui.OutlinedPushButton_2

    def get_optimization_enabled(self) -> SwitchButton:
        return self.ui.SwitchButton

    def get_init(self) -> OutlinedPushButton:
        return self.ui.OutlinedPushButton_4

    def show_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.info(title, content, parent=self, duration=duration)

    def show_warning_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.warning(title, content, parent=self, duration=duration)

    def show_success_info(self, title: str, content: str, duration: int = 15000) -> None:
        InfoBar.success(title, content, parent=self, duration=duration)

    def show_error_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.error(title, content, parent=self, duration=duration)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = SettingsView()
    w.show()
    app.exec()
