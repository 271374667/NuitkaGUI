from pathlib import Path

from src.core.paths import UI_DIR

widget_dict: dict[str, str] = {
    "TonalPushButton": "PushButton",
    "FilledPushButton": "PrimaryPushButton",
    "OutlinedPushButton": "PillPushButton",
    "qmaterialwidgets": "qfluentwidgets",
    "OutlinedCardWidget": "SimpleCardWidget",
    "PillPushButton": "PushButton",
    "TextPushButton": "HyperlinkButton"
}


def tran_material2fluent(source_path: Path) -> Path:
    with open(source_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Replace widget names
    target_path = source_path.with_name(source_path.stem + "_fluent" + source_path.suffix)
    with open(target_path, "w", encoding="utf-8") as f:
        for line in lines:
            for key, value in widget_dict.items():
                if key in line:
                    line = line.replace(key, value)
            f.write(line)

    return target_path


if __name__ == '__main__':
    source_path = r"E:\load\python\Project\nuitkaGUIOld\githubOpenSource2\ui\about_page.ui"
    result_path = tran_material2fluent(Path(source_path))
    target_path = UI_DIR / result_path.name
    if target_path.exists():
        target_path.unlink()
    result_path.rename(target_path)
    print(f"Transformed {source_path} to {result_path}, and moved to {target_path}")
