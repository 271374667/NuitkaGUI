from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

ASSETS_DIR = PROJECT_DIR / 'assets'
OUTPUT_DIR = PROJECT_DIR / 'output'
SCRPITS_DIR = PROJECT_DIR / 'scripts'
UI_DIR = PROJECT_DIR / 'ui'
SRC_DIR = PROJECT_DIR / 'src'
DEPENDENCE_DIR = PROJECT_DIR / 'dependence'
RESOURCE_DIR = SRC_DIR / 'resource'
INTERFACE_DIR = SRC_DIR / 'interface'
COMMAND_IMPLEMENT_DIR = SRC_DIR / 'common' / 'nuitka_command' / 'command_implement'

CONFIG_FILE = PROJECT_DIR / 'config.json'
QRC_FILE = ASSETS_DIR / 'res.qrc'
QRC_PY_FILE = RESOURCE_DIR / 'rc_res.py'
LOGO_FILE = ASSETS_DIR / 'logo.ico'
CCACHE_DEPENDENCE_FILE = DEPENDENCE_DIR / 'ccache.exe'
DEPENDS_EXE_DEPENDENCE_FILE = DEPENDENCE_DIR / 'depends.exe'
DEPENDS_DLL_DEPENDENCE_FILE = DEPENDENCE_DIR / 'depends.dll'
UPX_DEPENDENCE_FILE = DEPENDENCE_DIR / 'upx.exe'
GCC_EXE_FILE = DEPENDENCE_DIR / 'w64devkit' / 'bin' / 'gcc.exe'
DEPENDENCE_SAVE_PATH_FILE = PROJECT_DIR / 'dependence_save_path.json'
