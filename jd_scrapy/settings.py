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
CONCURRENT_REQUESTS = 1
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
    'jd_scrapy.middlewares.ProxyMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,

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
    'jd_scrapy.pipelines.JdItemPipeline': 1,
    # 'jd_scrapy.pipelines.JdCatPipeline': 1
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
    {'ip_port': '124.88.67.17:80', 'user_pass': ''},
    {'ip_port': '121.193.143.249:80', 'user_pass': ''},
    {'ip_port': '119.90.24.25:80', 'user_pass': ''},
    {'ip_port': '221.180.170.2:80', 'user_pass': ''},
    {'ip_port': '106.46.136.104:808', 'user_pass': ''},
    {'ip_port': '106.46.136.162:808', 'user_pass': ''},
    {'ip_port': '122.138.252.65:8118', 'user_pass': ''},
    {'ip_port': '106.46.136.118:808', 'user_pass': ''},
    {'ip_port': '106.46.136.98:808', 'user_pass': ''},
    {'ip_port': '175.155.24.20:808', 'user_pass': ''},
    {'ip_port': '106.120.78.129:80', 'user_pass': ''},
    {'ip_port': '183.32.88.221:808', 'user_pass': ''},
    {'ip_port': '122.229.17.128:80', 'user_pass': ''},
    {'ip_port': '221.180.170.114:80', 'user_pass': ''},
    {'ip_port': '175.21.193.200:8998', 'user_pass': ''},
    {'ip_port': '115.110.118.62:3128', 'user_pass': ''},
    {'ip_port': '5.2.69.135:1080', 'user_pass': ''},
    {'ip_port': '175.18.12.144:8998', 'user_pass': ''},
    {'ip_port': '86.105.55.118:80', 'user_pass': ''},
    {'ip_port': '67.205.156.162:3128', 'user_pass': ''},
    {'ip_port': '149.56.198.196:8080', 'user_pass': ''},
    {'ip_port': '60.214.172.230:8081', 'user_pass': ''},
    {'ip_port': '221.180.170.106:80', 'user_pass': ''},
    {'ip_port': '221.180.170.107:80', 'user_pass': ''},
    {'ip_port': '27.36.157.97:8998', 'user_pass': ''},
    {'ip_port': '120.87.240.235:8998', 'user_pass': ''},
    {'ip_port': '120.84.251.233:80', 'user_pass': ''},
]

WORKING_DIR = 'work/'
FINISH_DIR = 'down/'

MONGODB = {
    'SERVER': 'localhost',
    'PORT': 32770,
    'DB_NAME': 'jd_spider',
    'BOOK_ITEM': 'book_item_multi',
    'BOOK_CAT': 'book_cat'
}
