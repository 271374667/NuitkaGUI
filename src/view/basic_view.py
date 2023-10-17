from PySide6.QtCore import Signal
from PySide6.QtGui import QDragEnterEvent
from PySide6.QtWidgets import (QApplication, QWidget)
from qmaterialwidgets import FluentIcon as FIF
from qmaterialwidgets.components import (FilledPushButton, InfoBadge, InfoBar, InfoBarPosition, OutlinedPushButton,
                                         SwitchButton, ToolTipFilter)

from src.component.dropMask import MaskDialogBase
from src.interface.Ui_basic_page import Ui_basic_page


class BasicView(QWidget):
    py_file_selected = Signal(str)

    def __init__(self):
        super().__init__()
        # 一些内置的状态
        self._file_icon_status = False
        self._input_python_file = ''
        self._output_dir = ''

        self.setObjectName('BasicView')
        self.setAcceptDrops(True)

        self.ui = Ui_basic_page()
        self.ui.setupUi(self)

        self.dialog_mask = MaskDialogBase(self, '文件拖入', FIF.ZIP_FOLDER)
        self.dialog_mask.hide()

        self._output_dir_unselected = InfoBadge.info('自动选择', parent=self, target=self.ui.CardWidget_3)
        self._icon_unselected = InfoBadge.info('自动选择', parent=self, target=self.ui.CardWidget_4)

        self._output_dir_selected = InfoBadge.attension('已选择', parent=self, target=self.ui.CardWidget_3)
        self._output_dir_selected.hide()
        self._icon_selected = InfoBadge.attension('已选择', parent=self, target=self.ui.CardWidget_4)
        self._icon_selected.hide()

        self.initialize()

    def get_select_python_file(self) -> FilledPushButton:
        """获取选择 Python 文件的按钮"""
        return self.ui.BTNGetPy

    def get_output_path(self) -> OutlinedPushButton:
        """获取输出路径的按钮"""
        return self.ui.BTNOutputPath

    def get_icon(self) -> OutlinedPushButton:
        """获取图标"""
        return self.ui.BTNIcon

    def get_mode_radiobutton(self) -> SwitchButton:
        """获取模式"""
        return self.ui.SwitchButton

    def get_file_icon_status(self) -> bool:
        """获取文件选择图标的状态，一个是选中，一个是未选中"""
        return self._file_icon_status

    def get_start(self) -> FilledPushButton:
        """获取开始按钮"""
        return self.ui.BTNStart

    def get_mask(self) -> MaskDialogBase:
        """获取遮罩"""
        return self.dialog_mask

    def set_py_file_status(self, status: bool) -> None:
        """根据布尔值设置文件选择图标的状态，一个是选中，一个是未选中"""
        if status:
            self.ui.IWSelectedFile.setIcon(":/Icons/materialIcons/has_file.svg")
        else:
            self.ui.IWSelectedFile.setIcon(":/Icons/materialIcons/no_file.svg")
        self._file_icon_status = status

    def set_output_status(self, status: bool) -> None:
        """根据布尔值设置输出路径的状态，一个是选中，一个是未选中"""
        if status:
            self._output_dir_selected.show()
            self._output_dir_unselected.hide()
            return
        self._output_dir_selected.hide()
        self._output_dir_unselected.show()

    def set_icon_status(self, status: bool) -> None:
        """根据布尔值设置图标的状态，一个是选中，一个是未选中"""
        if status:
            self._icon_selected.show()
            self._icon_unselected.hide()
            return
        self._icon_selected.hide()
        self._icon_unselected.show()

    def set_input_python_file_text(self, text: str) -> None:
        """设置需要打包的 Python 文件的文本提示"""
        if not text.strip():
            self.ui.LBPyFilePath.setText('在这里选择需要被打包的 .py 文件')
            return
        self.ui.LBPyFilePath.setText(text)
        self._input_python_file = text

    def set_output_dir_text(self, text: str) -> None:
        """设置输出文件"""
        if not text.strip():
            self.ui.LBOutputPath.setText('您的程序被打包之后存放的位置')
            return
        self.ui.LBOutputPath.setText(text)
        self._output_dir = text

    def resize_mask(self) -> None:
        self.get_mask().resize(self.width(), self.height())

    def show_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.info(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def show_warning_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.warning(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def show_success_info(self, title: str, content: str, duration: int = 15000) -> None:
        InfoBar.success(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def show_error_info(self, title: str, content: str, duration: int = -1) -> None:
        InfoBar.error(title, content, parent=self, duration=duration, position=InfoBarPosition.TOP)

    def dragEnterEvent(self, e: QDragEnterEvent):
        if e.mimeData().hasText():
            self.dialog_mask.show()

    # 窗体大小发生改变触发事件
    def resizeEvent(self, event):
        self.resize_mask()

    def initialize(self) -> None:
        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == '__main__':
    app = QApplication([])
    window = BasicView()
    # window.set_mode(True)
    # window.set_py_file_status(True)
    window.show()
    app.exec()
