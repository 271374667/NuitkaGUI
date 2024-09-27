from PySide6.QtCore import Signal, QObject
from src.utils.singleton import singleton


@singleton
class SignalBus(QObject):
    update_setting_view = Signal()
