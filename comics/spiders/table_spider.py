import scrapy

class TableSpider(scrapy.Spider):
    name = "table"

    def start_requests(self):
        urls = [
            "https://en.wikipedia.org/wiki/List_of_Calvin_and_Hobbes_books"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        x = response.css("table tr td:nth-child(1)").extract()
