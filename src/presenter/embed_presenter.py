from pathlib import Path

import loguru
from PySide6.QtWidgets import QApplication

from src.model.embed_model import EmbedModel
from src.utils.thread_utils import RunInThread
from src.view.embed_view import EmbedView


class EmbedPresenter:
    def __init__(self):
        self._view = EmbedView()
        self._model = EmbedModel()

        self.bind()

    @property
    def view(self) -> EmbedView:
        return self._view

    @property
    def model(self) -> EmbedModel:
        return self._model

    def bind(self):
        self._view.get_load_dir_btn().clicked.connect(self._load_dir)
        self._view.get_file_tree().clicked.connect(self.write_nuitka_cmd)

    def get_nuitka_cmd(self) -> tuple[list[str], list[str]]:
        """生成Nuitka命令

        Returns:
            list[str]: 文件列表
            list[str]: 文件夹列表
        """
        return self._view.get_file_tree().get_nuitka_cmd()

    def write_nuitka_cmd(self):
        source_script_path = self._model.source_script_path
        if not source_script_path:
            self._view.show_warning_infobar("错误", "请先选择源文件", 1000, is_closable=True)
            return

        files, dirs = self.get_nuitka_cmd()
        self._model.set_include_data_files(files)
        self._model.set_include_data_dir(dirs)
        loguru.logger.debug(f"写入嵌入式文件列表和文件夹列表,文件列表:{files},文件夹列表:{dirs}")

    def _load_dir(self):
        source_script_path: Path = self._model.source_script_path
        if source_script_path is None:
            self._view.show_warning_infobar("错误", "请先选择源文件", 1000, is_closable=True)
            return

        def run():
            self._view.get_file_tree().clear()
            self._view.get_file_tree().set_root_path(source_script_path.parent)

        def finished():
            self._view.finish_state_tooltip("完成", "打包文件的项目目录加载完成")

        self._view.show_state_tooltip("加载中...", '正在加载打包文件的项目目录')
        self.t = RunInThread()
        self.t.set_start_func(run)
        self.t.set_finished_func(finished)
        self.t.start()


if __name__ == '__main__':
    app = QApplication([])
    view = EmbedPresenter()
    view.model.source_script_path = Path(r"E:\load\python\Project\nuitkaGUIOld\githubOpenSource2\main.py")
    view.view.show()
    app.exec()
