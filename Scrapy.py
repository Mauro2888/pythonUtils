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
                
from bs4 import BeautifulSoup as bs
import requests


url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2."
request_call = requests.get(url)
content = bs(request_call.text, "html.parser")
titolo = content.findAll("div", {"class": "_3wU53n"})
prezzo = content.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
prezzo_precedente = content.findAll("div", {"class": "_3auQ3N _2GcJzG"})

for tit in titolo:
    for prz in prezzo:
        for prz_prc in prezzo_precedente:
            print(tit.text + " " + prz.text + " " + prz_prc.text)

          
