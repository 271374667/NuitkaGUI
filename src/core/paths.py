from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

ASSETS_DIR = PROJECT_DIR / 'assets'
OUTPUT_DIR = PROJECT_DIR / 'output'
SCRPITS_DIR = PROJECT_DIR / 'scripts'
UI_DIR = PROJECT_DIR / 'ui'
SRC_DIR = PROJECT_DIR / 'src'
RESOURCE_DIR = SRC_DIR / 'resource'
INTERFACE_DIR = SRC_DIR / 'interface'

CONFIG_FILE = PROJECT_DIR / 'config.json'
QRC_FILE = ASSETS_DIR / 'res.qrc'
QRC_PY_FILE = RESOURCE_DIR / 'rc_res.py'
