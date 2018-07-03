import scrapy
from pj1.items import Pj1Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
class logSp(scrapy.Spider):
    name = "log"
    start_urls = ["https://weibo.com/p/1005053663171333/myfollow?ignoreg=1#place"]
    allowed_domains = ["weibo.com"]


    def parse(self, response):
        pass