# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import FilesPipeline
import pdfkit
import scrapy
import logging
from datetime import datetime
from scrapy.utils.project import get_project_settings
#文件下载pipeline
class ZqrbprojPipeline(FilesPipeline):

    item =None

    # 获取文件url
    def get_media_requests(self, item, info):
        self.item = item
        yield scrapy.Request(item['url'])

    #文件名命
    def file_path(self, request, response=None, info=None, *, item=item):

        name ='//'+item['dirname'] +'//'+item['name']
        return name

    # 下载结束，item 释放【可以去掉】
    def item_completed(self, results, item, info):
        # print('---------------->','download OK …')
        return item


#生成pdf的pipeline
class createPDFPipeline:
    item = None
    def process_item(self, item, spider):
        self.item = item
        return item

    def close_spider(self,spider):
        options = {
            '--disable-smart-shrinking': True,  # 不使用智能收缩策略,这样字体设置才有效
            '--title': '[title]',  # 展示 h1、h2、h3等各级标题作为大纲
            '--page-size': 'Letter',
            '--encoding': "UTF-8",
            '--minimum-font-size': 20,  # 字体20刚刚好
            '--footer-center': '[page]/[toPage]',  # 页脚中间添加页码,
        }
        config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

        label_dict = spider.label_dict

        all_content =''

        h1_order= sorted(label_dict)
        year=''
        for i in h1_order:
            year=i[:4]
            #h1 是 2022-06,2022-05
            all_content +='<h1>{}</h1>\n'.format(i)

            h2_dict = label_dict.get(i)
            #h2 是 01，02，... 30
            h2_order=sorted(h2_dict)
            for j in h2_order:
                all_content += '<h2>{}</h2>\n'.format(j)

                h3_dict = h2_dict.get(j)
                #h3 是 pagenum ：A01 A03 C23
                # h3_order=sorted(h3_dict)
                for x in h3_dict:
                    all_content +='<h3>{}</h3>\n{}'.format(x,h3_dict.get(x))
        # 配置file_path
        settings = get_project_settings()
        file_path = settings.get('FILES_STORE')
        d = spider.start.strftime('%Y-%m')
        file_abs_path =file_path+ '/'+d[:4]+'/'+d+'.pdf'
        # file_abs_path =file_path+ year+'/'+year+'.pdf'
        print('正在生成pdf文件 ---> ', file_abs_path)
        logging.info(all_content)
        start = datetime.now()
        pdfkit.from_string(all_content, file_abs_path, options=options, configuration=config)
        end = datetime.now()

        print('pdf文件生成完成，用时 {} 秒'.format(end - start))

        print('>>> close spider successfully ... ... ')
        logging.info('--------------------------------------------------------')