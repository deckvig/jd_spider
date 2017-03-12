# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JdCommodityInfo(scrapy.Item):
    _id = scrapy.Field()
    cat = scrapy.Field()
    sku = scrapy.Field()
    link = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    img = scrapy.Field()
    selling_price = scrapy.Field()
    fix_price = scrapy.Field()
    publish = scrapy.Field()
    publish_date = scrapy.Field()
    shop_num = scrapy.Field()
    category = scrapy.Field()
    comment_count = scrapy.Field()
    comment_version = scrapy.Field()  # 为了得到评论的地址需要该字段
    score1count = scrapy.Field()  # 评分为1星的人数
    score2count = scrapy.Field()  # 评分为2星的人数
    score3count = scrapy.Field()  # 评分为3星的人数
    score4count = scrapy.Field()  # 评分为4星的人数
    score5count = scrapy.Field()  # 评分为5星的人数
    average_score = scrapy.Field()
    good_count = scrapy.Field()
    good_rate = scrapy.Field()
    general_count = scrapy.Field()
    general_rate = scrapy.Field()
    poor_count = scrapy.Field()
    poor_rate = scrapy.Field()
    after_count = scrapy.Field()


class BookCatItem(scrapy.Item):
    id = scrapy.Field()
    cat = scrapy.Field()
    spider = scrapy.Field()
    pages = scrapy.Field()
