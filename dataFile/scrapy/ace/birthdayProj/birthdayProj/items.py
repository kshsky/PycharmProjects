# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BirthdayprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    birthdayUrl = scrapy.Field()
    huaUrl = scrapy.Field()
    shuUrl = scrapy.Field()
