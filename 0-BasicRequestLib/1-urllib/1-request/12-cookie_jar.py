import http.cookiejar, urllib.request

"""
声明一个 CookieJar 对象，接下来我们就需要利用 HTTPCookieProcessor 来构建一个 Handler，
最后利用 build_opener() 方法构建出 Opener，执行 open() 函数即可。
"""
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)
