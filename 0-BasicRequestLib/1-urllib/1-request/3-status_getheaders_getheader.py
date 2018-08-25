import urllib.request

"""
response.status 获取Response 状态码
response.getheaders 获取头部信息，类型是list，每一项信息是一个元组
response.getheader('Server') 传入参数，获取某一项信息。
"""
response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(type(response.getheaders()))
print(response.getheader('Server'))
