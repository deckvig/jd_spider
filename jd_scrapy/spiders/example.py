# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    url = 'https://item.m.jd.com/newComments/newCommentsDetail.json'
    formdata = {
        'wareId': '12122800',
        'offset': '1',
        'num': '10',
        'type': '0',
        'checkParam': 'LUIPPTP'

    }

    def start_requests(self):
        return [scrapy.FormRequest(url=self.url, formdata=self.formdata)]

    def parse(self, response):
        data = response.body
        yield {
            'data': data

        }
