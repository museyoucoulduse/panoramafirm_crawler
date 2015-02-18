# -*- coding: utf-8 -*-

# Scrapy settings for panoramafirm_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'panoramafirm_crawler'

SPIDER_MODULES = ['panoramafirm_crawler.spiders']
NEWSPIDER_MODULE = 'panoramafirm_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'lulz (+http://www.hihihi.pl)'

# DOWNLOADER_MIDDLEWARES = {
#  #you need this line in order to scrap through a proxy/proxy list
# 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
# }
