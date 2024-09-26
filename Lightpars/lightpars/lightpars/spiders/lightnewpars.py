import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def parse(self, response):
        pass
