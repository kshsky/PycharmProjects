import scrapy
import logging
from ..items import ZqrbprojItem
from bs4 import BeautifulSoup as bs
import datetime
class ZqrbSpider(scrapy.Spider):
    name = 'zqrb'
    allowed_domains = ['www.cc.com']
    start_urls = ['http://epaper.zqrb.cn/html/2022-06/18/node_2.htm']
    base_url='http://epaper.zqrb.cn/'
    date=datetime.date(2022,6,19)
    datestr=date.strftime('%Y-%m-%d')
    # model_url ='http://epaper.zqrb.cn/html/{}/node_2.htm'.format('2022-06/18')

    # start_urls.append(model_url)
    day_dict={}
    page_dict={}
    label_dict={}

    def parse(self, response):
        # print(response.text)
        soup = bs(response.text,'lxml')
        request=response.url
        pos = request.index('html')
        date =request[pos+5:pos+15]
        year=date[:4]
        month=date[5:7]
        day=date[8:]
        dirname=year +'/'+year+'-'+month

        print('=================')
        ls = response.xpath('.//table[@class="biaoge"]')

        for i in ls:
            pageName = i.xpath('.//h2/a/text()').get().strip()
            rel_url = i.xpath('.//h2/span/a/@href').get()
            url = self.base_url+rel_url[rel_url.index('images'):]
            print(pageName,url)

            pagenum = i.xpath('.//table[@bgcolor="#ffffff"]/@id').get()
            details = i.xpath('.//table[@bgcolor="#ffffff"]/tr')

            print('\n{}\n'.format(pagenum))
            page_content =''
            k = 1
            for j in details:
                #vote_content12px
                detail = j.xpath('.//a[@class="vote_content12px"]/text()').get().strip()
                page_content +='({}){}<br>'.format(k,detail)
                k+=1
                print(detail)
            self.page_dict.update({pagenum:page_content})
            self.day_dict.update({year+'-'+month:self.page_dict})
            self.label_dict.update({year:self.day_dict})

        logging.info(self.label_dict)

        # item download
        ls = response.xpath('.//div[@id="pgn"]/table/tbody/tr')
        for i in ls:
            pagename = i.xpath('.//a[@id="pageLink"]/text()').get().strip()
            # float: right;
            rel_url = i.xpath('.//div[@style="float: right;"]/a/@href').get()

            pageurl = self.base_url + rel_url[rel_url.index('images'):]
            print('----', pagename, pageurl)

            item = ZqrbprojItem()
            item['url'] = pageurl
            item['dirname'] = dirname
            item['name'] = pagename+'.pdf'
            print(item)
            yield item


