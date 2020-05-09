# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class articles2(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    body = scrapy.Field()
    title = scrapy.Field()

class article2(scrapy.Item):
    title = scrapy.Field()
    paragraph = scrapy.Field()



class articles(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link  = scrapy.Field()

class articles2(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    body = scrapy.Field()

class article2(scrapy.Item):
    title = scrapy.Field()
    paragraph = scrapy.Field()
