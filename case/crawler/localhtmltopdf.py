import re
from datetime import datetime

import pdfkit

from bs4 import BeautifulSoup
import  pymysql

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def validateTitle(title):

    #替换英文字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    rep_en = re.sub(rstr, "_", title)  # 替换为下划线

    #替换中文字符
    rstr2=r"[：？'‘“”]"
    result = re.sub(rstr2, "-", rep_en)  # 替换为下划线

    return result


def persist_pdf(html_pdf_file_dict):
    print('\n\n---------------------persist----------------------------------\n\n')
    for i in html_pdf_file_dict:

        #option 是匹配 html标签的内容的
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
        # pdfkit.from_string(body, file_name, options=options, configuration=config)

        pdfkit.from_file(i, html_pdf_file_dict[i], options=options, configuration=config)

        end =datetime.now()

        print('pdf文件生成完成，用时 {} 秒'.format(end -start))

import os
import os.path
def local_html_dict_path_dict(html_path,pdf_path):

    # html_path = r'F:\PDF\python_html_to_pdf\html'
    # pdf_path = r'F:\PDF\python_html_to_pdf'
    html_set=set()
    for root,directory,file in os.walk(html_path):
        for i in file:
            html_set.add(i)

    pdf_set=set()
    for root,directory,file in os.walk(pdf_path):
        for i in file:
            pdf_set.add(i)
    remain_html = html_set-pdf_set

    html_pdf_path_dict={}
    for i in remain_html:
        pdfName = i.replace('html','pdf')
        html_pdf_path_dict.update({os.path.join(html_path,i):os.path.join(pdf_path,pdfName)})

    return html_pdf_path_dict

