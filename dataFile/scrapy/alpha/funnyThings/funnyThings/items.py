# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FunnythingsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名称,img,状态,标签,法定代表人：,注册资本：,成立日期：,电话：,邮箱：,地址：
    normal = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    legalPerson= scrapy.Field()
    capital = scrapy.Field()
    createTime = scrapy.Field()
    telephone = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
