import pymysql

conn = pymysql.connect(host='192.168.10.108',user='root',password='123456',db='scrapy',port=3306,charset='utf8')
# conn = pymysql.Connect(host='192.168.10.108',
#                             port=3306,
#                             user='root',
#                             password='123456',
#                             db='scrapy',
#                             charset='utf8')
cursor = conn.cursor()
sql ='select title, url from banfo'
cursor.execute(sql)
result = cursor.fetchall()

for i,j in enumerate(result):
    print(i,j)