from PySide6.QtWidgets import QFileDialog

from src.model.setting_model import SettingModel
from src.view.setting_view import SettingView


class SettingPresenter:
    def __init__(self):
        self._view = SettingView()
        self._model = SettingModel()

        self.bind()
        self.update_view()

    @property
    def view(self) -> SettingView:
        return self._view

    @property
    def model(self) -> SettingModel:
        return self._model

    def _exit(self):
        if self.view.show_mask_dialog("重启应用", "设置已经生效，重启应用后生效"):
            self.model.exit()

    def _project_python_exe_card_clicked(self):
        """让用户选择Python.exe路径"""
        file_path, _ = QFileDialog.getOpenFileName(self.view, "选择Python.exe", "", "Python.exe (*.exe)")
        if file_path:
            self.model.project_python_exe_path = file_path
            self.view.project_python_exe_path_card.setToolTip(file_path)

    def _global_python_exe_card_clicked(self):
        """让用户选择Python.exe路径"""
        file_path, _ = QFileDialog.getOpenFileName(self.view, "选择Python.exe", "", "Python.exe (*.exe)")
        if file_path:
            self.model.global_python_exe_path = file_path
            self.view.global_python_exe_path_card.setToolTip(file_path)

    def update_view(self):
        self.view.global_python_exe_path_card.setToolTip(str(self.model.global_python_exe_path))
        self.view.project_python_exe_path_card.setToolTip(str(self.model.project_python_exe_path))

    def bind(self):
        self.view.optimization_card.comboBox.currentIndexChanged.connect(self._exit)
        self.view.project_python_exe_path_card.clicked.connect(self._project_python_exe_card_clicked)
        self.view.global_python_exe_path_card.clicked.connect(self._global_python_exe_card_clicked)
