from pathlib import Path
from typing import Optional

from PySide6.QtCore import Signal
from PySide6.QtGui import QDragEnterEvent, QColor
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import ToolTipFilter, InfoBadge, SwitchButton, PillPushButton, PrimaryPushButton, BodyLabel, \
    CaptionLabel

from src.component.drop_mask import DropMask
from src.interface.Ui_basic_page_fluent import Ui_basic_page
from src.view.message_base_view import MessageBaseView


class BasicView(MessageBaseView):
    py_file_selected = Signal(str)

    def __init__(self):
        super().__init__()
        # 一些内置的状态
        self.setObjectName('BasicView')
        self.setAcceptDrops(True)

        self.ui = Ui_basic_page()
        self.ui.setupUi(self)

        self.dialog_mask = DropMask(self, '文件拖入')
        self.dialog_mask.hide()

        self._output_dir_unselected = InfoBadge.custom('自动选择', QColor('#6750a4'), QColor('#6750a4'), parent=self,
                                                       target=self.ui.CardWidget_3)
        self._icon_unselected = InfoBadge.custom('自动选择', QColor('#6750a4'), QColor('#6750a4'), parent=self,
                                                 target=self.ui.CardWidget_4)

        self._output_dir_selected = InfoBadge.warning('已选择', parent=self, target=self.ui.CardWidget_3)
        self._output_dir_selected.hide()
        self._icon_selected = InfoBadge.warning('已选择', parent=self, target=self.ui.CardWidget_4)
        self._icon_selected.hide()

        self._source_script_lb_origin_text: str = self.get_source_script_lb().text()
        self._output_btn_tooltip_origin_text: str = self.get_output_path_btn().toolTip()
        self._icon_btn_tooltip_origin_text: str = self.get_icon_btn().toolTip()

        self.initialize()

    @property
    def source_script_path(self) -> Optional[Path]:
        source_script_text: str = self.ui.LBPyFilePath.text()
        # 判断一个字符串是否是一个有效的路径
        if not Path(source_script_text).exists():
            return None
        return Path(source_script_text)

    @source_script_path.setter
    def source_script_path(self, source_script: Optional[Path]) -> None:
        if source_script is None or not Path(source_script).exists():
            self.ui.LBPyFilePath.setText(self._source_script_lb_origin_text)
            self.ui.IWSelectedFile.setIcon(":/Icons/materialIcons/no_file.svg")
            return
        self.ui.IWSelectedFile.setIcon(":/Icons/materialIcons/has_file.svg")
        self.ui.LBPyFilePath.setText(str(source_script))

    @property
    def output_dir(self) -> Optional[Path]:
        output_dir_text: str = self.get_output_path_btn().toolTip()
        if not Path(output_dir_text).exists():
            return None
        return Path(output_dir_text)

    @output_dir.setter
    def output_dir(self, output_dir: Optional[Path]) -> None:
        if output_dir is None or not output_dir.exists():
            if self.source_script_path:
                self.get_output_path_btn().setToolTip(str(output_dir))
            else:
                self.get_output_path_btn().setToolTip(self._output_btn_tooltip_origin_text)

            self._output_dir_selected.hide()
            self._output_dir_unselected.show()
            return
        self.get_output_path_btn().setToolTip(str(output_dir))
        self._output_dir_selected.show()
        self._output_dir_unselected.hide()

    @property
    def icon_path(self) -> Optional[Path]:
        icon_path_text: str = self.get_icon_btn().toolTip()
        if not Path(icon_path_text).exists():
            return None
        return Path(icon_path_text)

    @icon_path.setter
    def icon_path(self, icon_path: Optional[Path]) -> None:
        if icon_path is None or not icon_path.exists():
            self.get_icon_btn().setToolTip(self._icon_btn_tooltip_origin_text)
            self._icon_selected.hide()
            self._icon_unselected.show()
            return
        self.get_icon_btn().setToolTip(str(icon_path))
        self._icon_selected.show()
        self._icon_unselected.hide()

    def get_source_script_btn(self) -> PrimaryPushButton:
        """获取选择 Python 文件的按钮"""
        return self.ui.BTNGetPy

    def get_source_script_lb(self) -> CaptionLabel:
        return self.ui.LBPyFilePath

    def get_output_path_btn(self) -> PillPushButton:
        """获取输出路径的按钮"""
        return self.ui.BTNOutputPath

    def get_output_path_lb(self) -> BodyLabel:
        return self.ui.LBOutputPath

    def get_icon_btn(self) -> PillPushButton:
        """获取图标"""
        return self.ui.BTNIcon

    def get_mode_radiobutton(self) -> SwitchButton:
        """获取模式"""
        return self.ui.SwitchButton

    def get_start(self) -> PrimaryPushButton:
        """获取开始按钮"""
        return self.ui.BTNStart

    def get_mask(self) -> DropMask:
        """获取遮罩"""
        return self.dialog_mask

    def resize_mask(self) -> None:
        self.get_mask().resize(self.width(), self.height())

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
    widget = BasicView()
    widget.source_script_path = Path('C:/Users')
    widget.output_dir = Path('C:/Users')
    widget.show()
    app.exec()
