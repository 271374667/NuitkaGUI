from __future__ import annotations

import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTreeView, QApplication, QAbstractItemView

from src.core.paths import PROJECT_DIR


@dataclass
class Item:
    def __init__(self, path: Optional[Path] = None,
                 check_state: Qt.CheckState = Qt.CheckState.Unchecked,
                 parent: Optional['Dir'] = None):
        self._id = uuid.uuid4()
        self._path: Path = path
        self._check_state: Qt.CheckState = check_state
        self._parent: Optional['Dir'] = parent
        self._size: Optional[int] = None

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def path(self) -> Optional[Path]:
        return self._path

    @property
    def parent(self) -> Optional['Dir']:
        return self._parent

    @parent.setter
    def parent(self, value: Optional['Dir']):
        if self._parent:
            self._parent.remove_child(self)
        self._parent = value
        self._parent.add_child(self)

    @property
    def check_state(self) -> Qt.CheckState:
        return self._check_state

    @check_state.setter
    def check_state(self, value: Qt.CheckState):
        self._check_state = value

    @property
    def size(self) -> Optional[int]:
        return self._size

    @size.setter
    def size(self, value: Optional[int]):
        self._size = value

    def __str__(self):
        return f'{self.__class__.__name__}(path={self._path}, check_state={self._check_state}, size={self._size})'


@dataclass
class Dir(Item):
    def __init__(self, path: Optional[Path] = None,
                 check_state: Qt.CheckState = Qt.CheckState.Unchecked,
                 parent: Optional['Dir'] = None, ):
        super().__init__(path, check_state, parent)
        self._children = []

    @property
    def children(self) -> list[Item]:
        return self._children

    @children.setter
    def children(self, value: list[Item]):
        self._children = value

    @property
    def size(self) -> int:
        return sum(child.size for child in self._children)

    @property
    def check_state(self) -> Qt.CheckState:
        checked_count = 0
        unchecked_count = 0
        for child in self._children:
            if child.check_state == Qt.CheckState.Checked:
                checked_count += 1
            elif child.check_state == Qt.CheckState.Unchecked:
                unchecked_count += 1

        if checked_count == len(self._children):
            return Qt.CheckState.Checked
        if unchecked_count == len(self._children):
            return Qt.CheckState.Unchecked
        return Qt.CheckState.PartiallyChecked

    @check_state.setter
    def check_state(self, value: Qt.CheckState):
        for child in self._children:
            child.check_state = value

        if self._parent:
            self._parent.check_state = self._parent.check_state

    def add_child(self, child: Item):
        self._children.append(child)
        child._parent = self

    def remove_child(self, child: Item):
        self._children.remove(child)
        child._parent = None

    def clear_children(self):
        for child in self._children:
            child.parent = None
        self._children.clear()

    def __str__(self):
        return f'{self.__class__.__name__}(path={self._path}, check_state={self._check_state}, size={self.size})'


@dataclass
class File(Item):
    def __init__(self, path: Optional[Path] = None,
                 check_state: Qt.CheckState = Qt.CheckState.Unchecked,
                 parent: Optional['Dir'] = None):
        super().__init__(path, check_state, parent)

    @property
    def size(self) -> int:
        return self._path.stat().st_size

    def __str__(self):
        return f'{self.__class__.__name__}(path={self._path}, check_state={self._check_state}, size={self._size})'


class FileSystemManager:
    def __init__(self, root_dir: Path = PROJECT_DIR):
        self._root_dir = root_dir
        self._root = Dir(root_dir)
        self.add_dir(root_dir)

    @property
    def root(self) -> Dir:
        return self._root

    def add_dir(self, path: Path, parent: Optional[Dir] = None) -> Dir:
        if not parent:
            parent = self._root

        if path.is_dir():
            dir_item = Dir(path, parent=parent)
            parent.add_child(dir_item)
            for child_path in path.iterdir():
                if child_path.is_dir():
                    self.add_dir(child_path, dir_item)
                else:
                    file_item = File(child_path, parent=dir_item)
                    dir_item.add_child(file_item)
        elif path.is_file():
            file_item = File(path, parent=parent)
            parent.add_child(file_item)

        return parent

    def _str_helper(self, dir_item: Dir, level: int) -> str:
        indent = '  ' * level
        result = f"{indent}{dir_item.path.name}/\n"
        for child in dir_item.children:
            if isinstance(child, Dir):
                result += self._str_helper(child, level + 1)
            else:
                result += f"{indent}  {child.path.name}\n"
        return result

    def __str__(self):
        return self._str_helper(self._root, 0)


class TreeModel(QStandardItemModel):
    def __init__(self, file_system_manager: FileSystemManager, parent=None):
        super().__init__(parent)
        self.file_system_manager = file_system_manager
        self.setHorizontalHeaderLabels(['文件名', '文件大小', '文件位置'])
        self.build_model()

    def build_model(self):
        root_item = self.invisibleRootItem()
        self._add_dir_to_model(self.file_system_manager.root, root_item)

    def _add_dir_to_model(self, dir_item: Dir, parent_item: QStandardItem):
        name_item, path_item, size_item = self._create_standard_item(dir_item)
        parent_item.appendRow([name_item, path_item, size_item])

        for child in dir_item.children:
            if isinstance(child, Dir):
                self._add_dir_to_model(child, name_item)
            else:
                file_standard_item = self._create_standard_item(child)
                name_item.appendRow(file_standard_item)

    def _create_standard_item(self, item: Item) -> Sequence[QStandardItem]:
        name_item = QStandardItem(item.path.name if item.path else '')
        path_item = QStandardItem(str(item.path) if item.path else '')
        size_item = QStandardItem(str(item.size) if item.size is not None else '')
        name_item.setCheckable(True)
        name_item.setCheckState(item.check_state)

        return name_item, path_item, size_item


class DraggableFileTreeWidget(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.file_system_manager = FileSystemManager(PROJECT_DIR)
        self.model = TreeModel(self.file_system_manager)
        self.setModel(self.model)


if __name__ == '__main__':
    app = QApplication([])
    tree_view = DraggableFileTreeWidget()
    tree_view.show()
    app.exec()
    # f = FileSystemManager()
    # print(f)
