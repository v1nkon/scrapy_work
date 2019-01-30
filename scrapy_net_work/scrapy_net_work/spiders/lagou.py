# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy_net_work.items import PositionDetailItem
import json,time, sys
from urllib.parse import urlencode
class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com', "httpbin.ort/get"]
    common_params = {
        "px": "default",
        "city": "成都",
        "needAddtionalResult": "false"
    }
    common_body = {
        "first": "true",
        "pn": "10",
        "kd": "前端"
    }
    common_url = 'https://www.lagou.com/jobs/positionAjax.json'
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_%E5%89%8D%E7%AB%AF?px=default&city=%E6%88%90%E9%83%BD",
            "X - Requested - With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Accept": "application/json"
        },
        "USER_AGENT" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        "HTTPREQUESTDELAY": {
            "DELAY_ENABLED": True,
            "DELAY_TIME": 2
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
            'scrapy_net_work.pipelines.LagouPositionDetailPipeline': 400
        }
    }


    def start_requests(self):
        self._init_cookies()
        _url = self.common_url + '?' + urlencode(self.common_params)
        yield FormRequest(url=_url, callback=self.parse, cookies=self.cookies, formdata=self.common_body)
        # yield Request(url=test_url, callback=self.parse, cookies=self.cookies)
        pass

    def _init_cookies(self):
        browser = webdriver.Chrome()
        browser.get('https://www.lagou.com/')
        time.sleep(0.5)
        cookie = {}
        for ck in browser.get_cookies():
            cookie[ck['name']] = ck['value']
        self.cookies = cookie

    def parse(self, response):
        try:
            self.common_body['first'] = "false"
            self.common_body["pn"] = str(int(self.common_body["pn"]) + 1)
            _url = self.common_url + '?' + urlencode(self.common_params)
            yield FormRequest(url=_url, callback=self.parse, cookies=self.cookies, formdata=self.common_body)
            positions = json.loads( response.text )['content']['positionResult']['result']
            position_item_list = self.positionDict2Items(positions)
            for _position_item in position_item_list:
                yield _position_item
        except Exception:
            self.logger.error(sys.exc_info())

    def positionDict2Items(self, positions):
        position_field = list(PositionDetailItem().fields.keys())
        position_item_list = []
        for _position in positions:
            position_item = PositionDetailItem()
            for field in position_field:
                _value = _position[field]
                if type(_value) == list:
                    _value = ",".join(_value)
                position_item[field] = _value
            position_item_list.append(position_item)
        return position_item_list

