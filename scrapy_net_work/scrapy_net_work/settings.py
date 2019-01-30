# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_net_work project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_net_work'

SPIDER_MODULES = ['scrapy_net_work.spiders']
NEWSPIDER_MODULE = 'scrapy_net_work.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent

USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_net_work.middlewares.ScrapyNetWorkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_net_work.middlewares.HttpSetProxy': 1,
#    # 'scrapy_net_work.middlewares.ScrapyNetWorkDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    # 引入Scrapy提供的ImagesPipeline组件
    'scrapy.pipelines.images.ImagesPipeline': 300,
    'scrapy_net_work.pipelines.LagouPositionPipeline':400
}
# ImagesPipeline辅助配置项
# 图片存储路径(绝对路径 or 相对路径)
IMAGES_STORE = 'images'
# 该字段的值为XxxItem中定义的存储图片链接的image_urls字段
IMAGES_URLS_FIELD='image_urls'
# 该字段的值为XxxItem中定义的存储图片信息的images字段
IMAGES_RESULT_FIELD='images'
# 生成缩略图(可选)
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
# 过期时间,单位:天(可选)
IMAGES_EXPIRES = 120
# 过滤小图片(可选)
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
# 是否允许重定向(可选)
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



#拓展
EXTENSIONS = {
    'scrapy_net_work.extensions.MysqlUtil': 100
}


#日志相关
LOG_ENABLED = True

LOG_ENCODING = 'utf-8'

# LOG_FILE="scrapy.log"

LOG_FORMAT = '%(asctime)s %(filename)s %(lineno)s [%(name)s] %(levelname)s: %(message)s'

#数据库相关

DATABASE_ENABLED = True

DATABASE_NAME = 'crawler'

DATABASE_HOST = 'localhost'

DATABASE_PORT = 3306

DATABASE_USER = 'root'

DATABASE_PASSWORD = '123456'

#是否使用自定义代理

# HTTPSETPROXY = {
#     'HttpSetProxyEnabled' : True,
#     'HttpProxyCountry': 'CN',
#     'HttpProxyTable': 'github_proxy'
# }

DOWNLOADER_MIDDLEWARES = {
    #自定义代理
    'scrapy_net_work.middlewares.HttpSetProxy': 1,
   # 'scrapy_net_work.middlewares.ScrapyNetWorkDownloaderMiddleware': 543,
}



