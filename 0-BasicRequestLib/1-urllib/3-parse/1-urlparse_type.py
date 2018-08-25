from urllib.parse import urlparse

"""
urlparse 返回类型
<class 'urllib.parse.ParseResult'>
"""
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
