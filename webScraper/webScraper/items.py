# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BbcArticles(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
