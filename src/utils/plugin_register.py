import importlib.util
from pathlib import Path

import loguru


class PluginRegister:
    @staticmethod
    def load_plugins(search_path: Path, spec_class: type):
        """
        加载指定目录下的所有插件

        Args:
            search_path: 要搜索的目录
            spec_class: 要搜索的插件的父类(不需要实例化)

        Returns:
            插件列表
        """
        plugins = []

        for file in search_path.rglob("*.py"):
            loguru.logger.debug(f"加载了一个文件: {file.stem}")
            spec = importlib.util.spec_from_file_location(file.stem, file)
            if spec is None:
                continue
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # type: ignore

            for obj in vars(module).values():
                if (
                    isinstance(obj, type)
                    and issubclass(obj, spec_class)
                    and obj is not spec_class
                ):
                    plugins.append(obj)
        loguru.logger.info(f"加载了{len(plugins)}个插件")
        return plugins


if __name__ == "__main__":
    from src.common.nuitka_command.command import CommandFlagBase
    from src.core.paths import COMMAND_IMPLEMENT_DIR

    print(
        PluginRegister().load_plugins(
            search_path=COMMAND_IMPLEMENT_DIR, spec_class=CommandFlagBase
        )
    )
