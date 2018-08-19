from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'mtianyan'
}
"""
data参数要求bytes(使用urlencode+bytes)。
req 构造一个Request对象，指明url，data，headers(字典),method。
"""
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')

response = request.urlopen(req)
print(response.read().decode('utf-8'))

"""
可以通过add_header为Request对象添加更多header内容。
"""
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
print(req.headers)
