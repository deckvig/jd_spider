# -*- coding: utf-8 -*-

# Scrapy settings for jd_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_scrapy'

SPIDER_MODULES = ['jd_scrapy.spiders']
NEWSPIDER_MODULE = 'jd_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'jd_scrapy (+http://www.yourdomain.com)'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# CONCURRENT_REQUESTS = 32
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# RANDOMIZE_DOWNLOAD_DELAY = True
# DOWNLOAD_DELAY = 0.5  
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True
# LOG_LEVEL = 'INFO'
REDIRECT_ENABLED = False
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = True

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# DEFAULT_REQUEST_HEADERS = {
#     # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
#     'User-Agent': '* Baiduspider+(+http://www.baidu.com/search/spider.htm”)',
#     'Connection': 'keep-alive',
#     'Referer': 'http://book.jd.com/booksort.html',
# }
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'jd_scrapy.middlewares.RandomUserAgentMiddleware': 543,
#     'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': None,
# }
DOWNLOADER_MIDDLEWARES = {
    'jd_scrapy.middlewares.RandomUserAgentMiddleware': 1,
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': None,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'jd_scrapy.pipelines.JdItemPipeline': 1,
    'jd_scrapy.pipelines.JdCatPipeline': 1
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


PROXIES = [
    {'ip_port': '171.36.154.217:8998', 'user_pass': ''},
    {'ip_port': '101.31.63.250:8998', 'user_pass': ''},
    {'ip_port': '119.90.24.24:80', 'user_pass': ''},
    {'ip_port': '221.180.170.17:80', 'user_pass': ''},
    {'ip_port': '123.166.39.112:8118', 'user_pass': ''},
    {'ip_port': '114.239.3.27:808', 'user_pass': ''},
    {'ip_port': '110.7.73.138:80', 'user_pass': ''},
    {'ip_port': '175.155.25.13:808', 'user_pass': ''},
    {'ip_port': '110.72.26.222:8123', 'user_pass': ''},
    {'ip_port': '119.5.0.66:808', 'user_pass': ''},
    {'ip_port': '110.73.4.242:8123', 'user_pass': ''},
    {'ip_port': '220.166.243.22:8118', 'user_pass': ''},
    {'ip_port': '106.46.136.230:808', 'user_pass': ''},
    {'ip_port': '113.99.216.190:8081', 'user_pass': ''},
    {'ip_port': '178.33.4.48:3128', 'user_pass': ''},
    {'ip_port': '106.91.35.74:8998', 'user_pass': ''},
    {'ip_port': '200.229.202.214:8080', 'user_pass': ''},
    {'ip_port': '123.125.14.246:3128', 'user_pass': ''},
    {'ip_port': '159.203.166.76:3128', 'user_pass': ''},
    {'ip_port': '89.36.213.168:3128', 'user_pass': ''},
    {'ip_port': '86.105.55.21:3128', 'user_pass': ''},
    {'ip_port': '69.12.92.6:1080', 'user_pass': ''},
    {'ip_port': '106.120.40.103:1080', 'user_pass': ''},
    {'ip_port': '177.42.129.227:8080', 'user_pass': ''},
    {'ip_port': '120.52.72.56:80', 'user_pass': ''},
    {'ip_port': '124.88.67.14:843', 'user_pass': ''},
    {'ip_port': '159.192.200.47:8080', 'user_pass': ''},
    {'ip_port': '222.128.80.28:8081', 'user_pass': ''},
    {'ip_port': '47.91.145.28:3128', 'user_pass': ''},
    {'ip_port': '113.237.70.237:8081', 'user_pass': ''},
    {'ip_port': '35.167.66.19:3128', 'user_pass': ''},
    {'ip_port': '69.12.67.180:1080', 'user_pass': ''},
]

WORKING_DIR = 'work/'
FINISH_DIR = 'down/'

MONGODB = {
    'SERVER': 'localhost',
    'PORT': 32770,
    'DB_NAME': 'jd_spider',
    'BOOK_ITEM': 'book_item',
    'BOOK_CAT': 'book_cat'
}
