from typing import Callable

from PySide6.QtWidgets import QApplication, QWidget

from src.interface.Ui_basic_page import Ui_basic_page


class BasicView(QWidget):
    def __init__(self):
        super().__init__()
        # 一些内置的状态
        self._file_icon_status = False
        self._input_python_file = ''
        self._pythonexe_text = ''
        self._output_dir = ''

        self.ui = Ui_basic_page()
        self.ui.setupUi(self)

    def get_file_icon_status(self) -> bool:
        """获取文件选择图标的状态，一个是选中，一个是未选中"""
        return self._file_icon_status

    def set_file_icon_status(self, status: bool) -> None:
        """根据布尔值设置文件选择图标的状态，一个是选中，一个是未选中"""
        if status:
            self.ui.IWSelectedFile.setIcon(":/Icons/materialIcons/has_file.svg")
        else:
            self.ui.IWSelectedFile.setIcon(":/Icons/materialIcons/no_file.svg")
        self._file_icon_status = status

    def btn_python_clicked(self, func: Callable) -> None:
        """选择需要打包的 .py 文件"""
        self.ui.BTNGetPy.clicked.connect(func)

    def get_input_python_file(self) -> str:
        """获取需要打包的 Python 文件"""
        return self._input_python_file

    def set_input_python_file_text(self, text: str) -> None:
        """设置需要打包的 Python 文件的文本提示"""
        if not text.strip():
            self.ui.LBPyFilePath.setText('在这里选择需要被打包的 .py 文件')
            return
        self.ui.LBPyFilePath.setText(text)
        self._input_python_file = text

    def btn_pythonexe_clicked(self, func: Callable) -> None:
        """选择 Python.exe 文件"""
        self.ui.BTNPythonExePath.clicked.connect(func)

    def get_pythonexe_text(self) -> str:
        """获取 Python.exe 文件"""
        return self._pythonexe_text

    def set_pythonexe_text(self, text: str) -> None:
        """设置 Python.exe 文件"""
        if not text.strip():
            default_text = """软件的运转需要使用python.exe
                            请确保您电脑里面至少有一个可以使用的Python环境
                            """
            self.ui.LBPythonExePath.setText(default_text)
            return
        self.ui.LBPythonExePath.setText(text)
        self._pythonexe_text = text

    def btn_output_dir_clicked(self, func: Callable) -> None:
        """选择输出文件"""
        self.ui.BTNOutputPath.clicked.connect(func)

    def get_output_dir(self) -> str:
        """获取输出文件"""
        return self._output_dir

    def set_output_dir_text(self, text: str) -> None:
        """设置输出文件"""
        if not text.strip():
            self.ui.LBOutputPath.setText('您的程序被打包之后存放的位置')
            return
        self.ui.LBOutputPath.setText(text)
        self._output_dir = text

    def btn_mode_clicked(self, func: Callable[[bool], None]) -> None:
        """切换打包模式"""
        self.ui.SwitchButton.checkedChanged.connect(lambda x: func(x))

    def get_mode(self) -> bool:
        """获取打包模式, True 为单文件, False 为文件夹"""
        return self.ui.SwitchButton.isChecked()

    def set_mode(self, mode: bool) -> None:
        """设置打包模式, True 为单文件, False 为文件夹"""
        self.ui.SwitchButton.setChecked(mode)

    def btn_start_clicked(self, func: Callable) -> None:
        """开始打包"""
        self.ui.BTNStart.clicked.connect(func)


if __name__ == '__main__':
    app = QApplication([])
    window = BasicView()
    # window.set_mode(True)
    # window.set_file_icon_status(True)
    window.show()
    app.exec()
