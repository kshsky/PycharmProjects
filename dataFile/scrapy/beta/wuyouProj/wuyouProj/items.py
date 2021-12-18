# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WuyouprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()
    releaseDate = scrapy.Field()
    salary = scrapy.Field()

    info = scrapy.Field()
    company = scrapy.Field()
    companyType = scrapy.Field()
    #
    # columnlist = ['job', 'release', 'salary', 'jobArea', 'experience', 'edu', 'num', 'company', 'companyType', ]

