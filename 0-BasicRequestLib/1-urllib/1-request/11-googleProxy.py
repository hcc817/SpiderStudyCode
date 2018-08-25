import socks
import socket
from urllib import request
import requests

"""
socks5协议，本地需运行着socks5支持，看到本机ip变为代理ip即可。
"""
socks.set_default_proxy(socks.SOCKS5, "localhost", 1080)
socket.socket = socks.socksocket
r = request.urlopen('http://icanhazip.com')

print("urllib 获取的本机地址:", r.read())

r = requests.get('http://icanhazip.com')
print("requests 获取的本机地址:", r.text)
