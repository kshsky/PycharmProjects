# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # columnList = ['job', 'jobTag', 'jobArea', 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']
    job = scrapy.Field()
    jobTag = scrapy.Field()
    jobArea = scrapy.Field()
    salary = scrapy.Field()
    requirement = scrapy.Field()
    company = scrapy.Field()
    companyTag = scrapy.Field()
    jobDesc = scrapy.Field()
