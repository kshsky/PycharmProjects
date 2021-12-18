

'''
    自定义工具类：

'''
from datetime import datetime
class MySQLUtils:

    '''
        检查表是否存在，存在返回 1，不存在返回 0
    '''
    def buildCheckTableSQL(self,dbName,tableName):

        checkSQL ='SELECT count(1) FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = "'+ dbName +'" AND TABLE_NAME = "'+tableName+'";'

        return checkSQL

    def buildDropSQL(self,tableName):
        droSQL = 'drop table if exists ' + tableName
        return droSQL

    def buildTruncateSQL(self,tableName):

        return 'truncate talbe '+ tableName

    def buildDeleteSQL(self,tableName):

        return 'delete * from ' +tableName


    def buildCreateSQL(self,tableName,columnNameList):

        createSQL = 'create table '+ tableName + ' ( '
        for i in columnNameList[:-1]:
            createSQL += i +' varchar(255),'
        createSQL += columnNameList[-1] + ' varchar(255)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

        return createSQL


    def buildInsertWholeRecordSQL(self,tableName, columnDataList):
        insertSQL = 'insert into ' + tableName + ' values( '

        for i in columnDataList[:-1]:
            insertSQL += '"' + i + '",'
        insertSQL += '"' + columnDataList[-1] + '")'
        return insertSQL

    def buildInsertPartRecordSQL(self,tableName,columnDataDict):
        insertSQL = 'insert into ' + tableName

        columnStr = '('
        columnDataStr = '('
        for i in columnDataDict:
            columnStr += '"' + i + '",'
            columnDataStr += '"' +columnDataDict[i] + '",'

        sql = insertSQL + columnStr[:-1] + ' ) values '+columnDataStr[:-1]+' )'
        return sql


    def buildUpdateSQL(self,tableName,updataDict,whereDict):

        sql = 'updata ' + tableName +' set '

        for i in updataDict:
            sql += i + ' = ' + updataDict[i] +' , '
        sql = sql[:-1]+' where '
        for j in whereDict:
            sql += j +' = '+updataDict[i] + ' and '

        return sql[:-5]


    def addDateToTableName(self,tableName):

        day = datetime.now().date()
        newTableName = tableName + str(day).replace('-', '_')

        return newTableName