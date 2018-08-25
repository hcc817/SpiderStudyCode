from urllib.parse import urlsplit

"""
urlsplit 返回 SplitResult
分割完整url
"""
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
