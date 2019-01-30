# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, Request
from scrapy_net_work.items import ImageItem

class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    # allowed_domains = ['daimg.com']
    # start_urls = ['http://www.daimg.com/']
    allowed_domains = ['mzitu.com', 'meizitu.net']
    start_urls = ['https://m.mzitu.com/xinggan/page/1']
    cur_page = 1
    total_pages = 2
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS" : {
            "Referer": "https://m.mzitu.com/xinggan/"
        },
        "HTTPREQUESTDELAY":{
            "DELAY_ENABLED":True,
            "DELAY_TIME":0.5
        },
        "DOWNLOADER_MIDDLEWARES" : {
            'scrapy_net_work.middlewares.HttpRequestDelay': 100,
        },
        "HTTPSETPROXY" : {
            'HttpSetProxyEnabled': False,
            'HttpNotSetProxyReg': '.html',
            'HttpProxyCountry': 'CN',
            'HttpProxyTable': 'github_proxy'
        }
    }

    # allowed_domains = ["httpbin.ort/get"]
    # start_urls = ['https://httpbin.org/get']

    # def __init__(self):




    def parse(self, response):
        # print(response.text)
        if self.cur_page < self.total_pages:
            self.cur_page += 1
            yield Request(url='https://m.mzitu.com/xinggan/page/{0}'.format(self.cur_page), callback=self.parse)
        sel = Selector(response)
        image_urls = sel.css('img::attr(data-original)').extract()
        image_urls_arr = []
        item = ImageItem()

        for image_url in image_urls:
            if image_url.find('http') != -1:
                image_urls_arr.append( image_url )
        item['image_urls'] = image_urls_arr
        yield item
