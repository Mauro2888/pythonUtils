import scrapy
from bs4 import BeautifulSoup

class HeadphonesSpider(scrapy.Spider):

    name = "prova"

    def start_requests(self):
        urls = [
        'https://sito1.it',
        'https://sito2.it'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body_urls = response.css('body').extract()     
        new_body = str(body_urls)
        soup = BeautifulSoup(new_body, 'html.parser')
        just_text = soup.get_text()
        just_text= just_text.replace('\\n',' ')
        
        with open('urls.csv', 'w') as f:
            for u in body_urls:
          
