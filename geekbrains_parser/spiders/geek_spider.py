from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from geekbrains_parser.items import BrainsItemLoader, BrainItem


class GeekSpider(CrawlSpider):
    name = 'geek_spider'

    start_url = ['https://gb.ru/geek_university/']
    allowed_domains = ['gb.ru']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//*[@id="prof-compact"]/div/div[1]/div[2]/div[2]'],
                allow=r'https://gb.ru/\w+/\w+$'
            ),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = BrainsItemLoader(BrainItem(), selector)
