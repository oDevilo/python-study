# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['https://movie.douban.com/']
    start_urls = ['https://movie.douban.com//']

    def parse(self, response):
        pass
