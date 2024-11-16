from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

ASSETS_DIR = PROJECT_DIR / "assets"
OUTPUT_DIR = PROJECT_DIR / "output"
SCRPITS_DIR = PROJECT_DIR / "scripts"
UI_DIR = PROJECT_DIR / "ui"
SRC_DIR = PROJECT_DIR / "src"
DEPENDENCE_DIR = PROJECT_DIR / "dependence"
DOWNLOADS_DIR = DEPENDENCE_DIR / "downloads"
GCC_DIR = (
    DOWNLOADS_DIR / "gcc" / "x86_64" / "13.2.0-16.0.6-11.0.1-msvcrt-r1" / "mingw64"
)
RESOURCE_DIR = SRC_DIR / "resource"
INTERFACE_DIR = SRC_DIR / "interface"
COMMAND_IMPLEMENT_DIR = SRC_DIR / "common" / "nuitka_command" / "command_implement"

LOG_FILE = PROJECT_DIR / "log.log"
CONFIG_FILE = PROJECT_DIR / "config.json"
QRC_FILE = ASSETS_DIR / "res.qrc"
QRC_PY_FILE = RESOURCE_DIR / "rc_res.py"
LOGO_FILE = DEPENDENCE_DIR / "logo.ico"
CCACHE_DEPENDENCE_FILE = DOWNLOADS_DIR / "depends" / "x86_64" / "ccache.exe"
DEPENDS_EXE_DEPENDENCE_FILE = DOWNLOADS_DIR / "depends" / "x86_64" / "depends.exe"
DEPENDS_DLL_DEPENDENCE_FILE = DOWNLOADS_DIR / "depends" / "x86_64" / "depends.dll"
UPX_DEPENDENCE_FILE = DOWNLOADS_DIR / "depends" / "x86_64" / "upx.exe"
GCC_EXE_FILE = GCC_DIR / "bin" / "gcc.exe"
CLANG_EXE_FILE = GCC_DIR / "bin" / "clang.exe"
DEPENDENCE_SAVE_PATH_FILE = PROJECT_DIR / "dependence_save_path.json"
NUITKA_CRASH_REPORT_FILE = PROJECT_DIR / "nuitka-crash-report.xml"
