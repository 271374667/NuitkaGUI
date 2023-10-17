from pathlib import Path
from typing import List, Tuple

import loguru
from PySide6.QtCore import Slot
from qmaterialwidgets.components import Flyout

from src.core import Plugin
from src.model.plugin_model import PluginModel
from src.utils.run_in_thread import RunInThread
from src.utils.singleton import Singleton
from src.view.plugin_view import PluginView


@Singleton
class PluginPresenter:
    def __init__(self):
        self._model = PluginModel()
        self._view = PluginView()
        self.flyout = self.get_view().get_flyout()

        self._plugins_enable_by_default: List[Tuple[Plugin, bool]] = []

        # 多线程往界面中添加插件，防止界面卡顿
        self.get_view().show_info('正在获取插件列表', '请稍等...', duration=1000)
        self.init_thread = RunInThread()
        self.init_thread.set_start_func(self.get_model().fetch_plugin_from_cmd)
        self.init_thread.set_finished_func(self.put_command_to_view)
        self.init_thread.start()
        self.bind()

    def get_model(self) -> PluginModel:
        return self._model

    def get_view(self) -> PluginView:
        return self._view

    def get_cmd(self) -> List[str]:
        return self.get_model().get_cmd()

    def set_plugins_status(self, plugins: List[Tuple[Plugin, bool]]) -> None:
        """设置插件的状态
        Args:
            plugins: 插件的状态
                    第一个元素是插件的枚举，通过 core.Plugin 设置
                    第二个元素是插件的状态

        Returns:
            None
        """
        self._plugins_enable_by_default = plugins

    @Slot()
    def auto_detect(self) -> None:
        py_file = self.get_model().get_py_file()
        if not py_file:
            self.get_view().show_error_info('错误', '请先前往主界面选择一个需要打包的py文件')
            return
        self.get_view().disable_all_plugin()

        def run():
            return self.get_model().get_all_packages_by_py_file(Path(py_file))

        def finished_func(plugins_detected: List[str]):
            self.get_view().enable_plugins(plugins_detected)
            self.get_view().show_success_info('自动检测成功', f'自动检测到{plugins_detected}', duration=3000)
            loguru.logger.debug(f'自动检测到的插件: {plugins_detected}')

        self.t = RunInThread()
        self.t.set_start_func(lambda: run())
        self.t.set_finished_func(lambda x: finished_func(x))
        self.t.start()

    @Slot()
    def show_current_selected(self) -> None:
        current_selected = self.get_model().get_selected_plugins()
        if len(current_selected) == 0:
            self.get_view().show_warning_info('警告', '当前未选择任何插件', duration=1000)
            return

        self.flyout.clear()
        self.flyout.add_plugins(current_selected)
        Flyout.make(self.flyout, target=self.get_view().get_selected_btn(), parent=self.get_view())

    @Slot()
    def bind(self) -> None:
        self.get_view().get_auto_btn().clicked.connect(self.auto_detect)
        self.get_view().get_selected_btn().clicked.connect(self.show_current_selected)

    @Slot(list)
    def put_command_to_view(self, plugins: List[tuple[str, str]]) -> None:
        if plugins == [('', '')]:
            self.get_view().show_error_info('您的NuitkaGUI无法使用',
                                            '请检查您的 nuitka 是否正常安装')
            return
        # 从命令行读取插件后添加到界面中
        for title, desc in plugins:
            plugin = self._view.add_plugin(title, desc)
            plugin.plugin_changed.connect(self._model.set_plugin_status)
        self._set_plugins_status(self._plugins_enable_by_default)

    def _set_plugins_status(self, plugins: List[Tuple[Plugin, bool]]) -> None:
        for each in plugins:
            self.get_view().set_plugin_status(each[0].value, each[1])


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    presenter: PluginPresenter = PluginPresenter()
    presenter.get_view().show()
    presenter.set_plugins_status([(Plugin.UPX, True), (Plugin.PYSIDE6, True)])
    app.exec()
