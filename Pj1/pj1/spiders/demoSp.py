import scrapy
from pj1.items import Pj1Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
class demoSp(scrapy.Spider):
    name = "demo"
    start_urls = ["https://www.qidian.com/rank/yuepiao"]
    allowed_domains = ["qidian.com"]


    def parse(self, response):
        l = ItemLoader(item=Pj1Item(),response=response)
        l.add_xpath('name',"//*[@data-eid='qd_C40']//text()")
        l.add_xpath('author',"//*[@data-eid='qd_C41']//text()")
        a=response.xpath("//*[@class='book-mid-info']//*[@class='intro']//text()").extract()
        c = []
        for i in a:
            d = MapCompose(str.strip)(i)
            c.append(d)
        l.add_value('info',c)
        print("=====================================")
        '''
        item['info'] = response.xpath("//*[@class='book-mid-info']//*[@class='intro']//text()").extract()
        item['author'] = response.xpath("//*[@data-eid='qd_C41']//text()").extract()
        item['name'] = response.xpath("//*[@data-eid='qd_C40']//text()").extract()
        '''
        print("=====================================")
        return l.load_item()
