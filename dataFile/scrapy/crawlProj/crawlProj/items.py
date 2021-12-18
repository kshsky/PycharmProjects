# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlprojItem(scrapy.Item):

    id = scrapy.Field()
    detailUrl = scrapy.Field()
    detailTitle = scrapy.Field()


class CrawlprojDetailItem(scrapy.Item):
    num = scrapy.Field()
    detailTitle = scrapy.Field()
    detailContent = scrapy.Field()


