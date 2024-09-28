import os
import unittest
import winreg
from pathlib import Path

from src.utils.env_utils import EnvUtils


class TestEnvUtils(unittest.TestCase):
    def setUp(self):
        self.env_utils = EnvUtils()
        self.test_path = Path("C:\\test_path")
        self.test_var_name = "TEST_ENV_VAR"
        self.test_var_value = "C:\\test_value"
        self.original_path = os.environ.get("PATH", "")
        self.original_test_var = os.environ.get(self.test_var_name, "")

    def tearDown(self):
        os.environ["PATH"] = self.original_path
        if self.original_test_var:
            os.environ[self.test_var_name] = self.original_test_var
        else:
            os.environ.pop(self.test_var_name, None)

    def test_add_path_to_user_env_by_os(self):
        self.env_utils.add_path_to_user_env_by_os(self.test_path)
        self.assertIn(str(self.test_path), os.environ["PATH"])

    def test_add_path_to_user_env_by_register(self):
        self.env_utils.add_path_to_user_env_by_register(self.test_path)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            current_path = winreg.QueryValueEx(key, "PATH")[0]
        self.assertIn(str(self.test_path), current_path)

    def test_append_path_to_user_env_by_os(self):
        self.env_utils.append_path_to_user_env_by_os(self.test_path, self.test_var_name)
        self.assertIn(str(self.test_path), os.environ[self.test_var_name])

    def test_append_path_to_user_env_by_register(self):
        self.env_utils.append_path_to_user_env_by_register(self.test_path, self.test_var_name)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            current_value = winreg.QueryValueEx(key, self.test_var_name)[0]
        self.assertIn(str(self.test_path), current_value)

    def test_remove_path_from_user_env_by_os(self):
        os.environ["PATH"] = f"{self.test_path};{self.original_path}"
        self.env_utils.remove_path_from_user_env_by_os(self.test_path)
        self.assertNotIn(str(self.test_path), os.environ["PATH"])

    def test_remove_path_from_user_env_by_register(self):
        self.env_utils.add_path_to_user_env_by_register(self.test_path)
        self.env_utils.remove_path_from_user_env_by_register(self.test_path)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            current_path = winreg.QueryValueEx(key, "PATH")[0]
        self.assertNotIn(str(self.test_path), current_path)

    def test_export_user_env(self):
        env_path = self.env_utils.export_user_env()
        self.assertTrue(env_path.exists())
        env_path.unlink()  # Clean up the exported file

    def test_import_user_env(self):
        env_path = self.env_utils.export_user_env()
        self.env_utils.import_user_env(env_path)
        self.assertTrue(env_path.exists())
        env_path.unlink()  # Clean up the exported file


if __name__ == "__main__":
    unittest.main()
