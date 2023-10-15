from typing import List

from src.model.embed_model import EmbedModel
from src.utils.run_in_thread import RunInThread
from src.view.embed_view import EmbedView


class EmbedPresenter:
    def __init__(self):
        self._model = EmbedModel()
        self._view = EmbedView()

        self.bind()

    def get_view(self) -> EmbedView:
        return self._view

    def get_model(self) -> EmbedModel:
        return self._model

    def show(self) -> None:
        self.get_view().show()

    def get_cmd(self) -> List[str]:
        return self.get_model().get_cmd()

    def _load_filetree(self) -> None:
        py_file = self.get_model().get_py_file()
        if str(py_file) == '.':
            self.get_view().show_error_info('未选择 .py 文件', '请回到主页面选择需要打包的 .py 文件')
            return
        self.t = RunInThread()
        self.t.set_start_func(lambda: self.get_model().set_root_path(py_file.parent))
        self.t.start()

    def bind(self) -> None:
        self.get_model().set_file_tree(self.get_view().get_file_tree())
        self.get_view().get_open_new_dir_btn().clicked.connect(self._load_filetree)
        self.get_view().get_file_tree().itemClicked.connect(lambda: self.get_model().set_cmd(self.get_cmd()))


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from src.common.manager.command_manager import CommandManager
    from src.core import StrCommands

    cmd_manager = CommandManager()
    cmd_manager.set_option_value(StrCommands.main, r'E:\load\python\MyWheel\nuitkaGUI\githubOpenSource2\src\core.py')
    print(cmd_manager.get_option_value(StrCommands.main))
    print(cmd_manager.get_cmd())

    app = QApplication([])
    presenter = EmbedPresenter()
    presenter.show()
    app.exec()
