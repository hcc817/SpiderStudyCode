from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

"""
在此本地搭建了一个代理，运行在 5555 端口上（使用崔大的本地代理池）。
在这里使用了 ProxyHandler，ProxyHandler 的参数是一个字典，键名是协议类型，比如 HTTP 还是 HTTPS 等，键值是代理链接，可以添加多个代理。
然后利用 build_opener() 方法利用这个 Handler 构造一个 Opener，然后发送请求即可。
"""

import requests

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        res_proxy = requests.get(PROXY_POOL_URL)
        if res_proxy.status_code == 200:
            return res_proxy.text
    except ConnectionError:
        return None


a = get_proxy()
print("代理地址: " + a)
proxy_dict = {a}

proxy_handler = ProxyHandler()
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://icanhazip.com')
    print("本机地址: " + response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
