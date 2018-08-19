from urllib.parse import urlunsplit

"""
urlunsplit
将scheme->fragments规格列表，合并成url
"""
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
