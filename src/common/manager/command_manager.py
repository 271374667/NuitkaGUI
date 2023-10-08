from collections import ChainMap
from enum import Enum
from typing import List, Union


class BoolCommands(Enum):
    onefile = '--onefile'
    standalone = '--standalone'
    show_progress = '--show-progress'
    show_memory = '--show-memory'
    remove_output = '--remove-output'
    windows_disable_console = '--windows-disable-console'
    mingw64 = '--mingw64'
    quiet = '--quiet'
    lto_no = '--lto=no'
    disable_ccache = '--disable-ccache'
    assume_yes_for_downloads = '--assume-yes-for-downloads'
    clang = '--clang'
    windows_uac_admin = '--windows-uac-admin'


class StrCommands(Enum):
    output_dir = '--output-dir'
    main = '--main'
    nofollow_import_to = '--nofollow-import-to'
    include_package = '--include-package'
    windows_icon_from_ico = '--windows-icon-from-ico'
    windows_company_name = '--windows-company-command_enum'
    windows_file_version = '--windows-file-version'
    windows_product_version = '--windows-product-version'
    windows_file_description = '--windows-file-description'
    onefile_tempdir_spec = '--onefile-tempdir-spec'


class IntCommands(Enum):
    jobs = '--jobs'


class CommandManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # create a dict to save state
        self._str_commands_dict = {x.value: "" for x in StrCommands}
        self._int_commands_dict = {x.value: 0 for x in IntCommands}
        self._bool_commands_dict = {x.value: False for x in BoolCommands}
        self._plugins_dict = {}
        self.extra_cmd = []

        # self._commands_dict = str_commands_dict | bool_commands_dict | int_commands_dict
        self._commands_dict = ChainMap(self._bool_commands_dict, self._str_commands_dict, self._int_commands_dict)

    def __set_onefile(self, value: bool) -> None:
        # disable standalone mode selection
        self._commands_dict[BoolCommands.standalone.value] = False
        self._commands_dict[BoolCommands.onefile.value] = value

    def __set_standalone(self, value: bool) -> None:
        self._commands_dict[BoolCommands.onefile.value] = False
        self._commands_dict[BoolCommands.standalone.value] = value

    def add_command(self, command: Union[str, List[str]]) -> None:
        """
        增加额外的命令到 nuitka

        Args:
            command: nuitka options, notice this options need to have nuitka version > 1.7.0

        Returns:
            None
        """
        if isinstance(command, str):
            self.extra_cmd.append(command.split())
            return
        self.extra_cmd.extend(command)

    def remove_command(self, command: Union[str, List[str]]) -> None:
        """删除额外的命令

        该指令只能删除通过 add_command 添加的命令，不能删除默认的命令

        Args:
            command: nuitka options, notice this options need to have nuitka version > 1.7.0

        Returns:
            None
        """
        if isinstance(command, str):
            if command in self.extra_cmd:
                self.extra_cmd.remove(command)
            return
        for each in command:
            if each in self.extra_cmd:
                self.extra_cmd.remove(each)

    def get_extra_cmd(self) -> List[str]:
        """获取额外的命令"""
        return self.extra_cmd

    def set_plugin(self, plugin_name: str, plugin_status: bool) -> None:
        """添加插件

        通过字典的方式添加插件，插件的名字作为键，插件的状态作为值，True 为启用，False 为禁用

        Args:
            plugin_name: 插件的名字
            plugin_status: 插件的状态

        Returns:
            None
        """
        self._plugins_dict[plugin_name] = plugin_status

    def set_value(self, command_enum: Union[IntCommands, StrCommands, BoolCommands],
                  value: Union[int, str, bool]) -> None:
        """
        control nuikta options enable and value

        Args:
            command_enum: enum type about IntCommands, Strcommands, BoolCommands
            value: must be same type as command_enum like int, str, bool

        Returns:
            None
        """
        if command_enum == BoolCommands.onefile:
            self.__set_onefile(value)
        elif command_enum == BoolCommands.standalone:
            self.__set_standalone(value)
        else:
            self._commands_dict[command_enum.value] = value

    def get_cmd(self) -> List[str]:
        """
        get nuitka cmd about current enable option

        Returns:
            List[str]: the command list current enable
        """
        if (self._commands_dict[BoolCommands.standalone.value] is False
                and self._commands_dict[BoolCommands.onefile.value] is False):
            # standalone and onefile must have one is True
            self._commands_dict[BoolCommands.standalone.value] = True

        # use a small for-loop 3 times to replace a big for-loop with many if
        enable_cmd_list = []
        for each in BoolCommands:
            current_value = self._commands_dict[each.value]
            if current_value is not False:
                enable_cmd_list.append(each.value)

        for each in StrCommands:
            current_value = self._commands_dict[each.value]
            if current_value != "":
                enable_cmd_list.append(f'{each.value}={current_value}')

        for each in IntCommands:
            current_value = self._commands_dict[each.value]
            if current_value != 0:
                enable_cmd_list.append(f'{each.value}={current_value}')

        # 增加额外的命令
        enable_cmd_list.extend(self.extra_cmd)

        # 增加插件
        enable_plugin_list = [
                key for key, value in self._plugins_dict.items() if value is True
                ]
        enable_cmd_list.extend(f'--enable-plugin={",".join(enable_plugin_list)}')

        return enable_cmd_list

    def analysis_cmd(self, command: Union[str, List]) -> (List[str], List[str]):
        """parse str or list cmd and return current support options and not supported

        this func is to distinguish options current nuitkaGUI is supported and not supported

        Args:
            command: nuitka options, notice this options need to have nuitka version > 1.7.0

        Returns:
            List: available cmd about nuitkaGUI,because I didn't put all options in nuitkaGUI
            List: available cmd about nuitkaGUI
        """
        cmd_list = []
        available_cmd = []
        unavailable_cmd = []

        def _append_condition(x: str):
            return ('python' not in x) and (x != '-m') and (x != 'nuitka') and (x.endswith('.py') is False)

        # 根据是字符串还是列表进行不同的处理
        if isinstance(command, str):
            # 先根据空格分割，再根据等号分割，最后根据逗号分割，删去nuitka和python和-m和.py结尾的
            # 这里只负责往cmd_list里面添加，不负责判断是否可用
            content = command.split()
            for each in content:
                # 因为命令有两种一种是有等号的需要赋值的，这里使用split将 key 和 value 分别变成元组
                # 他们看起来像是这样的 ('--output-dir', ('D:\\打包结果\\数据处理工具', 'haha', '66'))
                # 一种是没有等号的,这里直接添加到列表里面
                if '=' in each:
                    item_key, item_value = each.split('=')
                    item_value_list = tuple(item_value.split(','))
                    cmd_list.append((item_key, item_value_list))
                    continue
                elif _append_condition(each):
                    cmd_list.append(each)

        elif isinstance(command, List):
            for each in command:
                if '=' in each:
                    item_key, item_value = each.split('=')
                    item_value_list = tuple(item_value.split(','))
                    cmd_list.append((item_key, item_value_list))
                    continue
                elif _append_condition(each):
                    cmd_list.append(each)

        # 根据cmd_list里面的内容判断是否可用
        for each in cmd_list:
            if isinstance(each, tuple):
                if each[0] in self._commands_dict:
                    available_cmd.append(each)
                    continue
                unavailable_cmd.append(each)
                continue

            elif each in self._commands_dict:
                available_cmd.append(each)
                continue
            unavailable_cmd.append(each)
        return available_cmd, unavailable_cmd


if __name__ == '__main__':
    from pprint import pprint

    m = CommandManager()
    # m.set_value(BoolCommands.onefile, True)
    # m.set_value(BoolCommands.standalone, True)
    # m.set_value(BoolCommands.show_progress, True)
    # m.set_value(BoolCommands.show_memory, True)
    # m.set_value(StrCommands.output_dir, 'output_dir')
    # m.set_value(IntCommands.jobs, 4)
    #
    # print(m.get_cmd())
    commmd = r'python -m nuitka --output-dir=D:\打包结果\数据处理工具,haha,66 testDtsRun.py'
    pprint(m.analysis_cmd(commmd))
