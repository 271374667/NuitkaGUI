from pathlib import Path
from typing import List, Tuple

import loguru
from PySide6.QtWidgets import QApplication
from qfluentwidgets import Flyout

from src.common.nuitka_command.command_manager import CommandManager
from src.model.plugin_model import PluginModel
from src.utils.thread_utils import RunInThread
from src.view.plugin_view import PluginView


class PluginPresenter:
    def __init__(self):
        self._view = PluginView()
        self._model = PluginModel()
        self.flyout = self._view.get_flyout()
        self._command_manager = CommandManager()
        self._plugins_enable_by_default: List[Tuple[str, bool]] = []

        # 多线程往界面中添加插件，防止界面卡顿
        self._view.show_info_infobar('正在获取插件列表', '请稍等...', duration=1000)
        self.init_thread = RunInThread()
        self.init_thread.set_start_func(self.model.fetch_plugin_from_cmd)
        self.init_thread.set_finished_func(self.put_command_to_view)
        self.init_thread.start()
        self.bind()

    @property
    def view(self) -> PluginView:
        return self._view

    @property
    def model(self) -> PluginModel:
        return self._model

    def put_command_to_view(self, plugins: List[tuple[str, str]]) -> None:
        if plugins == [('', '')]:
            self.view.show_error_infobar('您的NuitkaGUI无法使用',
                                         '请检查您的 nuitka 是否正常安装')
            return
        # 从命令行读取插件后添加到界面中
        for title, desc in plugins:
            plugin = self._view.add_plugin(title, desc)
            plugin.card_clicked.connect(self._model.set_plugin_status)
            if title in self._model.get_enable_plugins():
                plugin.checked = True
        self._set_plugins_status(self._plugins_enable_by_default)

    def auto_detect(self) -> None:
        py_file = self._model.get_source_script()
        if not py_file:
            self._view.show_error_infobar('错误', '请先前往主界面选择一个需要打包的py文件')
            return
        self._view.disable_all_plugin()
        self._model.disable_all_plugin()

        def run():
            return self._model.get_all_packages_by_py_file(Path(py_file))

        def finished_func(plugins_detected: List[str]):
            self._view.enable_plugins(plugins_detected)
            self._view.show_success_infobar('自动检测成功', f'自动检测到{plugins_detected}', duration=3000)
            loguru.logger.debug(f'自动检测到的插件: {plugins_detected}')

        self.t = RunInThread()
        self.t.set_start_func(lambda: run())
        self.t.set_finished_func(lambda x: finished_func(x))
        self.t.start()

    def update_value_to_command_manager(self, plugin_name: str, is_selected: bool) -> None:
        plugin_command = self._command_manager.get_command_by_command('enable-plugins')
        if plugin_command is None:
            return

        self.model.set_plugin_status(plugin_name, is_selected)
        plugin_command.value = self.model.get_enable_plugins()

    def update_widget(self) -> None:
        enabled_plugins = self._model.get_enable_plugins()
        for i in enabled_plugins:
            self._view.set_plugin_status(i, True)

    def _set_plugins_status(self, plugins: List[Tuple[str, bool]]) -> None:
        for each in plugins:
            self.view.set_plugin_status(each[0], each[1])

    def _show_current_selected(self) -> None:
        current_selected = self.model.get_enable_plugins()
        if len(current_selected) == 0:
            self._view.show_warning_infobar('警告', '当前未选择任何插件', duration=1000, is_closable=True)
            return

        self.flyout.clear()
        self.flyout.add_plugins(current_selected)
        Flyout.make(self.flyout, target=self._view.get_selected_btn(), parent=self._view, isDeleteOnClose=False)

    def bind(self):
        self.view.get_auto_btn().clicked.connect(self.auto_detect)
        self.view.get_selected_btn().clicked.connect(self._show_current_selected)
        self.view.card_clicked.connect(self.update_value_to_command_manager)


if __name__ == '__main__':
    app = QApplication([])
    presenter = PluginPresenter()
    presenter._command_manager.source_script = Path(r"E:\load\python\Project\nuitkaGUIOld\githubOpenSource2\main.py")
    presenter.view.show()
    app.exec()
