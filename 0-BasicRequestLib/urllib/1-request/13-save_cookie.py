import http.cookiejar
import urllib.request

"""
保存cookie
"""
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)