from __future__ import absolute_import
import scrapy
from ..items import BeautyprojItem

class GorgeSpider(scrapy.Spider):
    name = 'gorge'
    start_urls = ['https://wall.alphacoders.com/by_category.php?id=33&name=%E5%A5%B3%E6%80%A7+%E5%A3%81%E7%BA%B8&lang=Chinese&page=1']
    url_prefix = 'https://wall.alphacoders.com'
    url = 'https://wall.alphacoders.com/by_resolution.php?w=5184&h=3456&lang=Chinese&page={}'
    page_num = 1

    def parse(self, response):
        pic_list = response.xpath('//div[@id ="big_container"]/div[1]/div[2]/div')
        for i in pic_list:
            id = i.xpath('./@id').get()
            middleSrc = self.url_prefix + i.xpath('./div[1]/div[1]/a/@href').get()
            name_ori = i.xpath('./div[1]/div[1]/a/@title').get()
            avatar = i.xpath('./div[1]/div[1]/a/picture//img/@src').get()

            name = name_ori.replace(' ', '_') + id[id.index('_'):]
            print(id, name, middleSrc, avatar)
            item = BeautyprojItem()
            item['id']= id
            item['name']= name
            item['avatar']=avatar
            item['middleSrc']=middleSrc
            yield scrapy.Request(middleSrc,callback=self.parse_src,meta ={'item':item})

        if self.page_num<=20:
            print('--- {} ---'.format(self.page_num))
            self.page_num +=1
            next_page = self.url.format(self.page_num)

            yield scrapy.Request(next_page,callback=self.parse)

    def parse_src(self,response):

        item = response.meta['item']

        imgSrc = response.xpath('//*[@id="page_container"]/div[4]/a/picture//img/@src').get()

        item['imgSrc'] = imgSrc
        yield item


