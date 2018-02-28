# -*- coding: utf-8 -*-
import scrapy
import json


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']

    # 未定义 start_urls 使用 start_requests 函数启动
    def start_requests(self):
    
        startUrl = 'https://www.zhihu.com/people/wan-shang-lin/';
        startCookies = {};
        try:
            with open('./result/zhihuCookies.json', 'r') as fr:
                cookiesList = json.load(fr);
                for c in cookiesList:
                    startCookies[c['name']] = c['value'];
        except:
            pass    # 如果没有正确得到cookies,可利用

        # 返回request列表
        return [scrapy.Request(startUrl, cookies = startCookies, callback = self.parseInfo), ];

    def parseInfo(self, response):
        response.xpath(r'//span[@class="ProfileHeader-name"]')
        response.xpath(r'//span[@class="RichText ProfileHeader-headline"]')

    def parseRelation(self, response):
        pass

    def parse(self, response):
        pass
