import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

import loguru

from src.common.nuitka_command.command_implement.command_path import (
    CommandWindowsIconFromIco,
    CommandOutputDir,
)
from src.common.nuitka_command.command_manager import CommandManager
from src.config import cfg
from src.core.paths import NUITKA_CRASH_REPORT_FILE
from src.signal_bus import SignalBus


class BasicModel:
    def __init__(self):
        self._signal_bus = SignalBus()
        self._command_manager = CommandManager()
        self._output_command = self._command_manager.get_command_by_type(
            CommandOutputDir
        )
        self._windows_icon_command = self._command_manager.get_command_by_type(
            CommandWindowsIconFromIco
        )

    @property
    def source_script_path(self) -> Optional[Path]:
        return self._command_manager.source_script

    @source_script_path.setter
    def source_script_path(self, source_script: Optional[Path]) -> None:
        self._command_manager.source_script = source_script

    @property
    def project_python_exe_path(self) -> Path:
        return Path(cfg.get(cfg.project_python_exe_path))

    @project_python_exe_path.setter
    def project_python_exe_path(self, project_python_exe_path: Optional[Path]) -> None:
        if project_python_exe_path:
            cfg.set(cfg.project_python_exe_path, str(project_python_exe_path))
        else:
            cfg.set(cfg.project_python_exe_path, "")

    @property
    def output_dir(self) -> Optional[Path]:
        return Path(self._output_command.value)

    @output_dir.setter
    def output_dir(self, output_dir: Optional[Path]) -> None:
        self._output_command.value = output_dir
        print(self._output_command.value)

    @property
    def icon_path(self) -> Optional[Path]:
        return Path(self._windows_icon_command.value)

    @icon_path.setter
    def icon_path(self, icon_path: Optional[Path]) -> None:
        self._windows_icon_command.value = icon_path

    @property
    def packaged_mode(self) -> str:
        standalone_command = self._command_manager.get_command_by_command("standalone")
        if standalone_command.value:
            return "standalone"
        return "onefile"

    @packaged_mode.setter
    def packaged_mode(self, mode: str) -> None:
        standalone_command = self._command_manager.get_command_by_command("standalone")
        onefile_command = self._command_manager.get_command_by_command("onefile")
        if mode == "standalone":
            standalone_command.value = True
            onefile_command.value = False
        else:
            standalone_command.value = False
            onefile_command.value = True

    def start(self) -> bool:
        def getexceptions(context: str) -> str:
            # 如果是Nuitka的崩溃报告文件，则解析出其中的异常信息
            try:
                root = ET.fromstring(context)
                exceptions = root.findall('.//exception')
                return '\n'.join([exception.text for exception in exceptions if exception.text])
            except ET.ParseError as e:
                return f"Error parsing XML: {e}"

        try:
            command = self._command_manager.current_command.replace('"', "").split(" ")
            # command = self._command_manager.current_command
            loguru.logger.info(f"开始打包: {command}")
            result = subprocess.run(
                command, creationflags=subprocess.CREATE_NEW_CONSOLE, encoding="utf-8"
            )
            # result = subprocess.check_output(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
            loguru.logger.info(f"打包结束: {result}")
            if result.returncode != 0:
                raise Exception("打包失败")
            return True
        except Exception as e:
            loguru.logger.error(e)
            if NUITKA_CRASH_REPORT_FILE.exists():
                with open(NUITKA_CRASH_REPORT_FILE, 'r', encoding='utf-8') as f:
                    context = f.read()
                exceptions = getexceptions(context)
                self._signal_bus.append_output.emit(f"打包失败: {e}\n{exceptions}")
                NUITKA_CRASH_REPORT_FILE.rename(NUITKA_CRASH_REPORT_FILE.with_suffix('.bak'))
                return False
            self._signal_bus.append_output.emit(f"打包失败: {e}")
            return False
