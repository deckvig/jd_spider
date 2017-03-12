# -*- coding: utf-8 -*-
import json
import os
import re

import scrapy
from jd_scrapy.items import Jd_commodity_info
from scrapy.utils.project import get_project_settings


class JdListSpider(scrapy.Spider):
    name = "jd_list"
    allowed_domains = ["list.jd.com", 'pm.3.cn']
    SETTING = get_project_settings()
    sub_page_link = 'http://list.jd.com/list.html?cat=%s&page=%d&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main'
    item_price_link = 'http://pm.3.cn/prices/pcpmgets?skuids=%s&origin=2'
    item_comment_link = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=%s'
    url = 'http://book.jd.com/booksort.html'
    cookies = {
        'listck': 'f24d7042ea27d536f60467e705280fa6',
        '__jda': '122270672.1489256862989305248423.1489256863.1489256863.1489256863.1'
    }

    def start_requests(self):
        return [scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies)]

    def parse(self, response):
        for cat in response.css('.mc dd a::attr(href)').re(r'\d+-\d+-\d+'):
            url = self.sub_page_link % (cat, 1)
            # if not sub_item_finish(sku):
            yield scrapy.Request(url, meta={'cat': cat}, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        pages = int(response.css('.p-skip b::text').extract_first())
        if type(pages) == type(1) or type(pages) == type('a'):
            for page in range(1, pages + 1):
                cat = response.meta['cat']
                url = self.sub_page_link % (cat, page)
                yield scrapy.Request(url, meta={'cat': cat}, cookies=self.cookies, callback=self.parse_all_item_info)

    def parse_all_item_info(self, response):
        category = response.css('.trigger .curr::text').extract()
        items = response.css('.gl-item')
        re_n7 = re.compile(r'(\/n7\/)')
        for i in items:
            item = Jd_commodity_info()
            item['cat'] = response.meta['cat']
            link = i.css('.p-name a::attr(href)')
            item['sku'] = link.re_first(r'\d+')
            item['link'] = 'http:' + link.extract_first()
            img = i.css('.p-img a img::attr(src)').extract_first()
            if not img:
                img = i.css('.p-img a img::attr(data-lazy-img)').extract_first()
            item['img'] = 'http:' + re.sub(re_n7, '/imgzone/', img)
            item['name'] = i.css('.p-name a em::text').extract_first()
            item['author'] = i.css('.p-bi-name span a::attr(title)').extract()
            item['publish'] = i.css('.p-bi-store a::attr(title)').extract_first()
            item['publish_date'] = i.css('.p-bi-date::text').re_first(r'\d{4}-\d{1,2}')
            item['shop_num'] = i.css('.curr-shop::text').extract_first()
            item['category'] = category
            url = self.item_price_link % item['sku']
            yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item_price)

    def parse_item_price(self, response):
        data = json.loads(response.body_as_unicode())[0]
        item = response.meta['item']
        item['selling_price'] = data['p']
        item['fix_price'] = data['m']
        yield item

        # def sub_item_finish(filename):
        #     if os.path.isfile(SETTING['FINISH_DIR'] + filename):
        #         return True
        #     return False
