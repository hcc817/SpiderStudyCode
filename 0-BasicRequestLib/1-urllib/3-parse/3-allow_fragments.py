from urllib.parse import urlparse

"""
将#后面 也就是fragments单独提取进行禁止
query='id=5#comment' query存在的话会被合并进query中
"""
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)
