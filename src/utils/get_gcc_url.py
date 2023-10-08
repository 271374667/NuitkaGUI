from typing import Optional

import loguru
import requests

origin_url = 'https://wwvv.lanzout.com/ipSUN15naxmf'
parse_url = 'https://lz.qaiu.top/json/parser?url=https://wwvv.lanzout.com/ipSUN15naxmf'

data = {'url': origin_url}


def get_gcc_url() -> Optional[str]:
    try:
        loguru.logger.debug('正在尝试解析蓝奏云直链')
        response = requests.get(parse_url, json=data)
        return None if response.status_code != 200 else response.json()['data']
    except Exception as e:
        loguru.logger.error(f'蓝奏云直链解析失败: {e}')
        return None


if __name__ == '__main__':
    print(get_gcc_url())
