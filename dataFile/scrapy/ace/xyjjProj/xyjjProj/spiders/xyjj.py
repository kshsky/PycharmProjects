import scrapy
import time
from ..items import XyjjprojItem
class XyjjSpider(scrapy.Spider):
    name = 'xyjj'
    # allowed_domains = ['www.xx.com']
    start_urls = []
    xyjj='https://www.xyshjj.cn'
    #中国县域经济报
    # errorlist=['1467','1468','1469','1470','1471','1472','1473','1474','1479','1480']

    page=16
    for i in rang(page):
    # for i in [13,14]:
        start_urls.append('https://www.xyshjj.cn/list-1487-1489-0-{}.html'.format(i))

    def parse(self, response):
        ls = response.xpath('.//div[@class="article-list"]/div')
        for i in ls:
            url = i.xpath('./div/a/@href').get()
            name = i.xpath('./div/a/text()').get()
            if name.find('总')==-1:
                continue
            #2019年10月14日 第77期（总第1475期）
            # 格式：总期数-年-月-日-年度期数-版
            # 格式：1475-2019-10-14-77-01
            total_issue = name[name.rindex('总')+2:name.rindex('期')]
            year_issue = name[name.index('第')+1:name.index('期')]
            year=name[:4]
            month = name[name.index('年')+1:name.index('月')]
            month = '0'+month if len(month)==1 else month
            date = name[name.index('月')+1:name.index('日')]
            date = '0' + date if len(date) == 1 else date
            pname = total_issue +'-'+year+'-'+month+'-'+date+'-'+year_issue
            url = self.xyjj + '/'+url
            # print(url,' - ',pname)
            # if total_issue not in self.errorlist:
            #     continue
            print('-----------> ',total_issue)
            yield scrapy.Request(url =url,callback=self.parse_item,meta={'pname':pname})

    def parse_item(self, response):
        pname = response.meta['pname']
        ls = response.xpath('.//div[@class="article-main"]/div/p[position()!=last()]')
        for i in ls:
            if len(i.xpath('.//a'))==0:
                continue
            url = self.xyjj+i.xpath('.//a/@href').get()
            name = pname+'-'+i.xpath('.//a/@title').get()[:2]
            item = XyjjprojItem()
            item['url']=url
            item['name']=name+'.pdf'
            item['year']=pname[pname.index('-')+1:pname.index('-')+5]

            print(url,name)
            yield item






