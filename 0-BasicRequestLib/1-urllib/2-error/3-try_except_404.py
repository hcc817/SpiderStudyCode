from urllib import request, error

"""
404异常捕获
try catch逻辑处理
"""
try:
    response = request.urlopen('http://search.mtianyan.cn/')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
