
BOT_NAME = 'nlp3'
SPIDER_MODULES = ['nlp3.spiders']
NEWSPIDER_MODULE = 'nlp3.spiders'



"""proxy list !"""
ROTATING_PROXY_LIST = [
    '62.205.169.74:53281', '37.120.192.154:8080', '51.75.147.44:3128',
    '162.223.89.220:8080', '129.146.249.135:80', '69.63.170.74:3128',
    "41.162.57.82:8080","91.135.148.198:51498","149.28.220.85:3128",
    "83.69.93.64:44331","177.73.44.169:8080","35.187.248.216:8080",
    "49.48.68.144:8080","46.99.180.114:8080","150.129.148.99:35101",
    # ...
]

DOWNLOADER_MIDDLEWARES = {
    # use 2100 different agent setting for crawler!
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    # ...
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    # ...
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nlp3 (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'nlp3.middlewares.Nlp3SpiderMiddleware': 543,
#}




