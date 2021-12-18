# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RediscrawlprojItem(scrapy.Item):
    id = scrapy.Field()
    detailUrl = scrapy.Field()
    detailTitle = scrapy.Field()