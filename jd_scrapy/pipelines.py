# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from pymongo import MongoClient
from scrapy.utils.project import get_project_settings


class JdScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class JdItemPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        MONGODB = settings['MONGODB']
        self.server = MONGODB['SERVER']
        self.port = MONGODB['PORT']
        self.db_name = MONGODB['DB_NAME']
        self.col_name = MONGODB['COLLECTION']

    def open_spider(self, spider):
        self.mgo = MongoClient(self.server, self.port)
        self.db = self.mgo[self.db_name]

    def close_spider(self, spider):
        self.mgo.close()

    def process_item(self, item, spider):
        self.db[self.col_name].insert(dict(item))
        return item
