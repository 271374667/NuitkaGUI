from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QTimer, Signal


class MySplashScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 400)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowOpacity(0.95)
        # 设置为模态窗口
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.label = QLabel(self)
        self.movie = QMovie('resource/images/splash.gif')
        self.label.setMovie(self.movie)
        self.movie.start()

        self.statusLabel = QLabel(self)
        self.statusLabel.setText('正在加载,请等待……')
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statusLabel.setStyleSheet('color: white; font-size: 20px;')
        self.statusLabel.adjustSize()
        # 将控件放在窗体的正中间偏下
        self.statusLabel.move(
            (self.width() - self.statusLabel.width()) / 2 + 30, self.height() * 0.9)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.label)
        self.setLayout(self.mainLayout)


    def setLoadingText(self, str: str):
        self.statusLabel.setText(str)
        self.statusLabel.adjustSize()
        self.statusLabel.move(
            (self.width() - self.statusLabel.width()) / 2 , self.height() * 0.9)



if __name__ == "__main__":
    app = QApplication([])
    splash = MySplashScreen()
    splash.show()
    QTimer.singleShot(1000, lambda: splash.setLoadingText('当前正在加载资源文件'))
    QTimer.singleShot(3000, lambda: splash.setLoadingText('正在检查模块更新'))
    # 设置只触发一次
    app.exec()
