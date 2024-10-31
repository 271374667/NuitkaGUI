from PySide6.QtCore import Signal, QObject

from src.utils.singleton import singleton


@singleton
class SignalBus(QObject):
    # 由基础页面设置可用的python.exe后触发,修改设置页面的tooltips等一些信息
    update_setting_view = Signal()
    # 将内容输出到输出面板
    append_output = Signal(str)
    # 更新插件页面(解析页面触发插件页面的更新)
    update_plugin_view = Signal()
