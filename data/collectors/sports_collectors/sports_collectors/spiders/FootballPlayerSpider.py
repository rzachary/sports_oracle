import scrapy
import re
from scrapy.loader import ItemLoader
from sports_collectors.items import FootballPlayerItem

class FootballPlayerSpider(scrapy.Spider):
    name = "football"

    def start_requests(self):
        urls = []
        alphabets = [chr(ord('A')+i) for i in range(26)]
        start = 'https://www.pro-football-reference.com/players/{}/'

        for l in alphabets:
            urls.append(start.format(l))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        il = ItemLoader(item=FootballPlayerItem(), response=response)
        il.add_xpath('name', '//div[@id="div_players"]/p/a/text()')
        il.add_xpath('pos', '//div[@id="div_players"]/p/text()', re='\([\w]*[-\w]*\)')
        il.add_xpath('year', '//div[@id="div_players"]/p/text()', re='[\d]{4}-[\d]{4}')
        return il.load_item()
