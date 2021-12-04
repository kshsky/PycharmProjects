# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from datetime import datetime
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


def createInsertSQL(tableName, columnDataList):

    insertSQL = 'insert into ' + tableName + ' values( '

    for i in columnDataList[:-1]:
        insertSQL += '"' + i + '",'
    insertSQL += '"'+columnDataList[-1] + '")'
    return insertSQL

class SecondbloodPipeline:
    fp = None

    # 重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('>>> start crawl ... ... ')
        #文件保存在spider文件夹里
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
        #传递给下一个管道类
        return item

    def close_spider(self,spider):
        print('>>> close spider ... ... ')
        self.fp.close()

class mysqlPipeline:
    conn = None
    cursor = None
    day = datetime.now().date()
    tableName = 'spider_' + str(day).replace('-','_')

    def open_spider(self,spider):
        print('>>> open mysql spider pipeline ...')
        self.conn = pymysql.Connect(host='192.168.10.108',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db = 'scrapy',
                                    charset = 'utf8')


        self.cursor = self.conn.cursor()

        droSQL = 'drop table if exists ' + self.tableName
        # DROP TABLE IF EXISTS `user`;
        print(droSQL)
        self.cursor.execute(droSQL)
        self.conn.commit()

        createSQL = 'create table ' + self.tableName + ' (name varchar(100),img varchar(200),normal varchar(10),tag varchar(100),legalPerson varchar(100),capital varchar(100), createTime varchar(20),telephone varchar(30),email varchar(30),address varchar(100)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
        print(createSQL)
        self.cursor.execute(createSQL)
        self.conn.commit()


    def process_item(self,item,spider):
        # name = item['name']
        # img = item['img']
        # normal = item['normal']
        # tag = item['tag']
        # legalPerson = item['legalPerson']
        # capital = item['capital']
        # createTime = item['createTime']
        # telephone = item['telephone']
        # email = item['email']
        # address = item['address']
        # itemStr = name +','+img+','+normal+','+tag+','+legalPerson+','+capital+','+createTime+','+telephone+','+email+','+address+'\n'
        # # insertSQL ='insert into ' + self.tableName+' values("'+name +'","'+img+'","'+normal+'","'+tag+'","'+legalPerson+'","'+capital+'","'+createTime+'","'+telephone+'","'+email+'","'+address+'")'
        # #调用方法拼接insert的sql语句
        # listData = [name,img,normal,tag,legalPerson,capital,createTime,telephone,email,address]

        # 优化
        columnDataList = []
        columnDataList.append(item['name'])
        columnDataList.append(item['img'])
        columnDataList.append(item['normal'])

        columnDataList.append(item['tag'])
        columnDataList.append(item['legalPerson'])
        columnDataList.append(item['capital'])

        columnDataList.append(item['createTime'])
        columnDataList.append(item['telephone'])
        columnDataList.append(item['email'])

        columnDataList.append(item['address'])

        insertSQL=createInsertSQL(self.tableName,columnDataList)
        print(insertSQL)
        try:
            self.cursor.execute(insertSQL)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self,spider):
        print('>>> close spider ... ... ')
        self.cursor.close()
        self.conn.close()

