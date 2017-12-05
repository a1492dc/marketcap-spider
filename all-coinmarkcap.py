# -*- coding: utf-8 -*-
import scrapy

class coin_item(scrapy.Item):
    coin_url = scrapy.Field()
    coin_name = scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = "all-coinmarkcap"

    def start_requests(self):
        urls = [
            'https://coinmarketcap.com/all/views/all/',
        ]
        for url in urls:
		yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = []
	for coin in response.css("table#currencies-all tr"):
		item = coin_item()
		item["coin_name"] = coin.css("td span.currencies-symbol a::text").extract_first(),
		item["coin_url"] = coin.css("td span.currency-symbol a::attr(href)").extract(),
		yield item
