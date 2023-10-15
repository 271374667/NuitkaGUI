from collections import ChainMap
from typing import List, Tuple, Union

from src.core import BoolCommands, IntCommands, StrCommands, JsonSettings
from src.utils.singleton import Singleton
from src.common.manager.settings_manager import SettingsManager


@Singleton
class CommandManager:
    """
    设置的时候通过 set_option_value 和 枚举类 设置，获取的时候通过 get_option_value 和 枚举类 获取
    如果是枚举类里面没有的，可以通过 add_command 添加，通过 remove_command 删除
    """

    def __init__(self):
        self.settings_manager = SettingsManager()

        # create a dict to save state
        self._str_commands_dict = {x: "" for x in StrCommands}
        self._int_commands_dict = {x: 0 for x in IntCommands}
        self._bool_commands_dict = {x: False for x in BoolCommands}
        self._plugins_cmd = []
        self._extra_cmd = ['--assume-yes-for-downloads']
        self._embed_file_cmd = []

        # self._commands_dict = str_commands_dict | bool_commands_dict | int_commands_dict
        self._commands_dict = ChainMap(self._bool_commands_dict, self._str_commands_dict, self._int_commands_dict)

    def get_cmd(self) -> List[str]:
        """
        get nuitka cmd about current enable option

        Returns:
            List[str]: the command list current enable
        """
        if (self._commands_dict[BoolCommands.standalone] is False
                and self._commands_dict[BoolCommands.onefile] is False):
            # standalone and onefile must have one is True
            self._commands_dict[BoolCommands.standalone] = True

        # use a small for-loop 3 times to replace a big for-loop with many if
        enable_cmd_list = []
        # 获取 python 路径，以及填写 nuitka 起手式
        pythonexe_path = self.settings_manager.get(JsonSettings.PYTHONEXE.value)
        if pythonexe_path == '':
            enable_cmd_list.extend(['nuitka'])
        else:
            enable_cmd_list.extend([pythonexe_path, '-m', 'nuitka'])
        for each in BoolCommands:
            current_value = self._commands_dict[each]
            if current_value is not False:
                enable_cmd_list.append(each.value)

        for each in StrCommands:
            current_value = self._commands_dict[each]
            if current_value != "":
                enable_cmd_list.append(f'{each.value}={current_value}')

        for each in IntCommands:
            current_value = self._commands_dict[each]
            if current_value != 0:
                enable_cmd_list.append(f'{each.value}={current_value}')

        # 增加额外的命令
        # TODO: 这一部分未来可以重构，目前为了方便先这样写，到时候需要把这些都用 add_command 来代替
        enable_cmd_list.extend(self._extra_cmd)
        enable_cmd_list.extend(self._embed_file_cmd)
        enable_cmd_list.extend(self._plugins_cmd)

        return enable_cmd_list

    def add_command(self, command: Union[str, List[str]]) -> None:
        """
        增加额外的命令到 nuitka

        Args:
            command: nuitka options, notice this options need to have nuitka version > 1.7.0

        Returns:
            None
        """
        if isinstance(command, str):
            self._extra_cmd.extend(command.split())
            return
        self._extra_cmd.extend(command)

    def remove_command(self, command: Union[str, List[str]]) -> None:
        """删除额外的命令

        该指令只能删除通过 add_command 添加的命令，不能删除默认的命令

        Args:
            command: nuitka options, notice this options need to have nuitka version > 1.7.0

        Returns:
            None
        """
        if isinstance(command, str):
            if command in self._extra_cmd:
                self._extra_cmd.remove(command)
            return
        for each in command:
            if each in self._extra_cmd:
                self._extra_cmd.remove(each)

    def get_option_value(self, command_enum: Union[IntCommands, StrCommands, BoolCommands]) -> Union[bool, str, int]:
        """
        get current option enable or not

        Args:
            command_enum: enum type about IntCommands, Strcommands, BoolCommands

        Returns:
            bool, str, int: current option value
        """
        return self._commands_dict.get(command_enum)

    def set_option_value(self, command_enum: Union[IntCommands, StrCommands, BoolCommands],
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
            self._commands_dict[command_enum] = value

    def clear_option_value(self, command_enum: Union[IntCommands, StrCommands, BoolCommands]) -> None:
        """
        clear option value

        Args:
            command_enum: enum type about IntCommands, Strcommands, BoolCommands

        Returns:
            None
        """
        if isinstance(command_enum, BoolCommands):
            self._commands_dict[command_enum] = False
            return
        elif isinstance(command_enum, StrCommands):
            self._commands_dict[command_enum] = ""
            return
        self._commands_dict[command_enum] = 0

    def analysis_cmd(self, command: Union[str, list]) -> Tuple[List[str], List[str]]:
        """parse str or list cmd and return current support options and not supported

        this func is to distinguish options current nuitkaGUI is supported and not supported

        Args:
            command: nuitka options, notice this options need to have nuitka version > 1.7.0

        Returns:
            List[str]: available cmd about nuitkaGUI,because I didn't put all options in nuitkaGUI
            List[str]: unavailable cmd about nuitkaGUI
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
                # 因为现在的key是enum所以需要将str转换成enum
                if self.str_command2enum(each[0]) in self._commands_dict:
                    available_cmd.append(each)
                    continue
                unavailable_cmd.append(each)
                continue

            elif self.str_command2enum(each) in self._commands_dict:
                available_cmd.append(each)
                continue
            unavailable_cmd.append(each)
        return available_cmd, unavailable_cmd

    def set_embed_file_cmd(self, cmd: List[str]) -> None:
        """设置嵌入文件命令"""
        self._embed_file_cmd = cmd

    def set_plugins_cmd(self, cmd: List[str]) -> None:
        """设置插件命令"""
        self._plugins_cmd = cmd

    def get_extra_cmd(self) -> List[str]:
        """获取额外的命令"""
        return self._extra_cmd

    def str_command2enum(self, command: str) -> Union[IntCommands, StrCommands, BoolCommands]:
        """将字符串命令转换成枚举类"""
        command_key_dict = {x.value: x for x in self._commands_dict.keys()}
        if command in command_key_dict:
            return command_key_dict[command]

    def __set_onefile(self, value: bool) -> None:
        # disable standalone mode selection
        self._commands_dict[BoolCommands.standalone] = False
        self._commands_dict[BoolCommands.onefile] = value

    def __set_standalone(self, value: bool) -> None:
        self._commands_dict[BoolCommands.onefile] = False
        self._commands_dict[BoolCommands.standalone] = value


if __name__ == '__main__':
    from pprint import pprint

    m = CommandManager()
    # m.set_option_value(BoolCommands.onefile, True)
    # m.set_option_value(BoolCommands.standalone, True)
    # m.set_option_value(BoolCommands.show_progress, True)
    # m.set_option_value(BoolCommands.show_memory, True)
    # m.set_option_value(StrCommands.output_dir, 'output_dir')
    # m.set_option_value(IntCommands.jobs, 4)
    # m.add_command('--assume-yes-for-downloads')
    # m.add_command('--windows-icon-from-ico=icon.ico')
    # m.add_command('--windows-company-name=company_name')
    # m.remove_command('--windows-company-name=company_name')
    # print(m.get_cmd())
    # print(m.get_option_value(BoolCommands.onefile))
    commmd = r'python -m nuitka --output-dir=D:\打包结果\数据处理工具,haha,66 testDtsRun.py'
    commmd2 = r'nuitka --mingw64 --standalone --show-progress --show-memory --enable-plugin=pyqt5 --output-dir=out 你的.py'
    pprint(m.analysis_cmd(commmd2))
    print(m.str_command2enum('--nofollow-import-to'))
