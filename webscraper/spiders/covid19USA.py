# -*- coding: utf-8 -*-
import scrapy


class Covid19usaSpider(scrapy.Spider):
    name = 'covid19USA'
    allowed_domains = ['www.google.com']
    start_urls = ['https://news.google.com/rss/search?q={query}']

    def parse(self, response):
        pass
