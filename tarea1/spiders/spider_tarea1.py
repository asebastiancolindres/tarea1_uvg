# -*- coding: utf-8 -*-
import scrapy

from tarea1.items import articles2, article2

class SpiderTarea1Spider(scrapy.Spider):
    name = 'spider_tarea1'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    max_links = 25


    custom_settings={
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'file:C://Users//Sebas//Documents//Maestria//data_acquisition//Tareas///tarea1/link_wiki-%(time)s.json'
    }

    def parse(self, response):
        host = self.allowed_domains[0]
        c=0
        for link in response.css(".featured_article_metadata > a"):

            title = link.attrib.get("title")
            link= f"https://{host}{link.attrib.get('href')}"
            
            
            c=c+1
            if c > self.max_links:
                break

            yield response.follow(link,callback=self.parse_detail, meta={'link' : link,'title':title})
            

    def parse_detail(self,response):
        items = articles2()
        item = article2()

        items["link"] = response.meta["link"]
        item["title"] = response.meta["title"]
        item["paragraph"] = list()

        for text in response.xpath('//*[@id="mw-content-text"]/div/p[2]').xpath('string()').extract():
            item["paragraph"].append(text)
        
        items["body"] = item
        return items


