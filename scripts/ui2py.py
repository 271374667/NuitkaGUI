import subprocess
from concurrent.futures import ThreadPoolExecutor

from src.core.paths import UI_DIR, INTERFACE_DIR

count = 0
thread_pool = ThreadPoolExecutor(10)

print("正在清空Ui_*.py文件夹下的所有内容")
# 清空Ui_*.py文件夹下的所有内容
for each in INTERFACE_DIR.glob("**/*.*"):
    if each.stem.startswith("Ui_"):
        print(f"正在删除{each}……")
        each.unlink()


def trans_ui_to_py(ui_file):
    print(f"当前正在转换{ui_file}……")
    py_file = INTERFACE_DIR / f"Ui_{ui_file.stem}.py"
    subprocess.run(["pyside6-uic", ui_file, "-o", py_file])


for ui_file in UI_DIR.glob("**/*.ui"):
    count += 1
    thread_pool.submit(trans_ui_to_py, ui_file)

thread_pool.shutdown(wait=True)
print("正在替换资源文件")
for each in INTERFACE_DIR.glob("**/*.py"):
    if each.stem == "__init__":
        continue

    with open(each, "r", encoding="utf-8") as f:
        content = f.read()
    replace_resut = """from src.resource import rc_res

rc_res = rc_res # 防止格式化的时候资源文件被删除
"""
    content = content.replace("import res_rc", replace_resut)
    with open(each, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"替换{each}的 res 路径成功!")

print("正在格式化")
subprocess.run(
    [
        "ruff",
        "format",
        INTERFACE_DIR,
    ]
)
subprocess.run(["ruff", "check", INTERFACE_DIR, "--fix"])

print(f"Done! {count} files have been converted.")
