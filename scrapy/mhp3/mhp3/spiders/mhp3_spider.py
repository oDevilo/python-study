import scrapy
from urllib.parse import unquote

class Mhp3Spider(scrapy.Spider):
    name = "mhp3"
    allowed_domains = ["mhp3wiki.duowan.com"]
    start_urls = [
        "http://mhp3wiki.duowan.com/"
    ]

    def parse(self, response):
        f = open('test.html', 'wb+')
        content = response.body # response.body 对于html来说相当于整个html页面
        print("type:", type(content))
        content = content.decode() # 将byte转为str
        print("type:", type(content))
        for sel in response.xpath('//@href'):
            urlstr = sel.extract()
            unquotestr = unquote(urlstr)
            print(unquotestr)
            content = content.replace(urlstr, unquotestr)
        f.write(content.encode()) # 将str转为byte