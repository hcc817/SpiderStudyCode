from urllib import request, error

"""
404异常捕获
"""
try:
    response = request.urlopen('http://search.mtianyan.cn/1')
except error.URLError as e:
    print(e.reason)
