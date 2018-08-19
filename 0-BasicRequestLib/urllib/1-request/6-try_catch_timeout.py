import socket
import urllib.request
import urllib.error

"""
try except 捕获超时异常。
URLError是time out时抛出的异常。
URLError.reason 存放了这些异常的原因，如果是socket.timeout的一个实例化对象，将打印TIME OUT
"""
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
