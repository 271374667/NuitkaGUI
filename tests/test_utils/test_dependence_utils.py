import os
import tempfile
import unittest
from pathlib import Path

from src.utils.dependence_utils import DependenceUtils


class TestDependenceUtils(unittest.TestCase):
    def test_imports_from_simple_file(self):
        content = "import os\nimport sys"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            temp_file.write(content.encode('utf-8'))
            temp_file_path = Path(temp_file.name)

        result = DependenceUtils.get_import_name_from_py_file(temp_file_path)
        self.assertEqual(result, ['os', 'sys'])
        os.remove(temp_file_path)

    def test_imports_from_relative_import(self):
        content = "from . import module"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            temp_file.write(content.encode('utf-8'))
            temp_file_path = Path(temp_file.name)

        result = DependenceUtils.get_import_name_from_py_file(temp_file_path)
        self.assertEqual(result, ['module'])
        os.remove(temp_file_path)

    def test_imports_from_nested_import(self):
        content = "from package.subpackage import module"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            temp_file.write(content.encode('utf-8'))
            temp_file_path = Path(temp_file.name)

        result = DependenceUtils.get_import_name_from_py_file(temp_file_path)
        self.assertEqual(result, ['package'])
        os.remove(temp_file_path)

    def test_no_imports_in_file(self):
        content = "print('Hello, World!')"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            temp_file.write(content.encode('utf-8'))
            temp_file_path = Path(temp_file.name)

        result = DependenceUtils.get_import_name_from_py_file(temp_file_path)
        self.assertEqual(result, [])
        os.remove(temp_file_path)


if __name__ == '__main__':
    unittest.main()
