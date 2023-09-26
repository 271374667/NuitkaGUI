import subprocess
from pathlib import Path

UI_DIR = Path(__file__).parent.parent / 'ui'
PY_DIR = Path(__file__).parent.parent / 'src' / 'interface'

count = 0

for ui_file in UI_DIR.glob('*.ui'):
    count += 1
    print(f'current is running on {ui_file}')
    py_file = PY_DIR / f'Ui_{ui_file.stem}.py'
    subprocess.run(['pyside6-uic', str(ui_file), '-o', str(py_file)])

print(f'Done! {count} files have been converted.')
