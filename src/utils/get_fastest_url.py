"""
Methods:
    get_fastest_url(url_list: list[str]) -> str: fastest url
    通过多线程测试 url 的响应时间，返回最快的 url
"""
from concurrent.futures import ThreadPoolExecutor
from typing import List

import loguru
import requests


def get_fastest_url(url_list: List[str]) -> str:
    loguru.logger.debug(f'正在获取最快的链接: {url_list}')

    def test_speed(url):
        try:
            response = requests.get(url, timeout=5)
            return url, response.elapsed.total_seconds()
        except Exception:
            return url, float('inf')

    def find_fastest_url(urls):
        fastest_url = None
        fastest_time = float('inf')
        with ThreadPoolExecutor() as executor:
            results = executor.map(test_speed, urls)
            for url, response_time in results:
                if response_time < fastest_time:
                    fastest_url = url
                    fastest_time = response_time
                print(f'{url} response time: {response_time}')
        loguru.logger.debug(f'最快的链接: {fastest_url}')
        return fastest_url

    return find_fastest_url(urlList)


if __name__ == '__main__':
    urlList = ['https://www.baidu.com', 'https://www.google.com', 'https://www.bing.com']
    print(get_fastest_url(urlList))
