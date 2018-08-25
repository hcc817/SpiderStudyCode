from urllib.parse import urlsplit

"""
urlsplit中获取单个成员的两种方式
对象.属性 或 index
"""
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme, result[0])
