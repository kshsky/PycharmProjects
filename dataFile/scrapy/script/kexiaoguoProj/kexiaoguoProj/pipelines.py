# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import time
import pdfkit

class KexiaoguoprojPipeline:
    def process_item(self, item, spider):
        return item


    def close_spider(self, spider):

        options = {
            '--disable-smart-shrinking': True,
            '--title': '[title]',  # 展示 h1、h2、h3等各级标题作为大纲
            '--page-size': 'Letter',
            '--encoding': "UTF-8",
            '--minimum-font-size': 20,
            # '--header-left':pub,#页眉左边,
            # '--header-right':'我是右边页眉',#页眉右边，添加页码,
            '--footer-right': '[page]/[toPage]',  # 页脚右边，添加页码,
            # '--header-line':'--header-line', #添在页眉下方显示一条直线分隔正文
            # '--header-spacing':'5' #页眉与正文之间的距离(默认为零)
        }
        config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        print('正在生成pdf文件 ---> ', spider.file_path)
        file_content=''
        file_order = sorted(spider.file_content_dict)
        for i in file_order:
            file_content+= spider.file_content_dict.get(i)

        start = datetime.now()
        pdfkit.from_string(file_content, spider.file_path, options=options, configuration=config)
        end = datetime.now()

        print('pdf文件生成完成，用时 {} 秒'.format(end - start))
        print('>>> close spider successfully ... ... ')
