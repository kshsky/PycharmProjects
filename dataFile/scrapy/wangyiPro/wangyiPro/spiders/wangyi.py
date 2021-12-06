from __future__ import absolute_import
import scrapy
from selenium import webdriver
from ..items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['www.xx.com']
    start_urls = ['https://news.163.com/']

    # 图片 https://news.163.com/photo/#Current
    # 国内 https://news.163.com/domestic/
    # 国际 https://news.163.com/world/
    # 数读 https://data.163.com/special/datablog/
    # 军事 https://war.163.com/
    # 航空 https://news.163.com/air/
    # 传媒研究院 https://news.163.com/college
    # 政务 https://gov.163.com/
    # 公益 https://gongyi.163.com/yikuaiping/
    # 媒体 https://media.163.com/
    # 王三三 https://news.163.com/special/wangsansanhome/

    url_ele =['domestic','world','air','war']
    section_url_list = []
    # executable_path = "dataFile/scrapy/chromedriver.exe",
    #实例化浏览器对象
    # def __init__(self):
    #     pass
        # options.add_argument('--headless')  # 设置无界面
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # self.driver= webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe')
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
                    self.section_url_list.append(section_url)
                    urlItemDict.update({section_url:item})
            # print(self.section_url_list)
        for i in self.section_url_list:
            print('传参。。。',i)
            yield scrapy.Request(url = i, callback=self.parse_model)

    def parse_model(self,response):
        print(response.text)
        # item = scrapy.meta['item']
        print('--->>> parse model ---')
        # print('>>>'+item['sectionName'])

        info_list = response.xpath('/div[@class="ndi_main"]/div')
        for i in info_list:
            infoDetailUrl = i.xpath('./div/div/div[1]/h3/a/@href').get()
            infoTitleName = i.xpath('./div/div/div[1]/h3/a/text()').get()
            # item['infoTitleName']=infoTitleName
            # item['infoDetailUrl']=infoDetailUrl

            yield scrapy.Request(infoDetailUrl,callback=self.parse_detail)


    def parse_detail(self,response):
        item = scrapy.meta['item']
        infoDetailContent = response.xpath('//div[@class="post_body"]//text()')
        item['infoDetailContent'] = infoDetailContent
        yield item


