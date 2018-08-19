import urllib.parse
import urllib.request

"""
在这里我们传递了一个参数 word，值是 hello,它需要被转码成bytes（字节流）类型。
其中转字节流采用了 bytes() 方法，第一个参数需要是 str（字符串）类型，
需要用 urllib.parse 模块里的 urlencode() 方法来将参数字典转化为字符串。
第二个参数指定编码格式，在这里指定为 utf8。
"""
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
"""
request.urlopen(data=data)，post方式请求数据。 
"""
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
