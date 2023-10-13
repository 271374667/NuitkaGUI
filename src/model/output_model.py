from typing import List, Tuple, Union

from src.common.manager.command_manager import CommandManager


class OutputModel:
    def __init__(self):
        self.command_manager = CommandManager()

    def analysis_cmd(self, command: Union[str, list]) -> Tuple[List[str], List[str]]:
        return self.command_manager.analysis_cmd(command)

    def get_red_and_blue_cmd(self, command: str) -> Tuple[List[str], List[str]]:
        """返回需要被染色成红色和蓝色的文字

        在分析的时候为了分析出那些不在界面内的命令，所以需要把所有的命令都染成蓝色，然后把不在界面内的命令染成红色

        Returns:
            Tuple[List[str], List[str]]: 第一个是红色，第二个是蓝色
        """
        cmd_list = self.analysis_cmd(command.split())

        def cmd_tuple2str(cmd: list) -> List[str]:
            result = []
            for each in cmd:
                if isinstance(each, str):
                    result.append(each)
                    continue
                elif isinstance(each, tuple):
                    result.append(each[0])
                    result.extend(each[1])
                    continue
            return result

        red_cmd = cmd_tuple2str(cmd_list[0])
        blue_cmd = cmd_tuple2str(cmd_list[1])
        return red_cmd, blue_cmd

    def get_cmd(self) -> List[str]:
        return self.command_manager.get_cmd()


if __name__ == '__main__':
    commmd = r'nuitka --mingw64 --standalone --show-progress --show-memory --enable-plugin=pyqt5 --output-dir=out 你的.py --fuck'
    m = OutputModel()
    print(m.get_red_and_blue_cmd(commmd))
