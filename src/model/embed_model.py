from pathlib import Path
from typing import Optional

from src.common.manager.command_manager import CommandManager
from src.component.embedFileTree import EmbedFileTree
from src.core import StrCommands


class EmbedModel:
    def __init__(self):
        self.command_manager = CommandManager()
        self.file_tree: Optional[EmbedFileTree] = None

    def set_file_tree(self, file_tree: EmbedFileTree) -> None:
        self.file_tree = file_tree

    def set_root_path(self, path: Path) -> None:
        """设置根目录"""
        self.file_tree.set_root_path(path)

    def get_cmd(self) -> list[str]:
        """获取生成的命令"""
        return self.file_tree.get_nuitka_cmd()

    def get_py_file(self) -> Path:
        return Path(self.command_manager.get_option_value(StrCommands.main))

    def get_project_path(self) -> Path:
        return Path(self.get_py_file()).parent


if __name__ == '__main__':
    embed_model = EmbedModel()
    print(embed_model.get_py_file() == '')
