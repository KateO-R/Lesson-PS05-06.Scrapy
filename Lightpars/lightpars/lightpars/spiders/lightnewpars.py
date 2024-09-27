import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def parse(self, response):
        lights = response.css('div.WdR1o')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.q5Uds span::text').get(),
                'url': light.css('a').attrib['href']
            }