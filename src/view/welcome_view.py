from typing import Optional

from PySide6.QtWidgets import QApplication, QFileDialog
from qmaterialwidgets import FramelessWindow
from qmaterialwidgets.components import (FilledPushButton, InfoBadge, InfoBar, OutlinedPushButton,
                                         ProgressBar,
                                         TonalPushButton)

from src.interface.Ui_welcome_page import Ui_Form


class WelcomeView(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 设置三个选项的完成状态
        self.python_finished = InfoBadge.attension('已完成', parent=self, target=self.ui.CardWidget)
        self.gcc_finished = InfoBadge.attension('已完成', parent=self, target=self.ui.CardWidget_2)
        self.pip_finished = InfoBadge.attension('已完成', parent=self, target=self.ui.CardWidget_3)

        # 设置三个选项右上角都有一个没有完成的提示
        self.python_unfinished = InfoBadge.error('未完成', parent=self, target=self.ui.CardWidget)
        self.gcc_unfinished = InfoBadge.error('未完成', parent=self, target=self.ui.CardWidget_2)
        self.pip_unfinished = InfoBadge.error('未完成', parent=self, target=self.ui.CardWidget_3)

    def get_hand_pythonexe_btn(self) -> TonalPushButton:
        return self.ui.TonalPushButton

    def get_auto_pythonexe_btn(self) -> FilledPushButton:
        return self.ui.FilledPushButton

    def get_detect_gcc_btn(self) -> TonalPushButton:
        return self.ui.TonalPushButton_2

    def get_download_gcc_btn(self) -> FilledPushButton:
        return self.ui.FilledPushButton_2

    def get_default_pip_btn(self) -> TonalPushButton:
        return self.ui.TonalPushButton_3

    def get_auto_pip_btn(self) -> FilledPushButton:
        return self.ui.FilledPushButton_3

    def get_finish_btn(self) -> OutlinedPushButton:
        return self.ui.OutlinedPushButton

    def get_progress_bar(self) -> ProgressBar:
        return self.ui.ProgressBar

    def set_pythonexe_status(self, status: bool) -> None:
        if status:
            self.python_finished.show()
            self.python_unfinished.hide()
            return
        self.python_finished.hide()
        self.python_unfinished.show()

    def set_gcc_status(self, status: bool) -> None:
        if status:
            self.gcc_finished.show()
            self.gcc_unfinished.hide()
            return
        self.gcc_finished.hide()
        self.gcc_unfinished.show()

    def set_pip_status(self, status: bool) -> None:
        if status:
            self.pip_unfinished.hide()
            self.pip_finished.show()
            return
        self.pip_unfinished.show()
        self.pip_finished.hide()

    def get_pythonexe_path_by_hand(self) -> Optional[str]:
        """手动获取 python.exe 路径"""
        result = QFileDialog.getOpenFileName(self, '选择 python.exe', '', 'Python (*.exe)')
        return result[0] or None

    def progress_add_one(self) -> None:
        current_value = self.ui.ProgressBar.value()
        if current_value < self.ui.ProgressBar.maximum():
            self.ui.ProgressBar.setValue(self.ui.ProgressBar.value() + 1)
        return

    def progress_sub_one(self) -> None:
        current_value = self.ui.ProgressBar.value()
        if current_value > self.ui.ProgressBar.minimum():
            self.ui.ProgressBar.setValue(self.ui.ProgressBar.value() - 1)
        return

    def progress_set_value(self, value: int) -> None:
        self.ui.ProgressBar.setValue(value)

    def set_finish_status(self, status: bool) -> None:
        if status:
            self.ui.OutlinedPushButton.setEnabled(True)
            self.ui.OutlinedPushButton.setText('完成')
            return
        self.ui.OutlinedPushButton.setEnabled(False)
        self.ui.OutlinedPushButton.setText('您需要先完成设置')

    def show_info(self, title: str, content: str) -> None:
        InfoBar.info(title, content, parent=self, duration=-1)

    def show_warning_info(self, title: str, content: str) -> None:
        InfoBar.warning(title, content, parent=self, duration=-1)

    def show_success_info(self, title: str, content: str) -> None:
        InfoBar.success(title, content, parent=self, duration=15000)

    def show_error_info(self, title: str, content: str) -> None:
        InfoBar.error(title, content, parent=self, duration=-1)


if __name__ == '__main__':
    app = QApplication([])
    window = WelcomeView()
    window.set_pythonexe_status(True)
    window.ui.FilledPushButton_2.clicked.connect(lambda: window.progress_add_one())
    window.ui.TonalPushButton_2.clicked.connect(lambda: window.progress_sub_one())
    window.ui.TonalPushButton.clicked.connect(
            lambda: window.show_success_info('success标题', '点击了按钮,出现了success提示'))
    window.ui.FilledPushButton.clicked.connect(
            lambda: window.show_error_info('error标题', '点击了按钮,出现了error提示'))

    window.ui.TonalPushButton_3.clicked.connect(lambda: window.set_pip_status(True))
    window.ui.FilledPushButton_3.clicked.connect(lambda: window.set_pip_status(False))
    window.set_finish_status(True)
    window.show()
    app.exec()
