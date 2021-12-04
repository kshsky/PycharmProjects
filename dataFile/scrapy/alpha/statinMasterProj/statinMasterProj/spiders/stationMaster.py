from __future__ import absolute_import
import scrapy
from ..items import StatinmasterprojItem


class StationmasterSpider(scrapy.Spider):
    name = 'stationMaster'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']
    url = 'https://sc.chinaz.com/tupian/index_{}.html'
    page = 1
    def parse(self, response):

        ls = response.xpath('//div[@id="container"]/div')

        for i in ls:
            #在屏幕可视化区域用src，直接爬取没有屏幕，使用伪属性
            avatar = 'https:'+i.xpath('./div/a/img/@src2').get()
            name = i.xpath('./p/a/text()').get()
            midSrc = 'https:'+i.xpath('./p/a/@href').get()

            item = StatinmasterprojItem()
            item['name']=name
            item['avatar']=avatar
            item['midSrc']=midSrc

            # print(name,avatar,midSrc)

            yield scrapy.Request(url=midSrc,callback=self.parse_src,meta={'item':item})
            # break

        # if self.page <=5:
        #     print('---{}---'.format(self.page))
        #     self.page +=1
        #     next_page = self.url.format(self.page)
        #     yield scrapy.Request(url=next_page,callback=self.parse)



    def parse_src(self,response):
        item =response.meta['item']
        imgSrc =  'https:'+response.xpath('//div[@class="imga"]/a/img/@src').get()
        item['imgSrc'] =imgSrc

        print(imgSrc)
        yield item



