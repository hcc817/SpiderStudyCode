from urllib.parse import urljoin

"""
urljoin
将域名与字符串拼接。
base_url 提供了三项内容，scheme、netloc、path，
如果这三项在新的链接里面不存在，那么就予以补充.
如果新的链接存在，那么就使用新的链接的部分。
base_url 中的 parameters、query、fragments 是不起作用的。
"""
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://www.jianshu.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://www.jianshu.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://www.jianshu.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
