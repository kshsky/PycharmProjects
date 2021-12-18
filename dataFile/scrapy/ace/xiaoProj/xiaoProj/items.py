# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()
    page = scrapy.Field()
    public = scrapy.Field()
    contentUrl = scrapy.Field()

