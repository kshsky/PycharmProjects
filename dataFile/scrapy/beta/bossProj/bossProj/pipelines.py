# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from datetime import datetime
# =============================================

def buildCheckTableSQL(dbName, tableName):
    checkSQL = 'SELECT count(1) FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = "' + dbName + '" AND TABLE_NAME = "' + tableName + '";'

    return checkSQL


def buildDropSQL(tableName):
    droSQL = 'drop table if exists ' + tableName
    return droSQL


def buildTruncateSQL(tableName):
    return 'truncate talbe ' + tableName


def buildDeleteSQL(tableName):
    return 'delete * from ' + tableName


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
        columnStr += '"' + i + '",'
        columnDataStr += '"' + columnDataDict[i] + '",'

    sql = insertSQL +  columnStr[:-1] + ' ) values ' + columnDataStr[:-1] + ' )'
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
def checkNone(target):
    if target is None:
        return '-'
    return target

class BossprojPipeline:

    conn = None
    cursor = None
    # day = datetime.now().date()
    # tableName = 'boss_' + str(day).replace('-', '_')
    # columnList = ['job', 'jobTag', 'jobArea', 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']

    def open_spider(self, spider):
        print('>>> open spider pipeline ...')
        self.conn = pymysql.Connect(host='192.168.10.108',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db='scrapy',
                                    charset='utf8')
        tableName = spider.tableName
        columnList = spider.columnList

        self.cursor = self.conn.cursor()
        checkSQL = buildCheckTableSQL('scrapy', tableName)
        self.cursor.execute(checkSQL)
        record = self.cursor.fetchone()
        num = record[0]
        print(num)
        if num == 0:
            createSQL = buildCreateSQL(tableName,columnList)
            print('\n\n create table successfully \n\n')

            self.cursor.execute(createSQL)
            self.conn.commit()

    def process_item(self, item, spider):
        # 从spider中获取表名和字段名列表
        tableName=spider.tableName
        columnList = spider.columnList

        #存入数据库
        # columnList = ['job', 'jobTag', 'jobArea', 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']
        columnDataList =[]
        for i in columnList:
            columnDataList.append(item[i])

        sql = buildInsertWholeRecordSQL(tableName,columnDataList)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        # 在pipeline中的item是需要return的
        return item

    def close_spider(self, spider):
        print('>>> close spider ... ... ')
        self.cursor.close()
        self.conn.close()