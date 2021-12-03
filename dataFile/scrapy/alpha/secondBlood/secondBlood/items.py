# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SecondbloodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # item['name'] = name
    # item['img'] = img
    # item['normal'] = normal
    # item['tag'] = tag
    # item['legalPerson'] = legalPerson
    # item['capital'] = capital
    # item['createTime'] = createTime
    # item['telephone'] = telephone
    # item['email'] = email
    # item['address'] = address

    name = scrapy.Field()
    img = scrapy.Field()
    normal = scrapy.Field()
    tag = scrapy.Field()
    legalPerson = scrapy.Field()
    capital = scrapy.Field()
    createTime = scrapy.Field()
    telephone = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
