from PySide6.QtWidgets import QLineEdit

class DragableQLineEdit(QLineEdit):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, e):
        if e.mimeData().hasText():  
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().urls()[0].toLocalFile()
        self.setText(path)

