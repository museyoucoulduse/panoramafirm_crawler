# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Firma(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    phone = scrapy.Field()
    url = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    facebook = scrapy.Field()
    business = scrapy.Field()
    panoramafirm = scrapy.Field()
