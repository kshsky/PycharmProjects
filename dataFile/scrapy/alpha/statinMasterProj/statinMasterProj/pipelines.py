# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# useful for handling different item types with a single interface
import scrapy
import pymysql
from datetime import datetime

# =============================================

def buildDropSQL(tableName):
    droSQL = 'drop table if exists ' + tableName
    return droSQL


def buildCreateSQL(tableName, columnNameList):
    createSQL = 'create table ' + tableName + ' ( '
    for i in columnNameList[:-1]:
        createSQL += i + ' varchar(255),'
    createSQL += columnNameList[-1] + ' varchar(255)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

    return createSQL


def buildInsertSQL(tableName, columnDataList):
    insertSQL = 'insert into ' + tableName + ' values( '

    for i in columnDataList[:-1]:
        insertSQL += '"' + i + '",'
    insertSQL += '"' + columnDataList[-1] + '")'
    return insertSQL


def buildCheckTableSQL(dbName, tableName):

    checkSQL = 'SELECT count(1) FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = "' + dbName + '" AND TABLE_NAME = "' + tableName + '";'

    return checkSQL
# ===============================================
class StatinmasterprojPipeline:
    conn = None
    cursor = None
    day = datetime.now().date()
    tableName = 'stationMaster_' + str(day).replace('-', '_')
    columnList = ['name', 'avatar', 'midSrc', 'imgSrc']
    def open_spider(self, spider):
        print('>>> open gorge spider pipeline ...')
        self.conn = pymysql.Connect(host='192.168.10.108',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db='scrapy',
                                    charset='utf8')



        self.cursor = self.conn.cursor()
        checkSQL = buildCheckTableSQL('scrapy', self.tableName)
        self.cursor.execute(checkSQL)
        record = self.cursor.fetchone()
        num = record[0]
        print(num)
        if num == 0:
            createSQL = buildCreateSQL(self.tableName, self.columnList)
            print('\n\n create table successfully \n\n')

            self.cursor.execute(createSQL)
            self.conn.commit()

        # droSQL = buildDropSQL(self.tableName)
        # self.cursor.execute(droSQL)
        # self.conn.commit()

    def process_item(self, item, spider):
        col_data_list = []
        for i in self.columnList:
            col_data_list.append(item[i])

        insertSQL = buildInsertSQL(self.tableName, col_data_list)
        print(insertSQL)

        try:
            self.cursor.execute(insertSQL)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        print('>>> close spider ... ... ')
        self.cursor.close()
        self.conn.close()
###################################################################
from scrapy.pipelines.images import ImagesPipeline
import hashlib
from scrapy.utils.python import to_bytes
class ImagesPipeline(ImagesPipeline):

    item = None
    #重写父类的三个方法

    # 1、获取url
    # def get_media_requests(self, item, info):
    #     urls = ItemAdapter(item).get(self.images_urls_field, [])
    #     return [Request(u) for u in urls]
    def get_media_requests(self, item, info):
        self.item = item
        yield scrapy.Request(item['imgSrc'])


    # def file_path(self, request, response=None, info=None, *, item=None):
    #     image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
    #     return f'full/{image_guid}.jpg'
    # 存储路径： IMAGES_STORE = './imgs'
    # 2、给图片名命
    def file_path(self, request, response=None, info=None,item=item):
        #给图片名命
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        name = item['name']
        return '{}.jpg'.format(name)

    #3、把item传递给下一个管道类
    # def item_completed(self, results, item, info):
    #       with suppress(KeyError):
    #           ItemAdapter(item)[self.images_result_field] = [x for ok, x in results if ok]
    #       return item

    def item_completed(self, results, item, info):
        return item