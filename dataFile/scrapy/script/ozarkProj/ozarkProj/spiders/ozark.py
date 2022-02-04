import scrapy
from datetime import datetime
import time
import pdfkit
def alter_name(ori_name):
    result=''
    s ='S04'
    e = ori_name[ori_name.index('第')+1:ori_name.index('集')]
    if e =='一':
        result = s + 'E01-'+ori_name[ori_name.index('集')+2:-1]
    if e == '二':
        result = s + 'E02-'+ori_name[ori_name.index('集')+2:-1]
    if e == '三':
        result = s + 'E03-'+ori_name[ori_name.index('集')+2:-1]
    if e == '四':
        result = s + 'E04-'+ori_name[ori_name.index('集')+2:-1]
    if e == '五':
        result = s + 'E05-'+ori_name[ori_name.index('集')+2:-1]
    if e == '六':
        result = s + 'E06-'+ori_name[ori_name.index('集')+2:-1]
    if e == '七':
        result = s + 'E07-'+ori_name[ori_name.index('集')+2:-1]
    if e == '八':
        result = s + 'E08-'+ori_name[ori_name.index('集')+2:-1]
    if e == '九':
        result = s + 'E09-'+ori_name[ori_name.index('集')+2:-1]
    if e == '十':
        result = s + 'E10-'+ori_name[ori_name.index('集')+2:-1]
    if e == '十一':
        result = s + 'E11-'+ori_name[ori_name.index('集')+2:-1]
    if e == '十二':
        result = s + 'E12-'+ori_name[ori_name.index('集')+2:-1]
    print(result)
    return result



class OzarkSpider(scrapy.Spider):
    name = 'ozark'
    # allowed_domains = ['www.cc.com']
    # start_urls = ['https://www.kexiaoguo.com/meiju196/1/']
    # start_urls = ['https://www.kexiaoguo.com/meiju196/69/']
    # start_urls = ['https://www.kexiaoguo.com/meiju196/134/']
    start_urls = ['https://www.kexiaoguo.com/meiju196/199/']
    base_url ='https://www.kexiaoguo.com'

    def parse(self, response):

        ls = response.xpath('.//div[@id="daohang"]/ul[1]/li')

        for i in ls :
            part_url = self.base_url+i.xpath('./p/a/@href').get()
            part_name = i.xpath('./p/a/text()').get()

            print(part_name,part_url)

            yield scrapy.Request(url=part_url,callback=self.parse_detail,meta={'name':part_name})


    def parse_detail(self,response):
        name = response.meta['name']
        name_new = alter_name(name)
        content = response.xpath('.//div[@id="neirong"]/p').get()

        c = '<h1>第一季</h1><h2>{}</h2>{}'.format(name,content)
        cc=c.replace('♥','')
        # print(cc)
        options = {
            # --disable - smart - shrinking         不使用智能收缩策略
            # --enable - smart - shrinking          使用智能收缩策略(这是默认设置)
            '--disable-smart-shrinking':True,
            '--title': '[title]',  # 展示 h1、h2、h3等各级标题作为大纲
            '--page-size': 'Letter',
            '--encoding': "UTF-8",
            '--minimum-font-size':20,
            # '--header-left':pub,#页眉左边,
            # '--header-right':'我是右边页眉',#页眉右边，添加页码,
            '--footer-right': '[page]/[toPage]',  # 页脚右边，添加页码,
            # '--header-line':'--header-line', #添在页眉下方显示一条直线分隔正文
            # '--header-spacing':'5' #页眉与正文之间的距离(默认为零)
        }
        config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        print('正在生成pdf文件 ---> ', name_new)
        start = datetime.now()
        outpath='F:\\PDF\\美剧字幕\\Ozark-s04\\'+name_new+'.pdf'
        print(outpath)
        pdfkit.from_string(cc, outpath, options=options, configuration=config)

        end = datetime.now()

        print('pdf文件生成完成，用时 {} 秒'.format(end - start))


