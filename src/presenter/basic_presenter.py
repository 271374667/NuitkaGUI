import time
from pathlib import Path

import loguru
from PySide6.QtWidgets import QApplication, QFileDialog

from src.model.basic_model import BasicModel
from src.signal_bus import SignalBus
from src.utils.singleton import singleton
from src.utils.thread_utils import RunInThread
from src.utils.window_explorer_utils import WindowExplorerUtils
from src.view.basic_view import BasicView


@singleton
class BasicPresenter:
    def __init__(self):
        self._view = BasicView()
        self._model = BasicModel()

        self._window_explorer_utils = WindowExplorerUtils()
        self._signal_bus = SignalBus()

        self.bind()

    @property
    def view(self) -> BasicView:
        return self._view

    @property
    def model(self) -> BasicModel:
        return self._model

    def _source_script_changed(self, drop_file_url: str):
        drop_file_path: Path = Path(drop_file_url)

        if not drop_file_path.exists():
            self._view.show_warning_infobar('错误', f'文件不存在:{drop_file_url}')
            self._view.source_script_path = None
            self._model.source_script_path = None
            return

        if Path(drop_file_url).suffix != '.py':
            self._view.show_warning_infobar('错误', '只能拖入.py文件')
            self._view.source_script_path = None
            self._model.source_script_path = None
            return

        self._view.source_script_path = drop_file_path
        self._model.source_script_path = drop_file_path
        self._view.output_dir = self._get_output_dir_path()
        self._model.output_dir = self._get_output_dir_path()
        self._view.show_success_infobar('成功', f'已选择文件:{drop_file_path.name}', duration=2000)

        # 拖入文件后自动选择输出路径
        self._output_dir_changed(is_show_dialog=False)

        # 识别是否使用虚拟环境,如果有则使用虚拟环境中的Python.exe
        project_python_exe = self._window_explorer_utils.find_files_in_dir_recursive(drop_file_path.parent,
                                                                                     'python.exe',
                                                                                     WindowExplorerUtils.FileType.FILES)
        if project_python_exe:
            loguru.logger.debug(f'找到可用的python.exe地址: {project_python_exe}')
            project_python_exe = project_python_exe[0]
            if Path(project_python_exe).is_relative_to(drop_file_path.parent):
                self._view.show_mask_dialog('已找到项目Python.exe',
                                            f'我们发现您正在使用虚拟环境,是否使用项目中的Python.exe?\n{project_python_exe}')
                self._model.project_python_exe_path = project_python_exe
            else:
                self._model.project_python_exe_path = None
            self._signal_bus.update_setting_view.emit()

    def _open_file_dialog(self):
        py_file, _ = QFileDialog.getOpenFileName(self._view, '选择 Python 文件', '', 'Python 文件 (*.py)')
        loguru.logger.debug(f'选择 Python 文件为:{py_file}')

        if not py_file:
            self._view.show_warning_infobar('错误', '未选择任何文件')
            self._view.source_script_path = None
            self._model.source_script_path = None
            return

        self._view.source_script_path = Path(py_file)
        self._model.source_script_path = Path(py_file)
        self._view.output_dir = self._get_output_dir_path()
        self._model.output_dir = self._get_output_dir_path()
        self._view.show_success_infobar('成功', f'已选择文件:{self._view.source_script_path.name}', duration=2000)

    def _output_dir_changed(self, is_show_dialog: bool = True):
        """选择输出路径按钮点击的时候会触发这个函数"""
        if self._model.source_script_path is None:
            self._view.show_warning_infobar('错误', '请先选择 Python 文件')
            return

        if is_show_dialog:
            output_path = QFileDialog.getExistingDirectory(self._view, '选择输出路径', '')
            loguru.logger.debug(f'选择输出路径为:{output_path}')
        else:
            output_path = self._get_output_dir_path()

        if not output_path:
            self._view.output_dir = self._get_output_dir_path()
            self._view.show_warning_infobar('错误', '未选择任何文件夹,已自动选择')
            return

        self._view.output_dir = Path(output_path)
        self._model.output_dir = Path(output_path)
        loguru.logger.info(f'选择输出路径为:{output_path}')

    def _icon_changed(self):
        """选择图标按钮点击的时候会触发这个函数"""
        icon_path, _ = QFileDialog.getOpenFileName(self._view, '选择图标文件', '', '图标文件 (*.ico)')
        loguru.logger.debug(f'选择图标文件为:{icon_path}')

        if not icon_path:
            self._view.icon_path = None
            self._model.icon_path = None
            self._view.show_warning_infobar('错误', '未选择任何文件')
            return

        self._view.icon_path = Path(icon_path)
        self._model.icon_path = Path(icon_path)
        self._view.show_success_infobar('成功', f'已选择图标文件:{self._view.icon_path.name}', duration=2000)

    def _packaged_mode_changed(self):
        """打包模式改变的时候会触发这个函数"""
        current_mode = self._view.get_mode_radiobutton().isChecked()
        if current_mode:
            self._model.packaged_mode = 'onefile'
        else:
            self._model.packaged_mode = 'standalone'

    def _get_output_dir_path(self) -> Path:
        if self._model.source_script_path is None:
            return Path.cwd() / 'output'
        return self._model.source_script_path.parent / 'output'

    def _start(self):
        if self._model.source_script_path is None:
            self._view.show_warning_infobar('错误', '请先选择 Python 文件')
            return

        def start():
            return self._model.start()

        def finished(is_success: bool):
            if not is_success:
                self._view.show_error_infobar('错误', '打包任务失败')
                self._view.finish_state_tooltip('失败', '打包任务失败')
                return

            self._view.show_success_infobar('完成', f'打包任务完成,任务总耗时:{time.time() - start_time:.2f}s',
                                            duration=-1, is_closable=True)
            self._view.finish_state_tooltip('就绪', '打包已经完成')

        self._start_thread = RunInThread()
        self._start_thread.set_start_func(start)
        self._start_thread.set_finished_func(finished)
        self._start_thread.start()
        self._view.show_state_tooltip('运行中...', '正在打包中,请稍等')
        start_time = time.time()

    def bind(self):
        self._view.get_mask().droped_file_url.connect(self._source_script_changed)
        self._view.get_source_script_btn().clicked.connect(self._open_file_dialog)
        self._view.get_output_path_btn().clicked.connect(self._output_dir_changed)
        self._view.get_icon_btn().clicked.connect(self._icon_changed)
        self._view.get_mode_radiobutton().checkedChanged.connect(self._packaged_mode_changed)
        self._view.get_start_btn().clicked.connect(self._start)


if __name__ == '__main__':
    app = QApplication([])
    presenter = BasicPresenter()
    presenter.view.show()
    app.exec()
