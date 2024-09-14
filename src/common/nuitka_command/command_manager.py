from pathlib import Path
from typing import Optional

from src.common.nuitka_command import command_flag, command_multiple_times, command_text, command_path
from src.common.nuitka_command.command_plugin import CommandPlugin
from src.utils.singleton import singleton


@singleton
class CommandManager:
    def __init__(self):
        # Flags
        self.onefile = command_flag.CommandOneFile()
        self.standalone = command_flag.CommandStandAlone()
        self.show_progress = command_flag.CommandShowProgress()
        self.show_memory = command_flag.CommandShowMemory()
        self.remove_output = command_flag.CommandRemoveOutput()
        self.low_memory = command_flag.CommandLowMemory()
        self.mingw64 = command_flag.CommandMingw64()
        self.clang = command_flag.CommandClang()
        self.quiet = command_flag.CommandQuiet()
        self.lto_no = command_flag.CommandLtoNo()
        self.disable_ccache = command_flag.CommandDisableCcache()
        self.clean_cache = command_flag.CommandCleanCache()
        self.assume_yes_for_downloads = command_flag.CommandAssumeYesForDownloads()
        self.windows_uac_admin = command_flag.CommandWindowsUacAdmin()
        self.windows_uac_access = command_flag.CommandWindowsUacAccess()
        self.warn_implicit_exceptions = command_flag.CommandWarnImplicitExceptions()

        # Text
        self.windows_company_name = command_text.CommandWindowsCompanyName()
        self.windows_file_version = command_text.CommandWindowsFileVersion()
        self.windows_product_version = command_text.CommandWindowsProductVersion()
        self.windows_file_description = command_text.CommandWindowsFileDescription()
        self.onefile_tempdir_spec = command_text.CommandOnefileTempdirSpec()

        # Path
        self.main = command_path.CommandMain()
        self.output_dir = command_path.CommandOutputDir()
        self.windows_icon_from_ico = command_path.CommandWindowsIconFromIco()

        # multiple times
        self.include_data_files = command_multiple_times.CommandIncludeDataFiles()
        self.include_data_dir = command_multiple_times.CommandIncludeDataDir()

        # Plugins
        self.command_plugin = CommandPlugin()

    @property
    def source_script(self) -> Optional[Path]:
        return self.main.value

    @source_script.setter
    def source_script(self, source_script: Optional[Path]) -> None:
        self.main.value = source_script
