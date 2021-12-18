import pdfkit

from bs4 import BeautifulSoup
import  pymysql
conn = None
cursor = None



print('>>> open baixiaosheng spider pipeline ...')
conn = pymysql.Connect(host='192.168.10.108',
                            port=3306,
                            user='root',
                            password='123456',
                            db='scrapy',
                            charset='utf8')

sql='select page,id,title,public,contentUrl from baixiaosheng'
cursor =conn.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for i,j in enumerate(result):
    print(i+1,j)



print(type(j))

# file_name = 'F:\PDF\python_html_to_pdf\\'+'1.pdf'
#
# # subprocess.Popen([r'D:\program\python_call_exe\wkhtmltox-0.12.4_mingw-w64-cross-win64.exe'])
# config=pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# # pdfkit.from_string(body,filename,options=options,configuration=config)
# pdfkit.from_url('http://baixiaosheng.net/8241',file_name,options=options,configuration=config)
print('ok')