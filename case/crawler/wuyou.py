import random

from bs4 import BeautifulSoup
import requests
import pandas as pd



#############################################################
import pymysql
from datetime import datetime

# =============================================

'''
    检查表是否存在，存在返回 1，不存在返回 0
'''


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


# ===============================================
#打开数据库，建立连接

conn = None
cursor = None
day = datetime.now().date()
tableName = 'boss_' + str(day).replace('-', '_')
columnList=['job','jobTag','jobArea','salary','requirement','company','companyTag','jobDesc']
conn = pymysql.Connect(host='192.168.10.108',
                            port=3306,
                            user='root',
                            password='123456',
                            db='scrapy',
                            charset='utf8')



cursor = conn.cursor()
checkSQL = buildCheckTableSQL('scrapy', tableName)
cursor.execute(checkSQL)
record = cursor.fetchone()
num = record[0]
print(num)
if num == 0:
    createSQL = buildCreateSQL(tableName, columnList)
    print(createSQL)
    print('\n\n create table successfully \n\n')

    cursor.execute(createSQL)
    conn.commit()

# droSQL = buildDropSQL(self.tableName)
# self.cursor.execute(droSQL)
# self.conn.commit()



#############################################################
url='https://www.zhipin.com/c101010100-p100509/?page={}'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
         'Accept-Language': 'en',
         'Cookie':
         'lastCity=101010100; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=5103c730-3995-426a-bd63-c1b08e0ece66; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1638620726,1639551740; __l=r=https://www.baidu.com/other.php?sc.a00000jl3FL0WZ_LDXsDVfvWNG3-AAcXq3t4tFUVjm_r0E3pkHmHANTvg-0BvGIGG-ldjQHM-xcv88zxS2O45TcZa_hsdVeC6lNfz-WVNmAO3lG-t8IaOB_Jktbric3NxWiAGzZOYHORbEYDePQjMVGRwnufzLpBZcicgwzw6zrVFZ1HBKQb2ZxGSvaJOqxR-l_FNLwp9f1xBfdDJ1w1XUo3PObY.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqmhq1Tqpkko60ThPv5HD0IgF_gv-b5HDdn10vnjb3rj60UgNxpyfqnHfYP1TkPj60UNqGujYknHDdPjcYrfKVIZK_gv-b5HDznWT10ZKvgv-b5H00pywW5R9rf6KspyfqnfKWpyfqn0KWThnqn1D4P1c&dt=1639551735&wd=boss%E7%9B%B4%E8%81%98&tpl=tpl_12273_25897_22126&l=1530609888&l=/www.zhipin.com/c101010100-p100509/?page=4&ka=page-4&s=3&g=/www.zhipin.com/beijing/?sid=sem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; acw_tc=0bdd34b616395598008643134e019d4488938dd16da0c1da5237689b70e54c; __zp_stoken__=2fb1dJH8BL01xP3wnLxZWLgZ6QGt/STFeXUF9SEVaEmJgYnYjNTc4LmhWc0xUHUQ0T3t0a2RBSkQhJBYNNgl0MmMdBmUPfGQXBCksQgECbypiHDhFC00wOjsCOU4pNCt3DUJGQ2A/SE1pYQ0=; __c=1639551740; __a=35652195.1635823367.1638620725.1639551740.72.3.23.23; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1639560599; __zp_sseed__=nXtRXfo0UWBzC6imnN3MRcsYGTWxkbSvqJrm5qGUCug=; __zp_sname__=5387edf6; __zp_sts__=1639560779598'
         }
import time
for i in range(3,10):
    url = url.format(i)
    print('---{}--'.format(i))
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,'lxml')
# print(soup.prettify())


    ul_tag = soup.find(name='div',class_='job-list')

    unit_list = []

    li_tag = ul_tag.find_all('li')
    for i in li_tag:
        column_data = []
        job = i.find('a').string
        jobTag = i.find(name='div', class_='tags').get_text(separator=";", strip=True)
        jobArea = i.find(name='span', class_='job-area').string
        salary = i.find(name='span', class_='red').string
        requirement = i.find(name='p').get_text(separator=";")
        company = i.find_all(name='h3')[1].text
        companyTag = i.find_all(name='p')[1].get_text(separator=";")
        jobDesc = i.find(name='div', class_='info-desc').string

        column_data.append(checkNone(job))
        column_data.append(checkNone(jobTag))
        column_data.append(checkNone(jobArea))
        column_data.append(checkNone(salary))
        column_data.append(checkNone(requirement))
        column_data.append(checkNone(company))
        column_data.append(checkNone(companyTag))
        column_data.append(checkNone(jobDesc))
        # 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']
        sql = buildInsertWholeRecordSQL(tableName, column_data)
        print(sql)
        cursor.execute(sql)
        conn.commit()


    print('insert successfully ... ')
    a = random.choice([1,2,3,4,5])
    time.sleep(a)
cursor.close()
conn.close()
# print(li_tag[0])
#
# work = li_tag[0].find('a').string
# work_tag= li_tag[0].find(name='div',class_='tags').get_text(separator=";",strip=True)
# work_tag2= li_tag[0].find(name='div',class_='tags').text
# work_area = li_tag[0].find(name='span',class_='job-area').string
# salary= li_tag[0].find(name='span',class_='red').string
# require = li_tag[0].find(name='p').get_text(separator=";")
# company=li_tag[0].find_all(name='h3')[1].text
# company_tag=li_tag[0].find_all(name='p')[1].get_text(separator=";")
# work_desc = li_tag[0].find(name='div',class_='info-desc').string
#
# print('work:{}\nwork_tag:{}\nwork_tag2:{}\nwork_area:{}\nsalary:{}\nrequire:{}\ncompany:{}\ncompany_tag:{}\nwork_desc:{}'.
#       format(work,work_tag,work_tag2,work_area,salary,require,company,company_tag,work_desc))
#
