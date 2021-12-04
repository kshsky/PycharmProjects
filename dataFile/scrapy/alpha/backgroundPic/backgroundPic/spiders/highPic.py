from __future__ import absolute_import
import scrapy
from ..items import BackgroundpicItem

class HighpicSpider(scrapy.Spider):
    name = 'highPic'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wall.alphacoders.com/by_resolution.php?w=5184&h=3456&lang=Chinese&page=1']
    url_prefix='https://wall.alphacoders.com'
    url = 'https://wall.alphacoders.com/by_resolution.php?w=5184&h=3456&lang=Chinese&page={}'
    page_num = 1
    def parse(self, response):

        pic_list = response.xpath('//div[@id ="big_container"]/div[1]/div[2]/div')
        # print(pic_list)

        for i in pic_list:
            id = i.xpath('./@id').get()
            img_big = self.url_prefix + i.xpath('./div[1]/div[1]/a/@href').get()
            name_ori = i.xpath('./div[1]/div[1]/a/@title').get()
            img_small_ori = i.xpath('./div[1]/div[1]/a/picture//img/@src').get()

            name = name_ori.replace(' ','_')+id[id.index('_'):]
            print(id,name,img_big,img_small_ori)

            items = BackgroundpicItem()
            items['name']=name
            items['small']=img_small_ori
            items['src']=img_big

            yield items

        #递归爬取所有page

        if self.page_num < 10:
            print('--- {} ---'.format(self.page_num))
            self.page_num +=1
            new_url = self.url.format(self.page_num)
            yield scrapy.Request(url = new_url,callback=self.parse)
