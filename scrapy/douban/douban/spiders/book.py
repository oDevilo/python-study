# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['https://book.douban.com/']
    start_urls = ['http://https://book.douban.com//']

    def parse(self, response):
        pass
