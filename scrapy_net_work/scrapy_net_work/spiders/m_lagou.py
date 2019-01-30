# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy_net_work.items import PositionItem
import json,time
from urllib.parse import urlencode

class LagouSpider(scrapy.Spider):
    name = 'm_lagou'
    allowed_domains = ['lagou.com', "httpbin.ort/get"]
    start_urls = ['https://m.lagou.com/']
    common_params = {
        "city": "重庆",
        "positionName": "前端",
        "pageNo": 1,
        "pageSize": "15",
    }
    common_url = 'https://m.lagou.com/listmore.json'
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'Host': 'm.lagou.com',
            "Referer": "https://m.lagou.com/",
            "X - Requested - With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Accept": "application/json"
        },
        "HTTPREQUESTDELAY": {
            "DELAY_ENABLED": True,
            "DELAY_TIME": 0.5
        },
        "HTTPSETPROXY": {
            'HttpSetProxyEnabled': True,
            'HttpNotSetProxyReg': '.html',
            'HttpProxyCountry': 'CN',
            'HttpProxyTable': 'github_proxy'
        },
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy_net_work.middlewares.HttpSetProxy': 1,
            'scrapy_net_work.middlewares.HttpRequestDelay': 100
        },
        "ITEM_PIPELINES" : {
            'scrapy_net_work.pipelines.LagouPositionPipeline': 400
        }
    }


    def start_requests(self):
        self._init_cookies()
        _url = self.common_url + '?' + urlencode(self.common_params)
        test_url = 'https://httpbin.org/get' + '?' + urlencode(self.common_params)
        yield Request(url=_url, callback=self.parse, cookies=self.cookies)
        # yield Request(url=test_url, callback=self.parse, cookies=self.cookies)
        pass

    def _init_cookies(self):
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.get('https://m.lagou.com/search.html')
        wait.until(lambda browser:browser.find_element_by_css_selector("input.inputer"))
        time.sleep(0.5)
        browser.find_element_by_css_selector("div.lbutton").click()
        time.sleep(0.1)
        browser.find_element_by_css_selector('[data-item="成都"]').click()
        time.sleep(0.1)
        input = browser.find_element_by_css_selector("input.inputer").send_keys("前端")
        time.sleep(0.1)
        browser.find_element_by_css_selector("span.search").click()
        time.sleep(0.1)
        cookie = {}
        for ck in browser.get_cookies():
            cookie[ck['name']] = ck['value']
        self.cookies = cookie

    def parse(self, response):
        self.common_params['pageNo'] = self.common_params['pageNo'] + 1
        _url = self.common_url + '?' + urlencode(self.common_params)
        yield Request(url=_url, callback=self.parse, cookies=self.cookies)
        positions = json.loads( response.text )['content']['data']['page']['result']
        position_item_list = self.positionDict2Items(positions)
        for _position_item in position_item_list:
            yield _position_item

    def positionDict2Items(self, positions):
        position_field = list(PositionItem().fields.keys())
        position_item_list = []
        for _position in positions:
            position_item = PositionItem()
            for field in position_field:
                position_item[field] = _position[field]
            position_item_list.append(position_item)
        return position_item_list

