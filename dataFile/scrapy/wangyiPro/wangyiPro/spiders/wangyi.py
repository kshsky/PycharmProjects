from __future__ import absolute_import
import scrapy
from selenium import webdriver
from ..items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'

    start_urls = ['https://news.163.com/']
    url_ele =['domestic','world','air','war']
    section_url_list = []
    # executable_path = "dataFile/scrapy/chromedriver.exe",
    #实例化浏览器对象
    flag = 0
    status = 0
    def __init__(self):
        self.driver= webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe')
    def parse(self, response):

        # section_list = response.xpath('//div[@class="ns_area list"]/ul/li[position > 1]')
        section_list = response.xpath('//div[@class="ns_area list"]/ul/li[position()>1]')
        urlItemDict={}
        for i in section_list:
            # print(i)
            section_url =i.xpath('./a/@href').get()
            section_name = i.xpath('./a/text()').get()
            # print(section_name,section_url)
            for e in self.url_ele:
                if e in section_url:
                    item = WangyiproItem()
                    item['sectionName'] = section_name
                    item['sectionUrl'] = section_url
                    # print(item)
                    self.section_url_list.append(section_url)
                    urlItemDict.update({section_url:item})

        self.flag=1
        for i in self.section_url_list:
            yield scrapy.Request(url = i, callback=self.parse_sectoin,meta={'item':urlItemDict[i]})

    def parse_sectoin(self,response):
        item = response.meta['item']
        print('section >>> url:{} status:{} flag:{}'.format(response.url, self.status, self.flag))

        with open('./txt/'+item['sectionName']+'.txt','w',encoding='utf8') as fp:
            fp.write(response.text)

        # infoDetailUrl =