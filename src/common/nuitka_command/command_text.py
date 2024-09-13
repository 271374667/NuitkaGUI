from src.common.nuitka_command.command import CommandValueBase


class CommandOutputDir(CommandValueBase):
    command: str = 'output-dir'


class CommandMain(CommandValueBase):
    command: str = 'main'


class CommandWindowsIconFromIco(CommandValueBase):
    command: str = 'windows-icon-from-ico'


class CommandWindowsCompanyName(CommandValueBase):
    command: str = 'windows-company-name'


class CommandWindowsFileVersion(CommandValueBase):
    command: str = 'windows-file-version'


class CommandWindowsProductVersion(CommandValueBase):
    command: str = 'windows-product-version'


class CommandWindowsFileDescription(CommandValueBase):
    command: str = 'windows-file-description'


class CommandOnefileTempdirSpec(CommandValueBase):
    command: str = 'onefile-tempdir-spec'
