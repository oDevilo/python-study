# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['https://read.douban.com/']
    start_urls = ['https://read.douban.com/category/?kind=105']

    def parse(self, response):
        f = open('test.html', 'wb+')
        f.write(response.body)
        books = response.xpath('//div')
        print(len(books))
        for book in books:
            print(11111, book.xpath('//span/text()').extract())
