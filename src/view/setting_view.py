from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget
from qfluentwidgets import (
    BodyLabel,
    FluentIcon,
    Icon,
    PushSettingCard,
    SettingCardGroup,
    ToolTipFilter,
)
from qfluentwidgets.components import (
    ExpandLayout,
    LargeTitleLabel,
    SmoothScrollArea,
)

from src.resource import rc_res
from src.config import cfg
from src.core.version import __version__
from src.view.message_base_view import MessageBaseView

rc_res = rc_res


class SettingView(MessageBaseView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("setting_view")
        self.main_layout = QVBoxLayout()
        self.smooth_scroll_area = SmoothScrollArea()

        self.is_state_tooltip_running: bool = False

        self.scroll_widget = QWidget()
        self.expand_layout = ExpandLayout(self.scroll_widget)

        self.setting_title = LargeTitleLabel()
        self.setting_title.setText("设置")

        self.version_lb: BodyLabel = BodyLabel()
        self.version_lb.setText(f"当前软件版本: {__version__}")
        self.version_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._create_card_group()
        self._create_card()
        self._set_up_tooltip()
        self._set_up_layout()
        self._initialize()

    def _create_card_group(self):
        self.general_group = SettingCardGroup("通用", self.scroll_widget)

    def _create_card(self):
        # 全局设置
        self.project_python_exe_path_card = PushSettingCard(
            "项目Python.exe路径",
            Icon(FluentIcon.CHEVRON_RIGHT),
            "设置项目Python.exe的路径",
            "选择当前项目使用的Python.exe路径",
            self.general_group,
        )

        self.global_python_exe_path_card = PushSettingCard(
            "全局Python.exe路径",
            Icon(FluentIcon.CHEVRON_RIGHT),
            "设置全局Python.exe的路径",
            "选择全局Python.exe路径",
            self.general_group,
        )

    def _set_up_tooltip(self):
        self.project_python_exe_path_card.setToolTip("选择当前项目使用的Python.exe路径")
        self.global_python_exe_path_card.setToolTip("选择全局Python.exe路径")

    def _set_up_layout(self):
        """设置布局"""
        self.smooth_scroll_area.setWidget(self.scroll_widget)

        self.expand_layout.addWidget(self.general_group)
        self.scroll_widget.setLayout(self.expand_layout)
        self.expand_layout.setSpacing(28)
        self.expand_layout.setContentsMargins(60, 10, 60, 0)

        # 给卡片组添加卡片
        self.general_group.addSettingCards(
            [self.project_python_exe_path_card, self.global_python_exe_path_card]
        )

    def _initialize(self) -> None:
        """初始化窗体"""
        self.setWindowTitle("设置")
        self.setObjectName("setting_view")
        self.resize(1100, 800)
        self.smooth_scroll_area.setWidgetResizable(True)
        self.smooth_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.setting_title.setMargin(30)
        self.setting_title.setFixedWidth(200)

        self.main_layout.addWidget(self.setting_title)
        self.main_layout.addWidget(self.smooth_scroll_area)
        self.main_layout.addWidget(self.version_lb)
        self.setLayout(self.main_layout)

        # 这里因为背景色不一样,我手动打个补丁
        self.setStyleSheet("background-color: #f9f9f9")
        self.smooth_scroll_area.setStyleSheet("background-color: #f9f9f9")

        for each in self.findChildren(QWidget):
            each.installEventFilter(ToolTipFilter(each, 200))


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication()
    s = SettingView()
    s.show()
    app.exec()
