import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["itcast.cn"]
    start_urls = [
        "http://www.itcast.cn/"
    ]

    def parse(self, response):
        content = response.body # response.body 对于html来说相当于整个html页面
        f = open('test.html', 'wb+')
        f.write(content)
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print(title, link, desc)