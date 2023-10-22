from PySide6.QtCore import QObject, Signal, Slot

from src.common.manager.module_manager import ModuleManager
from src.common.manager.settings_manager import SettingsManager
from src.core import JsonSettings
from src.model.welcome_model import WelcomeModel
from src.utils.run_in_thread import RunInThread
from src.utils.singleton import Singleton
from src.view.welcome_view import WelcomeView


@Singleton
class WelcomePresenter(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.settings_manager: SettingsManager = SettingsManager()
        self.module_manager: ModuleManager = ModuleManager()

        self._model = WelcomeModel()
        self._view = WelcomeView()

        self._is_pythonexe_finished = False
        self._is_gcc_finished = False
        self._is_pip_finished = False

        # 获取所有的按钮
        self.pythonexe_by_hand_btn = self._view.get_hand_pythonexe_btn()
        self.pythonexe_auto_btn = self._view.get_auto_pythonexe_btn()
        self.detect_gcc_btn = self._view.get_detect_gcc_btn()
        self.download_gcc_btn = self._view.get_download_gcc_btn()
        self.default_pip_btn = self._view.get_default_pip_btn()
        self.auto_pip_btn = self._view.get_auto_pip_btn()
        self.bind()

    def get_model(self) -> WelcomeModel:
        return self._model

    def get_view(self) -> WelcomeView:
        return self._view

    def show(self):
        self.get_view().show()

    def close(self):
        self.get_view().close()

    def _get_finished_count(self) -> int:
        finished_count = self._is_pythonexe_finished + self._is_gcc_finished + self._is_pip_finished
        if finished_count == 3:
            self.get_view().set_finish_status(True)
            return finished_count
        self.get_view().set_finish_status(False)
        return finished_count

    @Slot()
    def pythonexe_by_hand(self) -> None:
        """手动选择 python.exe"""
        # 正确以后需要设置badge,进度条,成功提示,失败则反之
        result = self.get_view().get_pythonexe_path_by_hand()
        if result and self.get_model().is_pythonexe_avialable(result):
            self._is_pythonexe_finished = True
            self.get_view().set_pythonexe_status(True)
            self.get_view().progress_set_value(self._get_finished_count())
            self.get_view().show_success_info('python.exe 可用:', result)
            self.get_model().set_pythonexe_path(result)
            return
        self.get_view().show_error_info('python.exe 不可用', '请重新选择 python.exe')
        self._is_pythonexe_finished = False
        self.get_view().set_pythonexe_status(False)
        self.get_view().progress_set_value(self._get_finished_count())

    @Slot()
    def pythonexe_by_auto(self) -> None:
        """自动选择 python.exe"""
        self.get_view().get_auto_pythonexe_btn().setEnabled(False)

        def run(result):
            btn = self.get_view().get_auto_pythonexe_btn()
            if result and self.get_model().is_pythonexe_avialable(result):
                self._is_pythonexe_finished = True
                self.get_view().show_success_info('找到可用 python.exe', result)
                self.get_view().set_pythonexe_status(True)
                self.get_view().progress_set_value(self._get_finished_count())
                self.get_model().set_pythonexe_path(result)
                btn.setEnabled(True)
                return
            self._is_pythonexe_finished = False
            self.get_view().set_pythonexe_status(False)
            self.get_view().progress_set_value(self._get_finished_count())
            btn.setEnabled(True)

        self.t = RunInThread()
        self.t.set_start_func(self.get_model().get_pythonexe_path)
        self.t.set_finished_func(run)
        self.t.start()

    @Slot()
    def use_defualt_pip_source(self):
        """使用默认的 pip 源"""
        self.get_model().set_pip_source(self.get_model().get_default_pip_source())
        self.get_view().show_success_info('设置默认 pip 源成功',
                                          f'默认 pip 源为: {self.get_model().get_default_pip_source()}')
        self._is_pip_finished = True
        self.get_view().set_pip_status(True)
        self.get_view().progress_set_value(self._get_finished_count())

    @Slot()
    def use_auto_pip_source(self):
        """获取最快的 pip 源"""
        self.get_view().get_auto_pip_btn().setEnabled(False)

        def run(result):
            btn = self.get_view().get_auto_pip_btn()
            if result:
                self._is_pip_finished = True
                self.get_view().show_success_info('找到最快的 pip 源', result)
                self.get_view().set_pip_status(True)
                self.get_view().progress_set_value(self._get_finished_count())
                self.get_model().set_pip_source(result)
                btn.setEnabled(True)
                return
            self._is_pip_finished = False
            self.get_view().set_pip_status(False)
            self.get_view().progress_set_value(self._get_finished_count())
            btn.setEnabled(True)

        self.t1 = RunInThread()
        self.t1.set_start_func(self.get_model().get_fastest_pip_source)
        self.t1.set_finished_func(run)
        self.t1.start()

    @Slot()
    def detect_gcc(self):
        """判断当前gcc是否可用"""
        self.get_view().get_detect_gcc_btn().setEnabled(False)

        def run(result):
            btn = self.get_view().get_detect_gcc_btn()
            if result:
                self._is_gcc_finished = True
                self.get_view().show_success_info('gcc状态:', '可用')
                self.get_view().set_gcc_status(True)
                self.get_view().progress_set_value(self._get_finished_count())
                btn.setEnabled(True)
                return
            self._is_gcc_finished = False
            self.get_view().set_gcc_status(False)
            self.get_view().show_error_info('gcc状态:', '不可用')
            self.get_view().progress_set_value(self._get_finished_count())
            btn.setEnabled(True)

        self.t2 = RunInThread()
        self.t2.set_start_func(self.get_model().get_gcc_available)
        self.t2.set_finished_func(run)
        self.t2.start()

    @Slot()
    def download_gcc(self):
        """下载gcc，警告该选项会修改系统环境变量"""
        self.get_view().get_download_gcc_btn().setEnabled(False)
        self.get_view().show_warning_info('警告', '请勿关闭新开启的命令行窗口,否则可能会导致程序崩溃')

        def run():
            btn = self.get_view().get_download_gcc_btn()
            self.get_view().show_success_info('下载 GCC 成功', '请刷新环境变量(重启电脑)后点击上方的检测')
            btn.setEnabled(True)
            return

        self.t3 = RunInThread()
        self.t3.set_start_func(lambda: self.get_model().download_gcc())
        self.t3.set_finished_func(run)
        self.t3.start()

    @Slot()
    def finished_btn_clicked(self) -> None:
        """完成按钮点击事件"""
        # 安装第三方库
        self.module_manager.initialize()

        # 保存配置
        self.settings_manager.set(JsonSettings.FirstRun.value, False)
        self.finished.emit()
        self.get_view().close()

    @Slot()
    def bind(self) -> None:
        """绑定所有的信号槽"""
        self.pythonexe_by_hand_btn.clicked.connect(self.pythonexe_by_hand)
        self.pythonexe_auto_btn.clicked.connect(self.pythonexe_by_auto)
        self.default_pip_btn.clicked.connect(self.use_defualt_pip_source)
        self.auto_pip_btn.clicked.connect(self.use_auto_pip_source)
        self.detect_gcc_btn.clicked.connect(self.detect_gcc)
        self.download_gcc_btn.clicked.connect(self.download_gcc)
        self.get_view().get_finish_btn().clicked.connect(lambda: self.finished_btn_clicked())


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    p = WelcomePresenter()
    p.show()
    app.exec()
