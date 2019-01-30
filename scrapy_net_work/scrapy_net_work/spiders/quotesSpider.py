from scrapy import Spider, Request

class QuotesSpider(Spider):
    name = 'quotes'
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for _url in urls:
            yield Request(url=_url, callback=self.parse)

    def parse(self, response):
        for _quote in response.css('div.quote'):
            yield {
                'content': _quote.css('span.text::text').extract_first(),
                'author': _quote.css('small.author::text').extract_first(),
                'tags': _quote.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)