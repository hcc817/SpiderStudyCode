import urllib.request
from urllib import request
from urllib.robotparser import RobotFileParser

"""
解析robots协议
查询是否符合robots协议
因为简书的robots页面不允许爬虫访问，因此要重写read方法。
"""
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
}


class RobotFileParserAddHeader(RobotFileParser):
    def read(self):
        """Reads the robots.txt URL and feeds it to the parser."""
        try:
            req = request.Request(url=self.url, headers=headers, method='GET')
            f = urllib.request.urlopen(req)
        except urllib.error.HTTPError as err:
            if err.code in (401, 403):
                self.disallow_all = True
            elif 400 <= err.code < 500:
                self.allow_all = True
        else:
            raw = f.read()
            self.parse(raw.decode("utf-8").splitlines())


rp = RobotFileParserAddHeader()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
