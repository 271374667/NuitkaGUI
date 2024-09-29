from PySide6.QtCore import Signal, QObject

from src.utils.singleton import singleton


@singleton
class SignalBus(QObject):
    # 由基础页面设置可用的python.exe后触发,修改设置页面的tooltips等一些信息
    update_setting_view = Signal()
