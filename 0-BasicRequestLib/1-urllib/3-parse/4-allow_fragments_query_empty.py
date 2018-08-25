from urllib.parse import urlparse

"""
如果allow_fragments为false
query部分不存在，则query和fragment均为空
"""
result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result)
