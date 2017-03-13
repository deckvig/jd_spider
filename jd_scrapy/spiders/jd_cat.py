# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from jd_scrapy.items import BookCatItem


class JdCatSpider(CrawlSpider):
    name = 'jd_cat'
    allowed_domains = ['book.jd.com','list.jd.com']
    start_urls = ['http://book.jd.com/booksort.html']
    sub_page_link = 'http://list.jd.com/list.html?cat=%s&page=%d&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main'

    def parse(self, response):
        for cat in response.css('.mc dd a::attr(href)').re(r'\d+-\d+-\d+'):
            cat = cat.replace('-', ',')
            url = self.sub_page_link % (cat, 1)
            yield scrapy.Request(url, meta={'cat': cat}, callback=self.parse_sub_pages)

    def parse_sub_pages(self, response):
        pages = response.css('.fp-text i::text').extract_first()
        if pages != '0':
            item = BookCatItem()
            item['cat'] = response.meta['cat']
            item['spider'] = False
            item['pages'] = int(pages)
            yield item
