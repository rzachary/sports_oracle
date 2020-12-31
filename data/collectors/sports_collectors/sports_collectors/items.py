# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FootballPlayerItem(Item):
    name = Field()
    pos = Field()
    year = Field()

class BaseballPlayerItem(Item):
    name = Field()
    pos = Field()
    year = Field()

class BasketballPlayerItem(Item):
    name = Field()
    pos = Field()
    year = Field()

class SportsCollectorsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
