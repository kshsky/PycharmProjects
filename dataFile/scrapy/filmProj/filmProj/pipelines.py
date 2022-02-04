from __future__ import absolute_import
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from datetime import datetime


def buildCheckTableSQL(dbName, tableName):

    checkSQL = 'SELECT count(1) FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = "' + dbName + '" AND TABLE_NAME = "' + tableName + '";'

    return checkSQL


def buildDropSQL(tableName):
    droSQL = 'drop table if exists ' + tableName
    return droSQL


def buildTruncateSQL(tableName):
    return 'truncate talbe ' + tableName


def buildDeleteSQL(tableName):
    return 'delete from ' + tableName


def buildCreateSQL(tableName, columnNameList):
    createSQL = 'create table ' + tableName + ' ( '
    for i in columnNameList[:-1]:
        createSQL += i + ' varchar(255),'
    createSQL += columnNameList[-1] + ' varchar(255)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

    return createSQL


def buildInsertWholeRecordSQL(tableName, columnDataList):
    insertSQL = 'insert into ' + tableName + ' values( '

    for i in columnDataList[:-1]:
        insertSQL += '"' + i + '",'
    insertSQL += '"' + columnDataList[-1] + '")'
    return insertSQL


def buildInsertPartRecordSQL(tableName, columnDataDict):
    insertSQL = 'insert into ' + tableName

    columnStr = '('
    columnDataStr = '('
    for i in columnDataDict:
        columnStr += i + ','
        columnDataStr += '"' + columnDataDict[i] + '",'

    sql = insertSQL + columnStr[:-1] + ') values ' + columnDataStr[:-1] + ' )'
    return sql


def buildUpdateSQL(tableName, updataDict, whereDict):
    sql = 'updata ' + tableName + ' set '

    for i in updataDict:
        sql += i + ' = ' + updataDict[i] + ' , '
    sql = sql[:-1] + ' where '
    for j in whereDict:
        sql += j + ' = ' + updataDict[i] + ' and '

    return sql[:-5]


def addDateToTableName(tableName):
    day = datetime.now().date()
    newTableName = tableName + str(day).replace('-', '_')

    return newTableName
class FilmprojPipeline:


#########################################################################################

    tableName = 'tj91'
    columnNameList = ['name','url','section','detailName','actor','designation','language','type','detailUrl']
# {'actor': '波多野结衣',
#  'designation': '番号：HZGD-018',
#  'detailName': 'HZGD-018 在儿子面前被干的新妻 波多野结衣',
#  'detailUrl': '/N/76099.html',
#  'language': '语言：中文字幕',
#  'name': 'HZGD-018 在儿子面前被干的新妻 波多野结衣',
#  'section': '字幕二',
#  'type': '类型：骑兵\r\n'
#          ' 中出\xa0\xa0人妻\xa0\xa0强奸\xa0\xa0凌辱\xa0\xa0熟女\xa0\xa0中文字幕\xa0\xa0',
#  'url': 'https://www.xuan131.top/N/76099.html'}

    def open_spider(self,spider):
        print('>>> open mysql spider pipeline ...')

        self.conn = pymysql.Connect(host='192.168.10.108',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db = 'scrapy',
                                    charset = 'utf8')


        self.cursor = self.conn.cursor()

        checkSQL = buildCheckTableSQL('scrapy', self.tableName)
        self.cursor.execute(checkSQL)
        num = self.cursor.fetchone()[0]

        if num== 1:
            deleteSQL = buildDeleteSQL(self.tableName)
            self.cursor.execute(deleteSQL)
        if num == 0:
            createSQL  = buildCreateSQL(self.tableName,self.columnNameList)
            self.cursor.execute(createSQL)
            print('create table ok ...')
    def process_item(self, item, spider):
        # print(item)
        col_data_list = []
        for i in self.columnNameList:
            col_data_list.append(item[i])
        sql = buildInsertWholeRecordSQL(self.tableName,col_data_list)
        # print(sql)
        self.cursor.execute(sql)
        self.conn.commit()



    def close_spider(self, spider):
        print('>>> close spider ... ... ')
        self.cursor.close()
        self.conn.close()

