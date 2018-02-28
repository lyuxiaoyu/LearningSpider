# -*- coding: utf-8 -*-
import scrapy
from cnblogSpider.items import CnblogspiderItem


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/']

    def parse(self, response):
        divDayList = response.xpath(r"//div[@class='day']");
        for divDay in divDayList:
            date = divDay.xpath(r"./div[@class='dayTitle'][1]/a/text()").extract()[0];
            title = divDay.xpath(r"./div[@class='postTitle'][1]/a/text()").extract()[0];
            url = divDay.xpath(r"./div[@class='postTitle'][1]/a/@href").extract()[0];
            item = CnblogspiderItem(date = date, title = title, url = url);
            yield item;

        next_page = response.xpath(r"//a[text()='下一页'][1]/@href").extract();
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse);