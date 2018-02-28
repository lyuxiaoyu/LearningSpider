# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhihuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    name = scrapy.Field()
    headline = scrapy.Field()

    field = scrapy.Field()
    company = scrapy.Field()
    position = scrapy.Field()

    education = scrapy.Field()

    gender = scrapy.Field()

    followingNum = scrapy.Field()
    followersNum = scrapy.Field()

    likeNum = scrapy.Field()

