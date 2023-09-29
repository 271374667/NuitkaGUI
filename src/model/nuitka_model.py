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


class NuitkaModel:
    def __init__(self):
        # create a dict to save state
        self._str_commands_dict = {x.value: "" for x in StrCommands}
        self._int_commands_dict = {x.value: 0 for x in IntCommands}
        self._bool_commands_dict = {x.value: False for x in BoolCommands}

        # self._commands_dict = str_commands_dict | bool_commands_dict | int_commands_dict
        self._commands_dict = ChainMap(self._bool_commands_dict, self._str_commands_dict, self._int_commands_dict)

    def __set_onefile(self, value: bool):
        # disable standalone mode selection
        self._commands_dict[BoolCommands.standalone.value] = False
        self._commands_dict[BoolCommands.onefile.value] = value

    def __set_standalone(self, value: bool):
        self._commands_dict[BoolCommands.onefile.value] = False
        self._commands_dict[BoolCommands.standalone.value] = value

    def set_value(self, command_enum: Union[IntCommands, StrCommands, BoolCommands], value: Union[int, str, bool]):
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

        if isinstance(command, str):
            # only left option, remove python path and -m
            content = command.split()
            for each in content:
                if '=' in each:
                    item_key, item_value = each.split('=')
                    item_value_list = tuple(item_value.split(','))
                    cmd_list.append((item_key, item_value_list))
                    continue
            cmd_list.extend(
                    each for each in content if ('python' not in each) and (each != '-m') and (each != 'nuitka')
                    )
        elif isinstance(command, List):
            for each in command:
                if '=' in each:
                    item_key, item_value = each.split('=')
                    item_value_list = tuple(item_value.split(','))
                    cmd_list.append((item_key, item_value_list))
                    continue
            cmd_list.extend(
                    each for each in command if ('python' not in each) and (each != '-m') and (each != 'nuitka')
                    )

        for each in cmd_list:
            if isinstance(each, tuple):
                if each[0] in self._commands_dict:
                    available_cmd.append(each)
                    continue
                unavailable_cmd.append(each)
                continue

            if each in self._commands_dict:
                available_cmd.append(each)
                continue
            unavailable_cmd.append(each)
        return available_cmd, unavailable_cmd


if __name__ == '__main__':
    from pprint import pprint

    m = NuitkaModel()
    # m.set_value(BoolCommands.onefile, True)
    # m.set_value(BoolCommands.standalone, True)
    # m.set_value(BoolCommands.show_progress, True)
    # m.set_value(BoolCommands.show_memory, True)
    # m.set_value(StrCommands.output_dir, 'output_dir')
    # m.set_value(IntCommands.jobs, 4)
    #
    # print(m.get_cmd())
    commmd = 'nuitka --mingw64 --windows-disable-console --standalone --show-progress --show-memory --plugin-enable=qt-plugins --plugin-enable=pylint-warnings --recurse-all --recurse-not-to=numpy,jinja2,matplotlib,scipy,sqlalchemy,pandas,pygal,pyzbar,pubunit,qtunit,dataunit --output-dir=D:\打包结果\数据处理工具 testDtsRun.py'
    pprint(m.analysis_cmd(commmd))
