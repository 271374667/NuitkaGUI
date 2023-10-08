import subprocess
from pathlib import Path
from src.conf import config_path

UI_DIR = config_path.PROJECT_DIR / 'ui'
PY_DIR = config_path.SRC_HOME / 'interface'

count = 0
# TODO: 新建了一个components文件夹，里面放了一些组件，需要把他们也转换成py文件,丢到interface/component里面
for ui_file in UI_DIR.glob('**/*.ui'):
    count += 1
    print(f'当前正在转换{ui_file}……')

    py_file = PY_DIR / f'Ui_{ui_file.stem}.py'
    if py_file.parent == 'component':
        py_file = PY_DIR / 'component' / f'Ui_{ui_file.stem}.py'
    subprocess.run(['pyside6-uic', ui_file, '-o', py_file])

print('正在替换资源文件')
for each in PY_DIR.glob('**/*.py'):
    if each.stem == "__init__":
        continue

    with open(each, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('import res_rc', 'from src.resource import rc_res')
    with open(each, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'替换{each}的 res 路径成功!')

print(f'Done! {count} files have been converted.')
