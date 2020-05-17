import scrapy

class BbcSpider(scrapy.Spider):
    name = 'bbc'
    start_urls = ['https://www.bbc.com/news']

    def parse(self, response):
        
        for news in response.css('a.gs-c-promo-heading'):
            url = response.urljoin(news.css('::attr(href)').extract_first())
            yield scrapy.Request(url, callback=self.parse_articles)


    def parse_articles(self, response):
        title = str(response.css('div.story-body h1::text').get())
        author = response.css('span.byline__name::text').get()
        text = ''
        for i in range(len(response.css('div.story-body__inner p::text'))):
            text += response.css('div.story-body__inner p::text')[i].get()

        yield {
            'url': response.url,
            'title': title,
            'author' : author,
            'text': text
        }