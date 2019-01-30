# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        link = LinkExtractor(tags=('a','script'), attrs=('href', 'src'))
        list = link.extract_links(response)
        print(list)
        print(response)

