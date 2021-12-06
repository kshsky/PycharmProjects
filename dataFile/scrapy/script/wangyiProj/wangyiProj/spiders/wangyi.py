from __future__ import absolute_import
import scrapy
from scrapy.utils import spider

from ..items import WangyiprojItem
import os
from selenium import webdriver
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.sx.com']
    start_urls = ['https://news.163.com/']
    section_url_list=[]
    # section_url_list =['https://news.163.com/domestic/','https://news.163.com/world/','https://war.163.com/','https://news.163.com/air/']
    need_element =['domestic','world','air','war']

    flag = 0
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe')
    def parse(self, response):

        ls = response.xpath('//div[@class="ns_area list"]/ul/li[position()>1]')
        urlItemDict={}
        for e in self.need_element:
            for i in ls:
                sectionUrl = i.xpath('./a/@href').get()
                sectionName =i.xpath('./a/text()').get()
                if e in sectionUrl:
                    item = WangyiprojItem()
                    item['sectionUrl']=sectionUrl
                    item['sectionName']=sectionName
                    self.section_url_list.append(sectionUrl)
                    urlItemDict.update({sectionUrl:item})
                    # print(sectionName,sectionUrl)
        print(urlItemDict)
        for i in self.section_url_list:
            yield scrapy.Request(i,callback=self.parse_section,meta={'item':urlItemDict[i]})

    def parse_section(self,response):
        item = response.meta['item']
        sectionName =item['sectionName']
        print(sectionName, item['sectionUrl'])
        if self.flag ==0:
            with open('./txt/'+sectionName+'-10.txt','w',encoding='utf8') as fp:
                fp.write(response.text)
            print('---------- parse_section --------------')
            # web页面上的数据是在class=“ndi_main”的div里，而实际返回的html页面，数据在<div class="hidden">里，
            # 这是由于页面的懒加载造成的，因此需要使用Selenium模拟浏览器重新发起请求，返回最终和web一样的response
            info_list = response.xpath('//div[@class="hidden"]/div')
            for i in info_list:
                infoTital = i.xpath('./a/text()').get()
                infoDetailUrl = i.xpath('./a/@href').get()
                print(infoTital,infoDetailUrl)
        if self.flag==1:
            with open('./txt2/' + sectionName + '-2.txt', 'w', encoding='utf8') as fp:
                fp.write(response.text)
            print('---------- 2 --------------',sectionName)
            # web页面上的数据是在class=“ndi_main”的div里，而实际返回的html页面，数据在<div class="hidden">里，
            # 这是由于页面的懒加载造成的，因此需要使用Selenium模拟浏览器重新发起请求，返回最终和web一样的response
            info_list = response.xpath('//div[@class="na_detail clearfix "]')
            for i in info_list:
                item2 = WangyiprojItem()
                infoTitle = i.xpath('./div/h3/a/text()').get()
                infoDetailUrl = i.xpath('./div/h3/a/@href').get()

                item2['sectionName']=item['sectionName']
                item2['sectionUrl']=item['sectionUrl']
                item2['infoTitle']=infoTitle
                item2['infoDetailUrl']=infoDetailUrl

                # print(infoTitle, infoDetailUrl)
                # print('>>>>>\n',item)
                spider.logger.info('%s - %s'%(infoTitle, infoDetailUrl))
                # spider.logger.info('>>>>>\n %s' % (item))
                #设置flag=8 ，经过管道下载器时，不处理
                self.flag=5
                yield scrapy.Request(infoDetailUrl,callback=self.parse_detail,meta={'item':item2})

    def parse_detail(self,response):
        item = response.meta['item']
        print('DETAIL:',item)

        spider.logger.info('DETAIL === %s >>>> %s' % (item['infoTitle'],item['infoDetailUrl']))
        # spider.logger.info('%s >>>>>\n %s' % (str(self.flag),item))
        print('------- detail ---------',item['infoTitle'])

        sectionContent_list = response.xpath('//div[@class="post_body"]//text()')

        txt = ''
        for i in sectionContent_list:
            txt += i.get().strip()+'\n'

        item ['infoDetailContent']=txt
        yield item