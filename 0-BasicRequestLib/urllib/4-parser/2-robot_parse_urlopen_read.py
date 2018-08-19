from urllib import request
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

url = 'http://www.jianshu.com/robots.txt'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
}

req = request.Request(url=url, headers=headers, method='GET')
robot_txt = urlopen(req).read().decode('utf-8').split('\n')
rp = RobotFileParser()
rp.parse(robot_txt)
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))