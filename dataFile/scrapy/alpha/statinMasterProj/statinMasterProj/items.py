# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StatinmasterprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()
    imgSrc = scrapy.Field()
    midSrc = scrapy.Field()