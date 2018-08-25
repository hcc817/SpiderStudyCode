from urllib import request, error

"""
404异常捕获
获取原因，状态码，header
"""
try:
    response = request.urlopen('http://search.mtianyan.cn/1')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
