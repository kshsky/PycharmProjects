# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#一张表分为两部分插入
class FilmItem(scrapy.Item):
    columnNameList = ['name', 'url', 'section', 'detailName', 'actor', 'designation', 'language', 'type', 'detailUrl']
    name = scrapy.Field()
    url = scrapy.Field()
    section = scrapy.Field()
    detailName = scrapy.Field()
    actor = scrapy.Field()
    designation = scrapy.Field()
    language = scrapy.Field()
    type = scrapy.Field()
    detailUrl = scrapy.Field()




