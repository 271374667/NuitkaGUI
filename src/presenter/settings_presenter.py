from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog

from src.model.settings_model import SettingsModel
from src.utils.run_in_thread import RunInThread
from src.view.settings_view import SettingsView


class SettingsPresenter:
    def __init__(self):
        self._model = SettingsModel()
        self._view = SettingsView()

        self.bind()

    def get_model(self) -> SettingsModel:
        return self._model

    def get_view(self) -> SettingsView:
        return self._view

    @Slot()
    def pythonexe_clicked(self) -> None:
        pythonexe, _ = QFileDialog.getOpenFileName(self._view, '选择Python解释器', '', 'Python解释器 (*.exe)')
        if pythonexe:
            self._view.show_success_info('成功', 'Python解释器设置成功！')
            self._model.set_pythonexe(pythonexe)
            return

        self._view.show_error_info('错误', 'Python解释器设置失败！')
        self._model.set_pythonexe('')

    @Slot()
    def pythonexe_auto_clicked(self) -> None:
        def run():
            return self.get_model().get_auto_pythonexe()

        def finish_func(pythonexe_auto: str):
            if pythonexe_auto == '':
                self.get_view().show_error_info('错误', '未找到可用的 Python.exe')
                return

            self.get_view().show_success_info('成功', 'Python解释器设置成功！')
            self.get_model().set_pythonexe(pythonexe_auto)

        self.t1 = RunInThread()
        self.t1.set_start_func(run)
        self.t1.set_finished_func(finish_func)
        self.t1.start()

    @Slot()
    def pip_source_clicked(self) -> None:
        def run():
            pip_source = self.get_model().get_fastest_pip_source()
            return pip_source

        def finish_func(pip_source: str):
            self.get_view().show_success_info('pip源设置成功', pip_source)
            self.get_model().set_pip_source(pip_source)

        self.t2 = RunInThread()
        self.t2.set_start_func(run)
        self.t2.set_finished_func(finish_func)
        self.t2.start()

    @Slot(bool)
    def optimization_enabled_clicked(self, is_enable: bool) -> None:
        if is_enable:
            self.get_view().show_info('开启优化', '使用内置的一些 Nuitka 常用优化选项', duration=300)
        else:
            self.get_view().show_info('关闭优化', '清空全部前置设置', duration=300)
        self.get_model().set_optimization_enabled(is_enable)

    @Slot()
    def init_clicked(self) -> None:
        self.get_model().initialize_settings_json_file()
        self.get_view().show_success_info('初始化成功', '初始化成功！')

    def bind(self) -> None:
        self.get_view().get_pythonexe_auto().clicked.connect(lambda: self.pythonexe_auto_clicked())
        self.get_view().get_pythonexe().clicked.connect(lambda: self.pythonexe_clicked())
        self.get_view().get_pip_source().clicked.connect(lambda: self.pip_source_clicked())
        self.get_view().get_optimization_enabled().checkedChanged.connect(
                lambda x: self.optimization_enabled_clicked(x))
        self.get_view().get_init().clicked.connect(lambda: self.init_clicked())


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = SettingsPresenter().get_view()
    w.show()
    app.exec()
