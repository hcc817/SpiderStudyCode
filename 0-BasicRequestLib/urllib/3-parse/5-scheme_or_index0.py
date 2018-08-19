from urllib.parse import urlparse

"""
获取urlparse 结果的两种方式
索引下标，或对象.属性
"""
result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
