import pymysql
from itemadapter import ItemAdapter
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



class WuyouprojPipeline:
    conn = None
    cursor = None
    day = datetime.now().date()
    tableName = 'wuyou_' + str(day).replace('-', '_')
    # columnList = ['job', 'jobTag', 'jobArea', 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']
    columnList = ['job', 'releaseDate', 'salary', 'info', 'company', 'companyType']
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

    def process_item(self, item, spider):
        # 存入数据库
        # columnList = ['job', 'jobTag', 'jobArea', 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']
        columnDataList = []
        # columnlist = ['job', 'releaseDate', 'salary', 'jobArea', 'experience', 'edu', 'num', 'company', 'companyType']
        columnDataList.append(checkNone(item['job']))
        columnDataList.append(checkNone(item['releaseDate']))
        columnDataList.append(checkNone(item['salary']))
        columnDataList.append(checkNone(item['info']))
        columnDataList.append(checkNone(item['company']))
        columnDataList.append(checkNone(item['companyType']))
        sql = buildInsertWholeRecordSQL(self.tableName, columnDataList)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        print('>>> close spider ... ... ')
        self.cursor.close()
        self.conn.close()