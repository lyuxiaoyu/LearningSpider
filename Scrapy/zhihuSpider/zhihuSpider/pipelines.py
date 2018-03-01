# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import pymongo

class ZhihuspiderPipeline(object):

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017);
        self.db = self.client['zhihu'];   # 类似dict，若不存在，则新建；
        collectionName = 'zhihu'+time.strftime('%y%m%d%H%M%S',time.localtime(time.time()))
        self.collection = self.db[collectionName];   # 若不存在，则新建；
        
    def close_spider(self, spider):
        self.client.close();

    def process_item(self, item, spider):
        print("\nuser id: ", item.get('id'));
        self.collection.insert(dict(item));
        

