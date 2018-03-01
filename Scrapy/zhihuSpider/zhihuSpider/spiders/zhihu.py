# -*- coding: utf-8 -*-
import scrapy
import json
import re 

from zhihuSpider.items import *


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']

    # 未定义 start_urls 使用 start_requests 函数启动
    def start_requests(self):

        self.idPattern = re.compile(r'people/([a-zA-Z0-9\-]+)');
    
        startUrl = 'https://www.zhihu.com/people/zhan-kuang-2';
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

        l = ZhihuItemLoader(item=ZhihuspiderItem(), response = response);

        id = self.idPattern.search(response.url).group(1);
        l.add_value('id', id);
        l.add_xpath('name', r'//span[@class="ProfileHeader-name"]/text()');
        l.add_xpath('headline', r'//span[@class="RichText ProfileHeader-headline"]/text()');

        l.add_xpath('field', r'//svg[@class="Icon Icon--company"]/../../text()[1]');
        l.add_xpath('company', r'//svg[@class="Icon Icon--company"]/../../text()[2]');
        l.add_xpath('position', r'//svg[@class="Icon Icon--company"]/../../text()[3]');

        l.add_xpath('education', r'//svg[@class="Icon Icon--education"]/../../text()[1]');

        l.add_xpath('gender', r'//svg[@class="Icon Icon--male" or @class="Icon Icon--female"]/@class');

        realationNum = response.xpath(r'//strong[@class="NumberBoard-itemValue"]/@title').extract();
        l.add_value('followingNum', realationNum);
        l.add_value('followersNum', realationNum);

        l.add_xpath('likeNum', r'//svg[@class="Icon IconGraf-icon Icon--like"]/../../text()[2]');
        yield l.load_item();

        if len(realationNum) >= 2:
            if int(realationNum[0]) > 1:
                followingUrl = 'https://www.zhihu.com/people/' + id + '/following?page=1';
                yield scrapy.Request(followingUrl, meta = {'page': 1, 'relation': 'following', 'id': id}, callback = self.parseRelation) 

            if int(realationNum[1]) > 0:
                followersUrl = 'https://www.zhihu.com/people/' + id + '/followers?page=1';
                yield scrapy.Request(followersUrl, meta = {'page': 1, 'relation': 'followers', 'id': id}, callback = self.parseRelation)    
     

    def parseRelation(self, response):
        urls = response.css('a.UserLink-link').xpath(r'./@href').extract();

        # print(urls);
        for url in urls:
            yield scrapy.Request('https:'+url, callback = self.parseInfo);

        if urls and response.css('button.PaginationButton-next'):
            response.meta['page'] = response.meta['page'] + 1;
            nextPage = 'https://www.zhihu.com/people/' + response.meta['id'] + '/' + response.meta['relation'] +'?page='+ str(response.meta['page']);
            yield scrapy.Request(nextPage, meta = response.meta, callback = self.parseRelation) 

    def parse(self, response):
        pass
