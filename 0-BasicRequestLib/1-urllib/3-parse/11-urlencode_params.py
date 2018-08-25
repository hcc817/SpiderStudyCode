from urllib.parse import urlencode

params = {
    'name': 'mtianyan',
    'age': 21
}
"""
urlencode 将其序列化为 URL 标准 GET 请求参数。
"""
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
