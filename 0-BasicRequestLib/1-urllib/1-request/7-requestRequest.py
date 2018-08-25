import urllib.request

"""
依然是用urlopen() 方法来发送这个请求，只不过这次 urlopen() 方法的参数不再是一个 URL。
而是一个 Request 类型的对象，通过构造这个这个数据结构。
一方面我们可以将请求独立成一个对象，另一方面可配置参数更加丰富和灵活。
__init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
data:    bytes类型，如果是一个字典，可以先用 urllib.parse 模块里的 urlencode() 编码。
headers: 字典类型， Request Headers，可headers 参数直接构造，也可以通过调用 Request 实例的 add_header() 
"""
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
