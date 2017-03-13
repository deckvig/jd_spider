# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy.utils.project import get_project_settings
from selenium import webdriver

from jd_scrapy.items import JdCommodityInfo


class JdListSpider(scrapy.Spider):
    name = "jd_list"
    allowed_domains = ["list.jd.com", 'p.3.cn']
    SETTING = get_project_settings()
    sub_page_link = 'http://list.jd.com/list.html?cat=%s&page=%d&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main'
    item_price_link = 'http://p.3.cn/prices/mgets?skuIds==%s&pduid=%s'
    # item_comment_link = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=%s'
    url = 'http://book.jd.com/booksort.html'
    cookies = {
        'listck': '407d46c070524314b37f39277fd821dd',
        '__jda': '122270672.1489374677544638146764.1489374678.1489374678.1489374678.1'
    }

    def start_requests(self):
        return [scrapy.Request(url=self.url, callback=self.parse, cookies=self.cookies)]

    def parse(self, response):
        for cat in response.css('.mc dd a::attr(href)').re(r'\d+-\d+-\d+'):
            cat = cat.replace('-', ',')
            url = self.sub_page_link % (cat, 1)
            yield scrapy.Request(url, meta={'cat': cat}, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        pages = response.css('.fp-text i::text').extract_first()
        if pages != '0':
            if pages != '1':
                cookies = self.get_cookie(response.url)
            else:
                cookies = {
                    'listck': '8c1e86ef59a6dc5e6afc7c2144a7dfa3',
                    '__jda': '122270672.1489342825883952871218.1489342826.1489342826.1489342826.1'
                }
            for page in range(1, int(pages) + 1):
                cat = response.meta['cat']
                url = self.sub_page_link % (cat, page)
                meta = response.meta
                meta['cookie_jar'] = 1
                meta['uuid'] = cookies['__jda'].split('.')[1]

                yield scrapy.Request(url, meta=meta, cookies=cookies, callback=self.parse_all_item_info)

    def parse_all_item_info(self, response):

        category = response.css('.trigger .curr::text').extract()
        items = response.css('.gl-item')
        uuid = response.meta['uuid']
        re_n7 = re.compile(r'(\/n7\/)')
        sku = []
        itemss = {}
        count = 0
        for i in items:
            item = JdCommodityInfo()
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
            key = 'J_%s' % item['sku']
            itemss[key] = item
            sku.append(key)
            count += 1
            if count == 30:
                url = self.item_price_link % ('%2C'.join(sku), uuid)
                yield scrapy.Request(url, meta={'items': itemss}, callback=self.parse_item_price)
                # print('parse_all_item_info',itemss)
                itemss = {}
                sku = []
                count = 0
        if len(sku):
            url = self.item_price_link % ('%2C'.join(sku), uuid)
            # print('parse_all_item_info',itemss)
            yield scrapy.Request(url, meta={'items': itemss}, callback=self.parse_item_price)

    def get_prices(self, sku, itemss):
        url = self.item_price_link % '%2C'.join(sku)
        yield scrapy.Request(url, meta={'items': itemss}, callback=self.parse_item_price)

    def parse_item_price(self, response):
        data = json.loads(response.body_as_unicode())
        items = response.meta['items']
        # print('parse_item_price',items)
        for (key, item) in items.items():
            # print('111111111111111111111111111111111111111111111111111111111111', key, item)
            for price in data:
                if key == price['id']:
                    item['selling_price'] = price['p']
                    item['fix_price'] = price['m']
                    yield item

    def get_cookie(self, url):
        service_args = []
        service_args.append('--load-images=no')
        service_args.append('--disk-cache=yes')
        service_args.append('--ignore-ssl-errors=true')
        browser = webdriver.PhantomJS('/usr/local/bin/phantomjs', service_args=service_args)

        browser.get(url)
        elem = browser.find_element_by_class_name('pn-next')
        elem.click()
        jda = browser.get_cookie('__jda')
        listck = browser.get_cookie('listck')
        cookies = {'__jda': jda['value'], 'listck': listck['value']}
        # print("打印Cookies:", self.cookies)
        browser.close()
        return cookies
