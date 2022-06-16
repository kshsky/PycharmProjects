# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import time
import pdfkit

class QiushiprojPipeline:

    def persistHtml(self,filepath,filename,content):


        print('正在生成html文件 ---> ',filename)
        abspath = filepath+'/'+filename+'.html'
        start = datetime.now()
        with open(abspath, 'w', encoding='UTF-8') as fp:
            fp.write(content)
        fp.close()
        end = datetime.now()
        print('html文件生成完成，用时 {} 秒'.format(end - start))


    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):

        options = {
            '--disable-smart-shrinking': True, #不使用智能收缩策略,这样字体设置才有效
            '--title': '[title]',  # 展示 h1、h2、h3等各级标题作为大纲
            '--page-size': 'Letter',
            '--encoding': "UTF-8",
            '--minimum-font-size': 20,#字体20刚刚好
            # '--header-left':'film',#页眉左边,
            # '--header-right':'smith',#页眉右边，添加页码,
            '--footer-center': '[page]/[toPage]',  # 页脚中间添加页码,
            # '--footer-right': '[page]/[toPage]',  # 页脚右边，添加页码,
            # '--header-line':'--header-line', #添在页眉下方显示一条直线分隔正文
            # '--header-spacing':'5' #页眉与正文之间的距离(默认为零)
        }
        config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        file = spider.filepath + spider.filename + '.pdf'

        print('正在生成html文件 ---> ', file.replace('pdf','html'))
        file_content=''
        file_order = sorted(spider.magazine)
        for i in file_order:
            if spider.magazine.get(i) is not None:
                file_content+= spider.magazine.get(i)

        start = datetime.now()
        self.persistHtml(spider.filepath, spider.filename, file_content)

        print('正在生成pdf文件 ---> ', file)
        pdfkit.from_file(file.replace('pdf','html'),file,options=options, configuration=config)
        # pdfkit.from_string(file_content, file, options=options, configuration=config)
        end = datetime.now()

        #先生成html文件，然后转换成pdf

        print('pdf文件生成完成，用时 {} 秒'.format(end - start))
        print('>>> close spider successfully ... ... ')
