from urllib.parse import unquote

"""
url 中文解码
"""
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
