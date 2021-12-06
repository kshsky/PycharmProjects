# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sectionName = scrapy.Field()
    sectionUrl = scrapy.Field()
    infoTitle = scrapy.Field()
    infoDetailUrl = scrapy.Field()
    infoDetailContent = scrapy.Field()