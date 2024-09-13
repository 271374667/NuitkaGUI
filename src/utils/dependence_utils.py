import ast
from pathlib import Path
from typing import List


class DependenceUtils:
    @staticmethod
    def get_import_name_from_py_file(file_path: Path) -> List[str]:
        with file_path.open('r', encoding='utf-8') as file:
            file_content = file.read()

        tree = ast.parse(file_content)
        import_names = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_names.append(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    import_names.append(node.module.split('.')[0])
                else:
                    # Handle relative imports
                    import_names.append(node.names[0].name.split('.')[0])

        return import_names