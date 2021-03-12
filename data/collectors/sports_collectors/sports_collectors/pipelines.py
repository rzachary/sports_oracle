# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import pymongo
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter

class FootballPlayerPipeline:
	player_type = 'Football'

	def open_spider(self, spider):
		self.file = open('football_players.jl', 'w')

	def close_spider(self, spider):
		self.file.close()

	def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)

	def process_item(self, item, spider):
		exporter = self._exporter_for_item(item)
		line = json.dumps(ItemAdapter(item).asdict()) + "\n"
		self.file.write(line)
		return item

class BaseballPlayerPipeline:
	player_type = 'Baseball'

    def open_spider(self, spider):
        self.file = open('baseball_players.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)


class BasketballPlayerPipeline:
	player_type = 'Baseketball'

    def open_spider(self, spider):
        self.file = open('basketball_players.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)


class SportsCollectorsPipeline:
    def process_item(self, item, spider):
        return item
