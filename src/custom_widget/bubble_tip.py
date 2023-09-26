import sys

from PySide6.QtCore import (QEasingCurve, QParallelAnimationGroup, QPoint, QPropertyAnimation, QRectF, Qt)
from PySide6.QtGui import QColor, QGuiApplication, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget)


class BubbleLabel(QWidget):
    BackgroundColor = QColor(195, 195, 195)
    BorderColor = QColor(150, 150, 150)
    opacity = 0.95

    def __init__(self):
        super().__init__()
        # 设置无边框置顶
        self.setWindowFlags(
                Qt.Window | Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)
        # 设置最小宽度和高度
        self.setMinimumWidth(200)
        self.setMinimumHeight(48)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label = QLabel(self)

        layout = QVBoxLayout(self)
        # 左上右下的边距（下方16是因为包括了三角形）
        layout.setContentsMargins(8, 8, 8, 16)
        layout.addWidget(self.label)
        # 获取屏幕高宽
        self._desktop = QGuiApplication.primaryScreen()

    def setText(self, text):
        text = text.strip()
        self.label.setText(text)

    def text(self):
        return self.label.text()

    def stop(self):
        self.hide()
        self.animationGroup.stop()
        self.close()

    def show(self):
        super().show()
        # 窗口开始位置
        startPos = QPoint(
                self._desktop.availableGeometry().width() - self.width() - 100,
                self._desktop.availableGeometry().height() - self.height())
        endPos = QPoint(
                self._desktop.availableGeometry().width() - self.width() - 100,
                self._desktop.availableGeometry().height() - self.height() * 3 - 5)
        # 初始化动画
        self.initAnimation(startPos, endPos)

    def showMessage(self, text: str):
        self.setText(text)
        self.show()
        self.animationGroup.finished.connect(self.stop)

    def initAnimation(self, startPos, endPos):
        # 透明度动画
        opacityAnimation = QPropertyAnimation(self, b"opacity")
        opacityAnimation.setStartValue(1.0)
        opacityAnimation.setEndValue(0.0)
        # 设置动画曲线
        opacityAnimation.setEasingCurve(QEasingCurve.InQuad)
        opacityAnimation.setDuration(4000)  # 在4秒的时间内完成
        # 往上移动动画
        moveAnimation = QPropertyAnimation(self, b"pos")
        moveAnimation.setStartValue(startPos)
        moveAnimation.setEndValue(endPos)
        moveAnimation.setEasingCurve(QEasingCurve.InQuad)
        moveAnimation.setDuration(5000)  # 在5秒的时间内完成
        # 并行动画组（目的是让上面的两个动画同时进行）
        self.animationGroup = QParallelAnimationGroup(self)
        self.animationGroup.addAnimation(opacityAnimation)
        self.animationGroup.addAnimation(moveAnimation)
        self.animationGroup.finished.connect(self.close)  # 动画结束时关闭窗口
        self.animationGroup.start()

    def paintEvent(self, event):
        super(BubbleLabel, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

        rectPath = QPainterPath()  # 圆角矩形
        triPath = QPainterPath()  # 底部三角形

        height = self.height() - 8  # 往上偏移8
        rectPath.addRoundedRect(QRectF(0, 0, self.width(), height), 5, 5)
        x = self.width() / 5 * 4
        triPath.moveTo(x, height)  # 移动到底部横线4/5处
        # 画三角形
        triPath.lineTo(x + 6, height + 8)
        triPath.lineTo(x + 12, height)

        rectPath.addPath(triPath)  # 添加三角形到之前的矩形上

        # 边框画笔
        painter.setPen(QPen(self.BorderColor, 1, Qt.SolidLine,
                            Qt.RoundCap, Qt.RoundJoin))
        # 背景画刷
        painter.setBrush(self.BackgroundColor)
        # 绘制形状
        painter.drawPath(rectPath)
        # 三角形底边绘制一条线保证颜色与背景一样
        painter.setPen(QPen(self.BackgroundColor, 1,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(round(x), height, round(x + 12), height)

    def windowOpacity(self):
        return super().windowOpacity()

    def setWindowOpacity(self, opacity):
        super().setWindowOpacity(opacity)

    # 由于opacity属性不在QWidget中需要重新定义一个


class Window4Test(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window4Test, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.msgEdit = QLineEdit(self, returnPressed=self.onMsgShow)
        self.msgButton = QPushButton("显示内容", self, clicked=self.onMsgShow)
        layout.addWidget(self.msgEdit)
        layout.addWidget(self.msgButton)

    def onMsgShow(self):
        msg = self.msgEdit.text().strip()
        if not msg:
            return
        if hasattr(self, "_blabel"):
            self._blabel.stop()
            self._blabel.deleteLater()
            del self._blabel
        self._blabel = BubbleLabel()
        self._blabel.showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bubble = BubbleLabel()
    bubble.showMessage("hello world")
    sys.exit(app.exec())
