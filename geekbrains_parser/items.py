# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class BrainItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    description = scrapy.Field()
    logo = scrapy.Field()
    teachers = scrapy.Field()


class BrainsItemLoader(ItemLoader):
    pass
