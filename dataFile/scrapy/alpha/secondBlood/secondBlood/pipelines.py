# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SecondbloodPipeline:
    fp = None

    # 重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('>>> start crawl ... ... ')
        self.fp = open('./skyeye.txt', 'w', encoding='utf8')

    #该方法接收parse提交过来的item对象数据
    #该方法每接收到一个item就被调用一次
    def process_item(self, item, spider):

        name = item['name']
        img = item['img']
        normal = item['normal']
        tag = item['tag']
        legalPerson = item['legalPerson']
        capital = item['capital']
        createTime = item['createTime']
        telephone = item['telephone']
        email = item['email']
        address = item['address']
        itemStr = name +','+img+','+normal+','+tag+','+legalPerson+','+capital+','+createTime+','+telephone+','+email+','+address+'\n'

        self.fp.write(itemStr)
        return item

    def close_spider(self,spider):
        print('>>> close spider ... ... ')
        self.fp.close()
