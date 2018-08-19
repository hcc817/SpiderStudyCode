from urllib.parse import urlunparse

"""
反解析url
按照 scheme, netloc, url, params, query, fragment，顺序排列。
"""
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
