import datetime
import re

import pymysql


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

def validateTitle(title):

    #替换英文字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    rep_en = re.sub(rstr, "_", title)  # 替换为下划线

    #替换中文字符
    rstr2=r"[：？'‘“”]"
    result = re.sub(rstr2, "-", rep_en)  # 替换为下划线

    return result
class BirthdayprojPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        print('>>> open birthday spider pipeline ...')
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
            createSQL = buildCreateSQL(tableName, columnList)
            print('\n\n create table successfully \n\n')

            self.cursor.execute(createSQL)
            self.conn.commit()

    def process_item(self, item, spider):

        tableName = spider.tableName
        columnList = spider.columnList

        columnDataList = []
        for i in columnList:
            columnDataList.append(item[i])
        sql = buildInsertWholeRecordSQL(tableName,columnDataList)
        self.cursor.execute(sql)
        self.conn.commit()

        return item
