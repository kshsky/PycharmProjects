from datetime import datetime

import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver

from ..items import XiaoprojItem
import time
import re
def validateTitle(title):

    #替换英文字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    rep_en = re.sub(rstr, "_", title)  # 替换为下划线

    #替换中文字符
    rstr2=r"[：？'‘“”]"
    result = re.sub(rstr2, "-", rep_en)  # 替换为下划线

    return result

class XiaoSpider(scrapy.Spider):
    name = 'xiao'
    start_urls = ['http://baixiaosheng.net/page/16']
    base_usl ='http://baixiaosheng.net/page/{}'
    page = 16
    columnList=['page','id','title','public','contentUrl']
    tableName ='baixiaosheng'

    def __init__(self):
        print("初始化浏览器")
        self.driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe')

    def parse(self, response):
        # print(response.text)
        ls = response.xpath('//div[@id="main"]/div[position()!=last()]')
        print('--- {} ---'.format(self.page))
        for i in ls:
            # print(i)
            title = i.xpath('./div[2]/h1[@class="excerpt-title"]/a/text()').get()
            contentUrl = i.xpath('./div[2]/h1[@class="excerpt-title"]/a/@href').get()
            time = i.xpath('./div[1]').xpath('string(.)').get().strip()

            # print(title,contentUrl)
            item = XiaoprojItem()
            item['title']=title
            item['contentUrl']=contentUrl
            item['id']=contentUrl[-4:]
            item['page']=str(self.page)

            year = time[time.index('by')-5:time.index('by')-1]
            month = time[time.index('d') + 1:time.index('月')].strip()
            date = time[time.index(',') - 4:time.index(',') - 2].strip()
            if len(month) == 1:
                month = '0' + month
            if len(date) == 1:
                date = '0' + date

            item['public'] = year + '_' + month + '_' + date

            yield item

        self.page +=1
        next_page = self.base_usl.format(str(self.page))
        print(next_page)
        # if self.page <=16:
        #     yield scrapy.Request(url = next_page,callback=self.parse)

    # def parse_detail(self,response):
    #     item = response.meta['item']
    #
    #     soup =BeautifulSoup(response.text,'lxml')
    #
    #     content = soup.find(name='article')
    #     time = soup.find(name='div',class_='entry-meta-top').contents[0].strip()
    #
    #     # Published 8月 28th, 2019 by
    #     # Published 7月 23rd, 2018 by
    #     print(time)
    #     year = time[-7:-3]
    #     month = time[time.index('d')+1:time.index('月')].strip()
    #     date = time[time.index(',')-4:time.index(',')-2].strip()
    #     if len(month)==1:
    #         month = '0'+month
    #     if len(date) == 1:
    #         date = '0' + date
    #
    #     title_old = item['title']
    #     item['title']=year+'_'+month+'_'+date+'_'+title_old
    #     item['id']=content
    #
    #     yield item






