# -*- coding: utf-8 -*-
import scrapy, csv
from scrapy.utils.project import get_project_settings

class Covid19usaSpider(scrapy.Spider):
	name = 'covid19USA'
	allowed_domains = ['www.google.com']
	rss_url_format = "https://news.google.com/rss/search?q={query}"

	settings=get_project_settings()
	base_dir = settings.get('PROJECT_ROOT')
	output_file = base_dir + '\\scrapedData\\' + name + '.csv'

	def start_requests(self):
		urls = [
			'https://news.google.com/rss/search?q=%7Bcovid+coronavirus+usa+america+lockdown+businesses+shut%7D&hl=en-IN&gl=IN&ceid=IN:en',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
 
	def parse(self, response):
		items = response.xpath('//channel/item')

		with open(self.output_file, 'a', newline="") as file:
			writer = csv.writer(file)

			for item in items:
				scraped_info = {
					'title' : item.xpath('title/text()').extract(),
					'link': item.xpath('link//text()').extract_first(),
					'pubDate' : item.xpath('pubDate//text()').extract_first(),
				}

				writer.writerow(scraped_info.values())
				yield scraped_info
