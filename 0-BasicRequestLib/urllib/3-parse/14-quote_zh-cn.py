from urllib.parse import quote

"""
中文字符转化为 URL 编码
"""
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
