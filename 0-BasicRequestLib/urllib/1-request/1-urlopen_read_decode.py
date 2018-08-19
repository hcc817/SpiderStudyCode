import urllib.request

"""
使用urllib.1-request.urlopen请求网站
使用response.read()读取获取到的内容
使用.decode('utf-8'),以utf-8解码
"""
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
