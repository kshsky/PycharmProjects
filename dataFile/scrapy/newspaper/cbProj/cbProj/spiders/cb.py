import scrapy
import datetime
import time
import re
from ..items import CbprojItem
class CbSpider(scrapy.Spider):
    name = 'cb'
    allowed_domains = ['www.cc.som']
    start_urls = []
    issue_url='http://dianzibao.cb.com.cn/html/{}/node_1.htm'
    base_url='http://dianzibao.cb.com.cn/'
    year=2006
    start =datetime.date(year,11,21)
    # start =datetime.date(2006,1,2)
    end =datetime.date(year,11,30)

    delta = datetime.timedelta(days=1)
    d=start
    while d <=end:
        if d.isoweekday()==1:
            start_urls.append(issue_url.format(d.strftime('%Y-%m/%d')))
        d += delta


    def parse(self, response):
        issue_url = response.url

        date = issue_url[issue_url.index('html')+5:issue_url.index('html')+15]
        # print(date)
        ls = response.xpath('.//div[@id="bmdh"]/table/tbody/tr')
        if len(ls)==0:
            print(date,' : 没有数据')
            return
        for i in ls:
            pageName = i.xpath('./td[2]/a/text()').get()
            relative_url = i.xpath('./td[3]/a/@href').get()
            # print(pageName,relative_url)

            #针对2005年第一招商
            pageName=re.sub('第\s','第1',pageName)

            #去掉其他空格
            pageName = re.sub('\s', '', pageName)

            item = CbprojItem()
            item['name']=date.replace('/','-')+'-'+pageName.replace('/','-').replace(':','-')+'.pdf'
            item['url']=self.base_url+relative_url[relative_url.index('images'):]
            item['dirname']=date[:4]+'/'+date[:7]
            print(item)
            yield item

