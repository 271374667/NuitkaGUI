import os
import shutil
from pathlib import Path
from typing import Optional

import loguru
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog

from src.conf import config_path
from src.model.basic_model import BasicModel
from src.utils.run_in_thread import RunInThread
from src.view.basic_view import BasicView


# TODO: 两个按钮，然后现在的选择文件夹和选择输出文件夹的逻辑还有问题，需要修改
class BasicPresenter:
    def __init__(self):
        self._model = BasicModel()
        self._view = BasicView()

        # 只有在最后的时候才会对输出目录进行创建，不然每一次选择目录都会创建一个新的output
        self._output_dir: Optional[Path] = None

        self.bind()

    def get_model(self) -> BasicModel:
        return self._model

    def get_view(self) -> BasicView:
        return self._view

    @Slot(str)
    def droped_py_file(self, py_file: str) -> None:
        """拖拽文件到窗口的时候会触发这个函数"""
        if not py_file:
            return
        if not py_file.endswith('.py'):
            return

        # 设置 python 文件的状态
        self.get_view().set_py_file_status(True)
        self.get_view().show_success_info('选择 Python 文件成功', f'{Path(py_file).stem}.py 被选择', duration=1500)
        self.get_view().get_select_python_file().setToolTip(py_file)
        self.get_model().set_py_file(py_file)
        loguru.logger.debug(f'通过拖拽设置 Python 文件为:{py_file}')

        # 设置 output 的默认值
        self.get_view().get_output_path().setToolTip(str(self._get_default_output_dir()))  # 设置输出文件夹的默认值提示
        self.get_view().set_output_status(False)
        self.get_model().set_output_dir(str(self._get_default_output_dir()))

    @Slot()
    def select_py_file_btn_clicked(self) -> None:
        """选择 Python 文件按钮点击的时候会触发这个函数"""
        py_file, _ = QFileDialog.getOpenFileName(self.get_view(), '选择 Python 文件', '', 'Python 文件 (*.py)')
        loguru.logger.debug(f'选择 Python 文件为:{py_file}')

        if not py_file:
            # 设置 python 文件的状态
            self.get_view().show_error_info('未选择 Python 文件', '请选择一个需要被打包的 Python 文件', duration=1500)
            self.get_view().get_select_python_file().setToolTip('未选择 Python 文件')
            self.get_view().set_py_file_status(False)
            self.get_model().set_py_file('')

            # 设置输出文件夹
            self.get_view().get_output_path().setToolTip('未选择 Python 文件')
            self.get_view().set_output_status(False)  # 同时设置输出文件夹默认值
            self.get_model().set_output_dir('')
            loguru.logger.info('未选择 Python 文件')
            return

        # 显示各种状态提示控件，然后设置模型里面的数据，同时设置输出文件夹默认值
        self.get_view().show_success_info('选择 Python 文件成功', f'{Path(py_file).stem}.py 被选择', duration=1500)
        self.get_view().get_select_python_file().setToolTip(py_file)
        self.get_view().set_py_file_status(True)
        self.get_model().set_py_file(py_file)

        # 设置输出文件夹
        self.get_view().set_output_status(False)
        self.get_view().get_output_path().setToolTip(str(self._get_default_output_dir()))  # 设置输出文件夹的默认值提示
        loguru.logger.info(f'选择 Python 文件为:{py_file}')

    @Slot()
    def select_output_path_btn_clicked(self) -> None:
        """选择输出路径按钮点击的时候会触发这个函数"""
        output_path = QFileDialog.getExistingDirectory(self.get_view(), '选择输出路径', '')
        loguru.logger.debug(f'选择输出路径为:{output_path}')

        if not output_path:
            default_output_dir = self._get_default_output_dir()
            self.get_view().get_output_path().setToolTip(str(default_output_dir))
            self.get_view().set_output_status(False)
            self.get_model().set_output_dir(str(default_output_dir))
            loguru.logger.info('未选择输出路径')
            return
        self.get_view().get_output_path().setToolTip(output_path)
        self.get_view().set_output_status(True)
        self.get_model().set_output_dir(output_path)
        loguru.logger.info(f'选择输出路径为:{output_path}')

    @Slot(bool)
    def mode_changed(self, is_onefile: bool) -> None:
        """当打包模式改变的时候会触发这个函数"""
        self.get_model().set_onefile_mode(is_onefile)
        loguru.logger.info(f"打包模式改变为:{'单文件' if is_onefile else '文件夹'}")

    @Slot()
    def icon_selected_btn_clicked(self) -> None:
        """当选择图标按钮点击的时候会触发这个函数"""
        icon_file, _ = QFileDialog.getOpenFileName(self.get_view(), '选择图标', '', '图标文件 (*.ico)')
        loguru.logger.debug(f'选择图标为:{icon_file}')

        if not icon_file:
            self.get_view().show_error_info('未选择图标', '当前使用默认图标', duration=1500)
            self.get_view().get_icon().setToolTip('当前使用默认图标')
            self.get_view().set_icon_status(False)
            self.get_model().set_icon(str(config_path.ICO_FILE))
            return

        self.get_view().show_success_info('选择图标成功', icon_file, duration=1500)
        self.get_view().get_icon().setToolTip(icon_file)
        self.get_view().set_icon_status(True)
        self.get_model().set_icon(icon_file)
        loguru.logger.info(f'选择图标为:{icon_file}')

    @Slot()
    def start_btn_clicked(self) -> None:
        """开始打包的时候会触发这个函数"""
        py_file = self.get_model().get_py_file()
        if not py_file:
            self.get_view().show_error_info('未选择 Python 文件', '请选择一个需要被打包的 Python 文件', duration=1500)
            return

        # self._create_output_dir()
        # if not self.get_model().get_icon():
        #     # 先把 qrc 中的图标转换成 ico 文件保存到 output 目录下
        #     output_icon = self.get_model().rc_icon2local_ico(Path(self.get_model().get_output_dir()))
        #     self.get_model().set_icon(str(output_icon))

        def run():
            self._create_output_dir()
            if not self.get_model().get_icon():
                # 先把 qrc 中的图标转换成 ico 文件保存到 output 目录下
                output_icon = self.get_model().rc_icon2local_ico(Path(self.get_model().get_output_dir()))
                self.get_model().set_icon(str(output_icon))
            loguru.logger.info('开始打包')
            self.get_model().start()

        def finished_func():
            loguru.logger.info('打包完成')
            self.get_view().show_success_info('打包完成', '*.exe 可执行文件在输出目录的 .dist文件夹下', duration=-1)
            # 打开输出目录
            os.startfile(self.get_model().get_output_dir())

        self.t1 = RunInThread()
        self.t1.set_start_func(lambda: run())
        self.t1.set_finished_func(lambda: finished_func())
        self.t1.start()

    def _get_default_output_dir(self) -> Path:
        self._output_dir = Path(self.get_model().get_py_file()).parent / 'output'
        return self._output_dir

    def _create_output_dir(self) -> None:
        # 在运行 start 的时候记得调用这个函数，创建输出目录
        output_dir = Path(self.get_model().get_py_file()).parent / 'output'
        if output_dir.exists():
            shutil.rmtree(output_dir, ignore_errors=True)
        output_dir.mkdir(parents=True, exist_ok=True)

    def bind(self) -> None:
        self.get_view().get_mask().droped_file_url.connect(lambda x: self.droped_py_file(x))
        self.get_view().get_select_python_file().clicked.connect(self.select_py_file_btn_clicked)
        self.get_view().get_output_path().clicked.connect(self.select_output_path_btn_clicked)
        self.get_view().get_mode_radiobutton().checkedChanged.connect(self.mode_changed)
        self.get_view().get_start().clicked.connect(self.start_btn_clicked)
        self.get_view().get_icon().clicked.connect(self.icon_selected_btn_clicked)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    w = BasicPresenter().get_view()
    w.show()
    app.exec()
