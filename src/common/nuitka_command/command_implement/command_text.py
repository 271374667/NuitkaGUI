from src.common.nuitka_command.command import CommandTextBase


class CommandWindowsCompanyName(CommandTextBase):
    name: str = "公司名称"
    description: str = "设置Windows应用的公司名称"
    command: str = "windows-company-name"


class CommandWindowsFileVersion(CommandTextBase):
    name: str = "文件版本"
    description: str = "设置Windows应用的文件版本"
    command: str = "windows-file-version"


class CommandWindowsProductVersion(CommandTextBase):
    name: str = "产品版本"
    description: str = "设置Windows应用的产品版本"
    command: str = "windows-product-version"


class CommandWindowsFileDescription(CommandTextBase):
    name: str = "文件描述"
    description: str = "设置Windows应用的文件描述"
    command: str = "windows-file-description"


class CommandOnefileTempdirSpec(CommandTextBase):
    name: str = "单文件临时目录位置"
    description: str = "设置单文件临时目录位置"
    command: str = "onefile-tempdir-spec"
    visible: bool = False


class CommandIncludePackageData(CommandTextBase):
    name: str = "include-package-data"
    description: str = "在这里输入需要打包的模块的名称: 比如: PySide6, pyautogui,模块之间用逗号分隔"
    command: str = "include-package-data"
