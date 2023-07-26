from pathlib import Path
import typing
import threading
from dataclasses import dataclass


from PySide6.QtCore import QFileInfo, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QFileIconProvider, QMenu,
                               QTreeWidget, QTreeWidgetItem,
                               QTreeWidgetItemIterator)


@dataclass
class PathData:
    name: str
    absolute_path: str
    relative_path: str
    type: str


class FileTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # 类相关
        self.setWindowTitle('文件树')
        # 初始化变量
        self.icon_provider = QFileIconProvider()
        self.root_path = Path.cwd()  # 默认根目录
        self.root_node = self.invisibleRootItem()  # 树形控件的根节点
        self.default_checked = Qt.CheckState.Unchecked  # 默认选中状态
        # 设置表头
        self.setHeaderLabels(['名称', '绝对路径', '相对路径', '类型'])
        self.setColumnCount(4)
        self.setSizeAdjustPolicy(QTreeWidget.SizeAdjustPolicy.AdjustToContents)
        self.setSelectionBehavior(QTreeWidget.SelectionBehavior.SelectRows)
        self.header().setStretchLastSection(True)
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 300)
        self.setColumnWidth(2, 200)
        # 设置拖拽
        # 设置右键菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__open_menu)
        # 逻辑初始化
        # self.__load_directory(self.root_path, self.root_node)
        # 信号与槽
        self.itemChanged.connect(self.__on_item_changed)

    def __load_directory(self, path: Path, parent: QTreeWidgetItem):
        """
        函数“load_directory”递归地将目录及其子目录加载到 QTreeWidget 中，并为每个条目设置检查状态和图标。

        :param path: `path` 参数是您要加载的目录路径。它代表要从中加载文件和子目录的目录。
        :param parent: “parent”参数是对树小部件中父项的引用。它用于将子项目添加到父项目。
        """
        print(path)
        if Path(path).exists() is False:
            return
        for entry in Path(path).iterdir():
            if entry.is_dir():
                child = QTreeWidgetItem(parent, [entry.name, str(
                    entry.resolve()), str(entry.relative_to(self.root_path)), '文件夹'])
                child.setCheckState(0, self.default_checked)
                child.setIcon(0, self.icon_provider.icon(
                    QFileIconProvider.IconType.Folder))
                self.__load_directory(entry, child)
            else:
                child = QTreeWidgetItem(parent, [entry.name, str(
                    entry.resolve()), str(entry.relative_to(self.root_path)), '文件'])
                child.setCheckState(0, self.default_checked)
                child.setIcon(
                    0, QIcon(self.icon_provider.icon(QFileInfo(entry.resolve()))))

    def __delete_node(self):
        """删除节点"""
        selected_indexes = self.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            # 删除节点
            self.model().removeRow(selected_index.row(), selected_index.parent())

    def __open_menu(self, position):
        """打开右键菜单"""
        menu = QMenu()
        delete_action = QAction('删除该节点', self)
        delete_action.triggered.connect(self.__delete_node)

        # show_cmd_action = QAction('显示命令', self)
        # show_cmd_action.triggered.connect(lambda: print(self.get_nuitka_cmd()))

        menu.addAction(delete_action)
        # menu.addAction(show_cmd_action)
        menu.exec(self.viewport().mapToGlobal(position))

    def __check_child(self, parent_item: QTreeWidgetItem):
        """勾选子节点"""
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            child_item.setCheckState(0, Qt.CheckState.Checked)
            if child_item.childCount() > 0:
                self.__check_child(child_item)

    def __uncheck_child(self, parent_item: QTreeWidgetItem):
        """取消勾选子节点"""
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            child_item.setCheckState(0, Qt.CheckState.Unchecked)
            if child_item.childCount() > 0:
                self.__uncheck_child(child_item)

    def __check_parent(self, child_item: QTreeWidgetItem):
        """勾选父节点"""
        parent_item = child_item.parent()
        if parent_item is None:
            return
        all_checked = True
        for i in range(parent_item.childCount()):
            if parent_item.child(i).checkState(0) == Qt.CheckState.Unchecked:
                all_checked = False
                break
        if all_checked:
            parent_item.setCheckState(0, Qt.CheckState.Checked)
        else:
            parent_item.setCheckState(0, Qt.CheckState.PartiallyChecked)
        if parent_item.parent() is not None:
            self.__check_parent(parent_item)

    def __uncheck_parent(self, child_item: QTreeWidgetItem):
        """取消勾选父节点"""
        parent_item = child_item.parent()
        if parent_item is None:
            return
        all_unchecked = True
        for i in range(parent_item.childCount()):
            if parent_item.child(i).checkState(0) != Qt.CheckState.Unchecked:
                all_unchecked = False
                break
        if all_unchecked:
            parent_item.setCheckState(0, Qt.CheckState.Unchecked)
        else:
            parent_item.setCheckState(0, Qt.CheckState.PartiallyChecked)
        if parent_item.parent() is not None:
            self.__uncheck_parent(parent_item)

    def __partially_check_parent(self, child_item: QTreeWidgetItem):
        """部分勾选父节点"""
        parent_item = child_item.parent()
        if parent_item is None:
            return
        parent_item.setCheckState(0, Qt.CheckState.PartiallyChecked)
        if parent_item.parent() is not None:
            self.__partially_check_parent(parent_item)

    def __on_item_changed(self, item: QTreeWidgetItem, column: int):
        if column != 0:
            return
        if item.parent() is None:
            if item.checkState(0) == Qt.CheckState.Checked:
                self.__check_child(item)
            elif item.checkState(0) == Qt.CheckState.Unchecked:
                self.__uncheck_child(item)
        else:
            if item.checkState(0) == Qt.CheckState.Checked:
                self.__check_parent(item)
                self.__check_child(item)
            elif item.checkState(0) == Qt.CheckState.Unchecked:
                self.__uncheck_parent(item)
                self.__uncheck_child(item)
            if self.__is_all_childs_checked(item) is False:
                self.__partially_check_parent(item)

    def __is_all_childs_checked(self, parent_item: QTreeWidgetItem):
        """判断子节点是否全部勾选"""
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            if child_item.checkState(0) != Qt.CheckState.Checked:
                return False
            if child_item.childCount() > 0 and self.__is_all_childs_checked(child_item) is False:
                return False
        return True

    def get_parent_node(self, node: QTreeWidgetItem) -> QTreeWidgetItem:
        """获取父节点"""
        if node.parent() is None:
            return self.root_node
        return node.parent()

    def get_all_path(self) -> typing.List[PathData]:
        """获取所有被选中的节点的路径"""
        path_list = []
        iterator = QTreeWidgetItemIterator(self)
        while iterator.value():
            item = iterator.value()
            if item.checkState(0) == Qt.CheckState.Checked:
                # path_list.append((item.text(1), item.text(2), item.text(3)))
                path_list.append(PathData(item.text(0), item.text(1).replace(
                    '\\', '/'), item.text(2).replace('\\', '/'), item.text(3)))
            iterator += 1
        return path_list

    def set_root_path(self, path: Path):
        """设置根目录"""
        self.root_path = path
        self.root_node = self.invisibleRootItem()
        # 清除原本的内容
        self.clear()

        threading.Thread(self.__load_directory(Path(path), self.root_node)).start()

    def get_nuitka_cmd(self) -> list[str]:
        selected_path_list = self.get_all_path()
        cmd_list = []
        last_dir = ''
        for each in selected_path_list:
            if each.type == '文件夹':
                if each.relative_path.startswith(last_dir) and last_dir != '':
                    continue
                last_dir = each.relative_path
                # 如果文件夹被选中就不再添加其中的文件
                cmd_list.append(
                    f'--include-data-dir={each.absolute_path}={each.relative_path}')
            elif each.type == '文件':
                if each.relative_path.startswith(last_dir) and last_dir != '':
                    continue
                cmd_list.append(
                    f'--include-data-files={each.absolute_path}={each.relative_path}')
        return cmd_list


if __name__ == '__main__':
    app = QApplication([])
    file_tree = FileTree()
    file_tree.set_root_path(Path('tests'))
    file_tree.show()
    app.exec()
