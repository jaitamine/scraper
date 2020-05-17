import scrapy
from ..items import BbcArticles

class BbcSpider(scrapy.Spider):

    name = 'bbc'
    start_urls = ['https://www.bbc.com/news']

    def parse(self, response): 
       
        for news in response.css('a.gs-c-promo-heading'):
            url = response.urljoin(news.css('::attr(href)').extract_first())
            yield scrapy.Request(url, callback=self.parse_articles)


    def parse_articles(self, response):
        
        items = BbcArticles()
        title = str(response.css('div.story-body h1::text').get())
        author = response.css('span.byline__name::text').get()
        text = ''

        for i in range(len(response.css('div.story-body__inner p::text'))):
            text += response.css('div.story-body__inner p::text')[i].get()

        items['url'] = response.url
        items['title'] = title
        items['author'] = author
        items['text'] = text
               
        if len(text) < 100:
            pass
        else:
            yield(items)