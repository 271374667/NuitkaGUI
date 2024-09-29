from typing import Optional

from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import ToolTipFilter
from qfluentwidgets.components import PrimaryPushButton, InfoBadge, PillPushButton, ProgressBar, PushButton
from qframelesswindow import FramelessWindow

from src.interface.Ui_welcome_page_fluent import Ui_Form
from src.view.message_base_view import MessageBaseView


class WelcomeView(FramelessWindow, MessageBaseView):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Welcome to NuitkaGUI")

        # 设置三个选项的完成状态
        self._pip_source_url: Optional[str] = None
        self._python_exe_path: Optional[str] = None
        self._gcc_selected: bool = False
        self._current_finished: int = 0

        # 设置三个选项的完成状态
        self._python_finished = InfoBadge.attension('已完成', parent=self, target=self.ui.CardWidget)
        self._gcc_finished = InfoBadge.attension('已完成', parent=self, target=self.ui.CardWidget_2)
        self._pip_finished = InfoBadge.attension('已完成', parent=self, target=self.ui.CardWidget_3)

        # 设置三个选项右上角都有一个没有完成的提示
        self._python_unfinished = InfoBadge.error('未完成', parent=self, target=self.ui.CardWidget)
        self._gcc_unfinished = InfoBadge.error('未完成', parent=self, target=self.ui.CardWidget_2)
        self._pip_unfinished = InfoBadge.error('未完成', parent=self, target=self.ui.CardWidget_3)

        self.initialize()

    def get_hand_pythonexe_btn(self) -> PushButton:
        return self.ui.PushButton

    def get_auto_pythonexe_btn(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton

    def get_install_os_dependence_btn(self) -> PushButton:
        return self.ui.PushButton_2

    def get_intall_reg_dependence_btn(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton_2

    def get_default_pip_btn(self) -> PushButton:
        return self.ui.PushButton_3

    def get_auto_pip_btn(self) -> PrimaryPushButton:
        return self.ui.PrimaryPushButton_3

    def get_finish_btn(self) -> PillPushButton:
        return self.ui.finishedBtn

    def get_progress_bar(self) -> ProgressBar:
        return self.ui.ProgressBar

    @property
    def python_exe_path(self) -> Optional[str]:
        return self._python_exe_path

    @python_exe_path.setter
    def python_exe_path(self, value: Optional[str]) -> None:
        if value:
            self._python_finished.show()
            self._python_unfinished.hide()
            if self._python_exe_path is None:
                self._current_finished += 1
            self._python_exe_path = value
        elif not value:
            self._python_finished.hide()
            self._python_unfinished.show()
            if self._python_exe_path is not None:
                self._current_finished -= 1
            self._python_exe_path = None
        self._update_progress()

    @property
    def pip_source_url(self) -> Optional[str]:
        return self._pip_source_url

    @pip_source_url.setter
    def pip_source_url(self, value: Optional[str]) -> None:
        if value:
            self._pip_finished.show()
            self._pip_unfinished.hide()
            if self._pip_source_url is None:
                self._current_finished += 1
            self._pip_source_url = value
        elif not value:
            self._pip_finished.hide()
            self._pip_unfinished.show()
            if self._pip_source_url is not None:
                self._current_finished -= 1
            self._pip_source_url = None
        self._update_progress()

    @property
    def gcc_selected(self) -> bool:
        return self._gcc_selected

    @gcc_selected.setter
    def gcc_selected(self, value: bool) -> None:
        if value:
            self._gcc_finished.show()
            self._gcc_unfinished.hide()
            if not self._gcc_selected:
                self._current_finished += 1
            self._gcc_selected = value
        elif not value:
            self._gcc_finished.hide()
            self._gcc_unfinished.show()
            if self._gcc_selected:
                self._current_finished -= 1
            self._gcc_selected = value
        self._update_progress()

    def _progress_set_value(self, value: int) -> None:
        value = max(self.ui.ProgressBar.minimum(), min(value, self.ui.ProgressBar.maximum()))
        self.ui.ProgressBar.setValue(value)

    def _update_progress(self) -> None:
        self._progress_set_value(self._current_finished)
        if self._current_finished == 3:
            self.get_finish_btn().setEnabled(True)
            self.get_finish_btn().setText('完成')
        else:
            self.get_finish_btn().setEnabled(False)
            self.get_finish_btn().setText('您需要先完成设置')

    def initialize(self) -> None:
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == '__main__':
    app = QApplication([])
    window = WelcomeView()
    # window.ui.FilledPushButton_2.clicked.connect(lambda: window.progress_add_one())
    # window.ui.TonalPushButton_2.clicked.connect(lambda: window.progress_sub_one())
    # window.ui.TonalPushButton.clicked.connect(
    #         lambda: window.show_success_info('success标题', '点击了按钮,出现了success提示'))
    # window.ui.FilledPushButton.clicked.connect(
    #         lambda: window.show_error_info('error标题', '点击了按钮,出现了error提示'))
    #
    # window.ui.TonalPushButton_3.clicked.connect(lambda: window.set_pip_status(True))
    # window.ui.FilledPushButton_3.clicked.connect(lambda: window.set_pip_status(False))
    window.show()
    app.exec()
