from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import loguru
from PySide6.QtCore import QFileInfo, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileIconProvider,
    QMenu,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
)
from qfluentwidgets.components import RoundMenu
from src.core import settings
from src.utils.window_explorer_utils import WindowExplorerUtils


@dataclass
class PathData:
    name: str
    absolute_path: str
    relative_path: str
    type: str


class EmbedFileTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._window_explorer_utils = WindowExplorerUtils()
        self._drop_dir_root: Optional[Path] = None

        # 初始化控件
        self._setup_ui()

        # 信号与槽
        self.itemChanged.connect(self._on_item_changed)

    def set_root_path(self, path: Path):
        """设置根目录"""
        self.root_path = path
        self.root_node = self.invisibleRootItem()
        self.clear()
        self._load_directory(Path(path), self.root_node)
        loguru.logger.debug(f'文件树加载完成，共加载 {self.file_count} 个文件')

    def get_all_path(self) -> List[PathData]:
        """获取所有被选中的节点的路径"""
        path_list = []
        iterator = QTreeWidgetItemIterator(self)
        while iterator.value():
            item = iterator.value()
            if item.checkState(0) == Qt.CheckState.Checked:
                path_list.append(PathData(
                    item.text(0),
                    item.text(1).replace('\\', '/'),
                    item.text(2).replace('\\', '/'),
                    item.text(3),
                ))
            iterator += 1
        return path_list

    def get_nuitka_cmd(self) -> tuple[list[str], list[str]]:
        """生成Nuitka命令

        Returns:
            list[str]: 文件列表
            list[str]: 文件夹列表
        """
        selected_path_list = self.get_all_path()
        files_cmd_list: list[str] = []
        dirs_cmd_list: list[str] = []
        last_dir = ''
        for each in selected_path_list:
            if each.type == '文件夹':
                if each.relative_path.startswith(last_dir) and last_dir:
                    continue
                last_dir = each.relative_path
                dirs_cmd_list.append(f'{each.absolute_path}={each.relative_path}')
            elif each.type == '文件':
                if each.relative_path.startswith(last_dir) and last_dir:
                    continue
                files_cmd_list.append(f'{each.absolute_path}={each.relative_path}')
        return files_cmd_list, dirs_cmd_list

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                path = Path(url.toLocalFile())
                if path.is_dir():
                    self._handle_drop_dir(path)
                else:
                    self._handle_drop_file(path)
            event.accept()
        else:
            event.ignore()

    def _setup_ui(self):
        """初始化UI"""
        self.setWindowTitle('文件树')
        self.icon_provider = QFileIconProvider()
        self.root_path = Path.cwd()
        self.root_node = self.invisibleRootItem()
        self.default_checked = Qt.CheckState.Unchecked
        self.file_count = 0
        self._setup_header()
        self._setup_drag_and_drop()
        self._setup_context_menu()

    def _setup_header(self):
        """设置表头"""
        self.setHeaderLabels(['名称', '绝对路径', '相对路径', '类型'])
        self.setColumnCount(4)
        self.setSizeAdjustPolicy(QTreeWidget.SizeAdjustPolicy.AdjustToContents)
        self.setSelectionBehavior(QTreeWidget.SelectionBehavior.SelectRows)
        self.header().setStretchLastSection(True)
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 300)
        self.setColumnWidth(2, 200)

    def _setup_drag_and_drop(self):
        """设置拖拽属性"""
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QTreeWidget.DragDropMode.DragDrop)

    def _setup_context_menu(self):
        """设置右键菜单"""
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._open_menu)

    def _handle_drop_dir(self, path: Path):
        """处理拖拽到的文件夹"""
        self._drop_dir_root = path.parent
        child = QTreeWidgetItem(self.root_node, [path.name, str(path.resolve()), path.name, '文件夹'])
        child.setCheckState(0, self.default_checked)
        child.setIcon(0, self.icon_provider.icon(QFileIconProvider.IconType.Folder))
        self._load_directory(path, child, True)

    def _handle_drop_file(self, path: Path):
        """处理拖拽到的文件"""
        child = QTreeWidgetItem(self.root_node, [path.name, str(path.resolve()), path.name, '文件'])
        child.setCheckState(0, self.default_checked)
        child.setIcon(0, QIcon(self.icon_provider.icon(QFileInfo(path.resolve()))))

    def _load_directory(self, path: Path, parent: QTreeWidgetItem, is_drop: bool = False):
        """递归加载目录及其子目录到树中"""
        if not path.exists():
            return

        for entry in path.iterdir():
            if entry.is_dir():
                self._load_directory_entry(entry, parent, is_drop)
            else:
                self.file_count += 1
                self._create_file_item(entry, parent, is_drop)

    def _load_directory_entry(self, entry: Path, parent: QTreeWidgetItem, is_drop: bool):
        """加载目录条目"""
        if is_drop and entry.name in {".", ".."}:
            return

        if not is_drop:
            child = QTreeWidgetItem(parent, [entry.name, str(entry.resolve()),
                                             str(entry.relative_to(self.root_path)), '文件夹'])
        else:
            child = QTreeWidgetItem(parent, [entry.name, str(entry.resolve()),
                                             str(entry.relative_to(self._drop_dir_root)), '文件夹'])

        child.setCheckState(0, self.default_checked)
        child.setIcon(0, self.icon_provider.icon(QFileIconProvider.IconType.Folder))

        if not self._should_load_directory(entry):
            return

        self._load_directory(entry, child, is_drop)

    def _create_file_item(self, entry: Path, parent: QTreeWidgetItem, is_drop: bool):
        """创建文件条目"""
        if not is_drop:
            child = QTreeWidgetItem(parent, [entry.name, str(entry.resolve()),
                                             str(entry.relative_to(self.root_path)), '文件'])
        else:
            child = QTreeWidgetItem(parent, [entry.name, str(entry.resolve()),
                                             str(entry.relative_to(self._drop_dir_root)), '文件'])

        child.setCheckState(0, self.default_checked)
        child.setIcon(0, QIcon(self.icon_provider.icon(QFileInfo(entry.resolve()))))

    def _should_load_directory(self, entry: Path) -> bool:
        """判断是否应该加载目录"""
        if any(i in entry.stem for i in settings.IGNORE_DIRS):
            loguru.logger.debug(f'忽略文件夹: {entry.resolve()}')
            return False
        if self._window_explorer_utils.get_dir_files_count(entry, WindowExplorerUtils.FileType.FILES) == 0:
            loguru.logger.debug(f'空文件夹: {entry.resolve()}')
            return False
        if self._window_explorer_utils.get_dir_files_count(
                entry, WindowExplorerUtils.FileType.FILES) > settings.MAX_FILES_IN_DIR:
            loguru.logger.debug(f'文件夹内文件过多: {entry.resolve()}')
            return False
        return True

    def _open_menu(self, position):
        """打开右键菜单"""
        menu = RoundMenu()
        delete_action = QAction('删除该节点', self)
        delete_action.triggered.connect(self._delete_node)
        show_cmd_action = QAction('显示Nuitka命令', self)
        show_cmd_action.triggered.connect(lambda: loguru.logger.debug(self.get_nuitka_cmd()))
        menu.addAction(delete_action)
        menu.addAction(show_cmd_action)
        menu.exec(self.viewport().mapToGlobal(position))

    def _delete_node(self):
        """删除节点"""
        selected_indexes = self.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            self.model().removeRow(selected_index.row(), selected_index.parent())

    def _on_item_changed(self, item: QTreeWidgetItem, column: int):
        """处理条目状态变化"""
        if column != 0:
            return

        if item.parent() is None:
            if item.checkState(0) == Qt.CheckState.Checked:
                self._check_child(item)
            elif item.checkState(0) == Qt.CheckState.Unchecked:
                self._uncheck_child(item)
        else:
            if item.checkState(0) == Qt.CheckState.Checked:
                self._check_parent(item)
                self._check_child(item)
            elif item.checkState(0) == Qt.CheckState.Unchecked:
                self._uncheck_parent(item)
                self._uncheck_child(item)
            if self._is_all_childs_checked(item) is False:
                self._partially_check_parent(item)

    def _is_all_childs_checked(self, parent_item: QTreeWidgetItem) -> bool:
        """判断子节点是否全部勾选"""
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            if child_item.checkState(0) != Qt.CheckState.Checked:
                return False
            if child_item.childCount() > 0 and not self._is_all_childs_checked(child_item):
                return False
        return True

    def _check_child(self, parent_item: QTreeWidgetItem):
        """勾选子节点"""
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            child_item.setCheckState(0, Qt.CheckState.Checked)
            if child_item.childCount() > 0:
                self._check_child(child_item)

    def _uncheck_child(self, parent_item: QTreeWidgetItem):
        """取消勾选子节点"""
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            child_item.setCheckState(0, Qt.CheckState.Unchecked)
            if child_item.childCount() > 0:
                self._uncheck_child(child_item)

    def _check_parent(self, child_item: QTreeWidgetItem):
        """勾选父节点"""
        parent_item = child_item.parent()
        if parent_item is None:
            return

        all_checked = all(parent_item.child(i).checkState(0) != Qt.CheckState.Unchecked
                          for i in range(parent_item.childCount()))
        parent_item.setCheckState(0, Qt.CheckState.Checked if all_checked else Qt.CheckState.PartiallyChecked)

        if parent_item.parent() is not None:
            self._check_parent(parent_item)

    def _uncheck_parent(self, child_item: QTreeWidgetItem):
        """取消勾选父节点"""
        parent_item = child_item.parent()
        if parent_item is None:
            return

        all_unchecked = all(parent_item.child(i).checkState(0) == Qt.CheckState.Unchecked
                            for i in range(parent_item.childCount()))
        parent_item.setCheckState(0, Qt.CheckState.Unchecked if all_unchecked else Qt.CheckState.PartiallyChecked)

        if parent_item.parent() is not None:
            self._uncheck_parent(parent_item)

    def _partially_check_parent(self, child_item: QTreeWidgetItem):
        """部分勾选父节点"""
        parent_item = child_item.parent()
        if parent_item is None:
            return
        parent_item.setCheckState(0, Qt.CheckState.PartiallyChecked)

        if parent_item.parent() is not None:
            self._partially_check_parent(parent_item)


if __name__ == '__main__':
    from src.core.paths import PROJECT_DIR

    app = QApplication([])
    file_tree = EmbedFileTree()
    file_tree.set_root_path(PROJECT_DIR)
    file_tree.show()
    app.exec()
