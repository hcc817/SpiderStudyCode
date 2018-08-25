import urllib.request

"""
urllib.1-request.urlopen
返回的类型是HttpResponse
<class 'http.client.HTTPResponse'>
"""
response = urllib.request.urlopen('https://www.python.org')
print(type(response))
