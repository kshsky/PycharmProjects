# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime
import pymysql


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
###########################################################################################
class BackgroundpicPipeline:

    conn = None
    cursor = None
    day = datetime.now().date()
    tableName = 'highPic_' + str(day).replace('-','_')

    def open_spider(self,spider):
        print('>>> open hihgPic spider pipeline ...')
        self.conn = pymysql.Connect(host='192.168.10.108',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db = 'scrapy',
                                    charset = 'utf8')


        columnList = ['name','small','src']

        self.cursor = self.conn.cursor()
        checkSQL = buildCheckTableSQL('scrapy', self.tableName)
        self.cursor.execute(checkSQL)
        record = self.cursor.fetchone()
        num = record[0]
        print(num)
        if num == 0 :
            createSQL = buildCreateSQL(self.tableName, columnList)
            print('\n\n create table successfully \n\n')

            self.cursor.execute(createSQL)
            self.conn.commit()

        # droSQL = buildDropSQL(self.tableName)
        # self.cursor.execute(droSQL)
        # self.conn.commit()



    def process_item(self, item, spider):
        col_data_list = []
        col_data_list.append(item['name'])
        col_data_list.append(item['small'])
        col_data_list.append(item['src'])

        insertSQL = buildInsertSQL(self.tableName, col_data_list)
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