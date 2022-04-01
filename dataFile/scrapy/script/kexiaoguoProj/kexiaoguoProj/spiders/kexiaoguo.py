import scrapy
from datetime import datetime
import time
import pdfkit

def get_name_num(ori_name):
    e = ori_name[ori_name.index('第')+1:ori_name.index('集')]
    ep = ori_name[ori_name.index('Part')+4:]
    trans_dict={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'十一':11,'十二':12,'十三':13,'十四':14,'十五':15,'十六':16}
    return  trans_dict[e]*10+int(ep)

class KexiaoguoSpider(scrapy.Spider):
    name = 'kexiaoguo'
    # allowed_domains = ['www.xxx.com']
    #第一季 warrior
    # start_urls = ['https://www.kexiaoguo.com/meiju295/1/']
    # 第二季warrior
    # start_urls = ['https://www.kexiaoguo.com/meiju295/53/']
    #黑钱胜地s01
    # start_urls=['https://www.kexiaoguo.com/meiju196/69/']
    #ozark s02
    # start_urls=['https://www.kexiaoguo.com/meiju196/1/']
    #ozark s03
    # start_urls=['https://www.kexiaoguo.com/meiju196/134/']
    #ozark s04
    start_urls=['https://www.kexiaoguo.com/meiju196/199/']
    file_content_dict={}
    base_url= 'https://www.kexiaoguo.com'
    teleplay_name='Ozark'
    teleplay_season='s04'
    file_name = teleplay_name+'_'+teleplay_season
    file_path='F:\\PDF\\美剧字幕\\{}.pdf'.format(file_name)
    def parse(self, response):

        ls = response.xpath('.//div[@id="daohang"]/ul[1]/li')

        for i in ls:
            part_url = self.base_url + i.xpath('./p/a/@href').get()
            part_name = i.xpath('./p/a/text()').get().strip()

            print(part_name, part_url)

            yield scrapy.Request(url=part_url, callback=self.parse_detail, meta={'part_name': part_name})

    def parse_detail(self,response):
        part_name = response.meta['part_name']
        content = response.xpath('.//div[@id="neirong"]/p').get()
        c = '<h1>{}</h1>{}'.format(part_name, content)
        cc = c.replace('♥', '')
        self.file_content_dict.update({get_name_num(part_name):cc})

