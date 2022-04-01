import scrapy

from cbjProj.items import CbjprojItem
class CbjSpider(scrapy.Spider):
    name = 'cbj'
    # allowed_domains = ['www.cc.com']
    start_urls = ['http://dianzibao.cb.com.cn/html/2022-02/28/node_1.htm']
    # http://dianzibao.cb.com.cn/images/2022-03/07/13/2445B09C.pdf
    baseUrl = 'http://dianzibao.cb.com.cn/'

    def parse(self, response):

        # print(response.text[:100])

        ls = response.xpath('.//td[@style="BORDER-TOP: #C0C0C0 1px solid"]/div/table/tbody/tr')
        for i in ls:
            name = i.xpath('./td[1]/a[@id="pageLink"]/text()').get()
            href = i.xpath('./td[2]/a/@href').get()
            url = self.baseUrl+href[href.index('images'):]

            item = CbjprojItem()
            item['name']=name.replace('：','-')
            item['url']=url
            print(name)
            print(href)

            yield item

