import random
import re
from datetime import datetime
import time
import pdfkit

from bs4 import BeautifulSoup
import pymysql

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import os
import os.path

def validateTitle(title):

    #替换英文字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    rep_en = re.sub(rstr, "_", title)  # 替换为下划线

    #替换中文字符
    rstr2=r"[：？'‘“”]"
    result = re.sub(rstr2, "-", rep_en)  # 替换为下划线

    return result

'''
保存pdf，
参数：html_pdf_path_dict,key是html的绝对路径，key是pdf的绝对路径
'''
def persist_pdf(html_pdf_file_dict):
    print('\n\n---------------------persist----------------------------------\n\n')
    for i in html_pdf_file_dict:
        options = {
            '--title':'[title]', #展示 h1、h2、h3等各级标题作为大纲
            '--page-size':'Letter',
            '--encoding': "UTF-8",
            # '--header-left':pub,#页眉左边,
            # '--header-right':'我是右边页眉',#页眉右边，添加页码,
            '--footer-right':'[page]/[toPage]',#页脚右边，添加页码,
            # '--header-line':'--header-line', #添在页眉下方显示一条直线分隔正文
            # '--header-spacing':'5' #页眉与正文之间的距离(默认为零)
        }
        config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        print('正在生成pdf文件 ---> ', html_pdf_file_dict[i])
        start = datetime.now()

        pdfkit.from_file(i, html_pdf_file_dict[i], options=options, configuration=config)

        end =datetime.now()

        print('pdf文件生成完成，用时 {} 秒'.format(end -start))
'''
程序卡死，从本地的html列表和pdf列表 ，重新生成 html_pdf_path_dict

'''
def local_html_dict_path_dict(html_path,pdf_path):
    html_pdf_path_dict={}

    # html_path = r'F:\PDF\python_html_to_pdf\html'
    # pdf_path = r'F:\PDF\python_html_to_pdf'

    html_list = []
    for root,directory,file in os.walk(html_path):
        if root == html_path:
            html_list = file

    pdf_list = []
    for root,directory,file in os.walk(pdf_path):
        if root == pdf_path:
            pdf_list=file

    html_set = set()
    for i in html_list:
        html_set.add(i[:-4])

    pdf_set = set()
    for i in pdf_list:
        pdf_set.add(i[:-3])


    remain_html = html_set-pdf_set

    for i in remain_html:
        html_pdf_path_dict.update({os.path.join(html_path,i+'html'):os.path.join(pdf_path,i+'pdf')})

    return html_pdf_path_dict
'''
    从数据库中查询文章的url，并调取 persist_html，将文章以html的格式存储在磁盘中
    返回：html_pdf_path_dict,key是html的绝对路径，key是pdf的绝对路径
    
'''
def querySQL(root_html,root_pdf):

    conn = pymysql.Connect(host='192.168.10.108',
                            port=3306,
                            user='root',
                            password='123456',
                            db='scrapy',
                            charset='utf8')
    sql='select id,title,public,url from banfo'
    cursor =conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    ############################################
    print("初始化浏览器")
    # normal 等待整个界面加载完成（指对html和子资源的下载与解析, 如JS文件，图片等，不包括ajax）
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "normal"
    driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe',
                                   desired_capabilities=desired_capabilities)
    #################################################################
    html_pdf_path_dict={}
    for i,j in enumerate(result):
        print(i+1,j)
        if i<= 584:
            continue
        id = j[0]
        h1 = j[1]
        title = validateTitle(j[1])
        url = j[3]
        print('-----------------------html-------------------------------')
        print(datetime.now())
        time.sleep(random.randint(2, 6))
        driver.get(url)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.randint(4,6))
        driver.execute_script('window.scrollTo(0,{})'.format(0))
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,{})'.format(199))
        source = driver.page_source
        soup = BeautifulSoup(source, 'lxml')
        # print(source)
        content = soup.find(name='article')
        # print(soup.find('div','article-meta mt-4').get_text)
        public_time = soup.find('div','article-meta mt-4').find(name='span',class_=None).text
        original_tag = soup.find_all(name='span',class_='original-tag')
        #原创
        if len(original_tag)==1:
            original_tag_text =original_tag[0].text
            title = original_tag_text+'_'+title

        public = public_time[:10].replace('-','_')

        # print('----------------public_time------------------',public_time)

        body = '<h1>{}</h1>{}'.format(h1, content)
        html_path = os.path.join(root_html,public+'_'+title+'.html')
        pdf_path = os.path.join(root_pdf,public+'_'+title+'.pdf')
        html_pdf_path_dict.update({html_path:pdf_path})

        sql ='update banfo set public="{}" where id ="{}"'.format(public,id)
        print('----------------------> ',sql)
        cursor.execute(sql)
        conn.commit()

        print('正在生成html文件 ---> ',html_path)

        start = datetime.now()
        with open(html_path, 'w', encoding='UTF-8') as fp:
            fp.write(body)
        fp.close()
        end = datetime.now()
        print('html文件生成完成，用时 {} 秒'.format(end - start))

    driver.close()

    return html_pdf_path_dict



root_html = r'F:\PDF\python_html_to_pdf\banfo-html'
root_pdf= r'F:\PDF\python_html_to_pdf\banfo-pdf'
# html_pdf_path_dict = querySQL(root_html,root_pdf)
html_pdf_path_dict = local_html_dict_path_dict(root_html,root_pdf)
for i in html_pdf_path_dict:
    print(i,html_pdf_path_dict[i])

print('共需完成文件{}个'.format(len(html_pdf_path_dict)))
persist_pdf(html_pdf_path_dict)
print('--------------finished normally--------------------')
