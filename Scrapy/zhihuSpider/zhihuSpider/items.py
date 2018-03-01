# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import *

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


def TakeSecond(v):
    if len(v) >= 2:
        return v[1];
    else:
        return None;

class ZhihuItemLoader(ItemLoader):
    default_output_processor = TakeFirst();

    followingNum_in = Compose(TakeFirst(), lambda x: int(x));

    followersNum_in = Compose(TakeSecond, lambda x: int(x));

    likeNum_in = MapCompose(lambda x: x.strip(','), lambda x: int(x[0]));