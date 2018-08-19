from urllib.parse import urlparse

"""
urlparse 
scheme 参数设置
"""
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)
