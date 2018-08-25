import urllib.request

"""
urlopen 响应超时设置
urllib.error.URLError: <urlopen error timed out>
"""
response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
print(response.read())
