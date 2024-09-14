from pathlib import Path

import loguru
from PySide6.QtWidgets import QApplication, QFileDialog

from src.model.basic_model import BasicModel
from src.view.basic_view import BasicView


class BasicPresenter:
    def __init__(self):
        self._view = BasicView()
        self._model = BasicModel()

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

    def _output_dir_changed(self):
        """选择输出路径按钮点击的时候会触发这个函数"""
        if self._model.source_script_path is None:
            self._view.show_warning_infobar('错误', '请先选择 Python 文件')
            return

        output_path = QFileDialog.getExistingDirectory(self._view, '选择输出路径', '')
        loguru.logger.debug(f'选择输出路径为:{output_path}')

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
        return self._model.source_script_path.parent / 'output'

    def bind(self):
        self._view.get_mask().droped_file_url.connect(self._source_script_changed)
        self._view.get_source_script_btn().clicked.connect(self._open_file_dialog)
        self._view.get_output_path_btn().clicked.connect(self._output_dir_changed)
        self._view.get_icon_btn().clicked.connect(self._icon_changed)
        self._view.get_mode_radiobutton().checkedChanged.connect(self._packaged_mode_changed)


if __name__ == '__main__':
    app = QApplication([])
    presenter = BasicPresenter()
    presenter.view.show()
    app.exec()
