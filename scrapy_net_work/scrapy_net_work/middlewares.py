# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.exceptions import NotConfigured
import random, time

class HttpSetProxy(object):
    def __init__(self, mysql_util, HttpSetProxy):
        self.mysql_util = mysql_util
        self.HttpSetProxy = HttpSetProxy
        self.http_proxy_list = []
        self.https_proxy_list = []

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        HttpSetProxy = crawler.settings.getdict("HTTPSETPROXY")
        if not HttpSetProxy.get('HttpSetProxyEnabled'):
            raise NotConfigured

        s = cls(crawler.mysql_util, HttpSetProxy)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self):
        mysql_util = self.mysql_util
        country = self.HttpSetProxy.get('HttpProxyCountry')
        table = self.HttpSetProxy.get('HttpProxyTable')
        _sql = "select proxyIp, proxyPort from {0} where country = '{1}'".format(table, country) + " and proxyType = '{0}' and anonymity = 'high_anonymous' ;"
        mysql_util.execute(_sql.format("http"))
        self.http_proxy_list = mysql_util.cursor.fetchall()
        mysql_util.execute(_sql.format('https'))
        self.https_proxy_list = mysql_util.cursor.fetchall()


    def process_request(self, request, spider):
        print("execute HttpSetProxy")
        protocal = request.url.split(':')[0]
        proxy = ''
        if protocal == 'https':
            # https://218.57.146.212.8888
            https_ip, https_port = random.choice(self.https_proxy_list)
            proxy = "https://" + https_ip + ':' + https_port
            request.meta['proxy'] = proxy
        else:
            http_ip, http_port = random.choice(self.http_proxy_list)
            proxy = "http://" + http_ip + ':' + http_port
            request.meta['proxy'] = proxy


class HttpRequestDelay(object):
    def __init__(self, delay_time):
        self.delay_time = delay_time
        pass

    @classmethod
    def from_crawler(cls, crawler):
        HttpRequestDelay = crawler.settings.getdict("HTTPREQUESTDELAY")
        if not HttpRequestDelay.get('DELAY_ENABLED'):
            raise NotConfigured
        s = cls(HttpRequestDelay.get("DELAY_TIME", 0))
        return s
        pass

    def process_request(self, request, spider):
        delay = random.random()
        delay + self.delay_time
        time.sleep(delay)
        pass




