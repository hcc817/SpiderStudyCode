from urllib.parse import parse_qsl

"""
parse_qsl() 方法可以将参数转化为元组组成的列表
"""
query = 'name=mtianyan&age=21'
print(parse_qsl(query))
