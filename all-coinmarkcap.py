# -*- coding: utf-8 -*-
import scrapy

class coin_item(scrapy.Item):
    coin_url = scrapy.Field()
    coin_name = scrapy.Field()
    coin_code = scrapy.Field()
    coin_markcap = scrapy.Field()
    coin_price = scrapy.Field()
    coin_volume24 = scrapy.Field()


class Spider(scrapy.Spider):
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
		item["coin_url"] = coin.css('td span.currency-symbol a::attr(href)').extract(),
		item["coin_name"] = coin.css('td a.currency-name-container::text').extract(),
		item["coin_code"] = coin.css('td span.currency-symbol a::text').extract(),
		item["coin_markcap"] = coin.css('td.market-cap::attr(data-usd)').extract(),
		item["coin_price"] = coin.css('td a.price::attr(data-usd)').extract(),
		item["coin_volume24"] = coin.css('td.circulating-supply a::attr(data-supply)').extract(),


		yield item
