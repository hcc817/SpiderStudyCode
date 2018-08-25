__author__ = 'mtianyan'
__date__ = '2018/8/24 08:11'

import requests
import re

content = requests.get("https://book.douban.com/").text
# print(content)


p = re.compile(
    '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?',re.S)
result = re.findall(p, content)
print(result)
