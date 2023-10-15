"""
负责管理默认的配置文件，这个配置文件是一个json文件，里面包含了一些默认的配置信息，
包括 python.exe 的位置, 默认的下载源，以及一些其他的配置信息
"""
import json
from copy import deepcopy
from typing import Union

from src.conf import config, config_path
from src.core import JsonSettings
from src.utils.singleton import Singleton


@Singleton
class SettingsManager:
    def __init__(self):
        self._settings = deepcopy(config.JSON_SETTINGS_DICT)
        # self._settings = {
        #         JsonSettings.PYTHONEXE.value: '',
        #         JsonSettings.FASTEST_PIP_SOURCE.value: 'https://pypi.org/simple',
        #         JsonSettings.GCC_AVAILABLE.value: False,
        #         JsonSettings.FIRST_RUN.value: True,
        #         JsonSettings.OPTIMIZATION_ENABLED.value: True
        #         }
        self._settings_file = config_path.SETTINGS_FILE
        self.initialize()

    def get(self, key: str) -> Union[str, bool]:
        """获取配置信息, key 可以从当前类的属性中获取"""
        return self._settings.get(key)

    def set(self, key: str, value: Union[str, bool]) -> None:
        """设置配置信息, key 可以从当前类的属性中获取"""
        self._settings[key] = value
        self._save()

    def clear(self) -> None:
        """清除配置信息"""
        self._settings = {}
        self._save()

    def _save(self) -> None:
        content = json.dumps(self._settings, indent=4)
        self._settings_file.write_text(content, encoding='utf-8')

    def initialize(self) -> None:
        if not self._settings_file.exists():
            self._settings_file.touch()
            self._settings_file.write_text(json.dumps(self._settings, indent=4), encoding='utf-8')

        content = self._settings_file.read_text(encoding='utf-8')
        if content == '':
            content = '{}'  # 防止 json.loads() 报错
        content_json = json.loads(content)

        # 这里是为了让设置文件中的配置项与默认配置项保持一致，只有当设置文件中的配置项不存在时才会使用默认配置项
        for default in self._settings:
            if default not in content:
                continue
            self._settings[default] = content_json[default]


if __name__ == '__main__':
    sm = SettingsManager()
    sm.initialize()
    sm.set('first_run', True)
    print(sm.get('first_run'))
    print(sm.get(JsonSettings.FASTEST_PIP_SOURCE.value))
