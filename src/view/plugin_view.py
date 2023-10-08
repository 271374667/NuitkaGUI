from typing import Callable

from PySide6.QtWidgets import QApplication, QWidget

from src.interface.Ui_component_list_item import Ui_Form


class PluginItem(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def set_title(self, title: str) -> None:
        """设置插件的标题"""
        self.ui.LBTitle.setText(title)
        self.setObjectName(title)

    def set_info(self, info: str) -> None:
        """设置插件的简介"""
        self.ui.LBinfo.setText(info)

    def set_switch_status(self, status: bool) -> None:
        """设置插件的开关状态"""
        self.ui.SwitchButton.setChecked(status)

    def get_switch_status(self) -> bool:
        """获取插件的开关状态"""
        return self.ui.SwitchButton.isChecked()

    def switch_clicked(self, func: Callable[[str, bool], None]) -> None:
        """插件的开关被点击"""
        # 因为默认只有一个参数bool，所以需要使用 lambda 表达式来传递一个额外参数参数
        self.ui.SwitchButton.checkedChanged.connect(lambda x: func(self.objectName(), x))


if __name__ == '__main__':
    app = QApplication([])
    window = PluginItem()
    window.set_title('--standalone')
    window.switch_clicked(lambda x, y: print(x, y))
    window.show()
    app.exec()
