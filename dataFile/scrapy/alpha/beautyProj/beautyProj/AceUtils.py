

'''
    自定义工具类：

'''
class SQLUtils_MySQL:

    def buildDropSQL(self,tableName):
        droSQL = 'drop table if exists ' + tableName
        return droSQL


    def buildCreateSQL(self,tableName,columnNameList):

        createSQL = 'create table '+ tableName + ' ( '
        for i in columnNameList[:-1]:
            createSQL += i +' varchar(255),'
        createSQL += columnNameList[-1] + ' varchar(255)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

        return createSQL


    def buildInsertSQL(self,tableName, columnDataList):
        insertSQL = 'insert into ' + tableName + ' values( '

        for i in columnDataList[:-1]:
            insertSQL += '"' + i + '",'
        insertSQL += '"' + columnDataList[-1] + '")'
        return insertSQL


    def buildCheckTableSQL(self,dbName,tableName):

        checkSQL ='SELECT count(1) FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = "'+ dbName +'" AND TABLE_NAME = "'+tableName+'";'

        return checkSQL