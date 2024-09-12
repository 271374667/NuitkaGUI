from src.common.nuitka_command.command import CommandTextBase


class CommandOutputDir(CommandTextBase):
    command: str = 'output-dir'


class CommandMain(CommandTextBase):
    command: str = 'main'


class CommandNofollowImportTo(CommandTextBase):
    command: str = 'nofollow-import-to'


class CommandIncludePackage(CommandTextBase):
    command: str = 'include-package'


class CommandIncludeDataDir(CommandTextBase):
    command: str = 'include-data-dir'


class CommandWindowsIconFromIco(CommandTextBase):
    command: str = 'windows-icon-from-ico'


class CommandWindowsCompanyName(CommandTextBase):
    command: str = 'windows-company-name'


class CommandWindowsFileVersion(CommandTextBase):
    command: str = 'windows-file-version'


class CommandWindowsProductVersion(CommandTextBase):
    command: str = 'windows-product-version'


class CommandWindowsFileDescription(CommandTextBase):
    command: str = 'windows-file-description'


class CommandOnefileTempdirSpec(CommandTextBase):
    command: str = 'onefile-tempdir-spec'
