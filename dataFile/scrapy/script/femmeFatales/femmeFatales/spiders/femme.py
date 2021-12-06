from __future__ import absolute_import
import scrapy
from ..items import FemmefatalesItem
import os
class FemmeSpider(scrapy.Spider):
    name = 'femme'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.kexiaoguo.com/dianying6466/1/']
    url ='https://www.kexiaoguo.com/meiju391/{}/'
    page = 1


    def parse(self, response):

        html = response.text

        with open('./response.txt','w',encoding='utf8') as fp:
            fp.write(html)
        # / *[p or li] / text()[not (ancestor::a) and not (ancestor::script) and not (ancestor:: *[@ data-alink-ignore])]
        print(' ---{}---'.format(self.page))
        ll = response.xpath('//div[@id="neirong"]/p[1]/text()')
        content =''
        for i in ll:
            ii = i.get()
            content += ii + '\n'

        item = FemmefatalesItem()
        item['content']=content
        item['name']='No Time to Die'
        item['page']=self.page

        self.page +=1

        yield item
        next_page = self.url.format(self.page)
        if self.page <= 12:
            yield scrapy.Request(next_page,callback=self.parse)









