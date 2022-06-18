import scrapy
import datetime
from ..items import CeprojItem
class CeSpider(scrapy.Spider):
    name = 'ce'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://paper.ce.cn/pc/layout/202101/01/node_01.html']
    start_urls = []
    base_url = 'http://paper.ce.cn/pc/layout/{}/node_01.html'
    pdf_url_prefix='http://paper.ce.cn/pc/'
    start = datetime.date(2022,3,14)
    end = datetime.date(2022,6,16)
    delta = datetime.timedelta(days=1)
    d = start
    while d <= end:
        print(d.strftime('%Y%m/%d'))
        start_urls.append(base_url.format(d.strftime('%Y%m/%d')))
        d +=delta

    def parse(self, response):
        # print(response.text[:20000])
        cur_url = response.url
        date = cur_url[cur_url.rindex('/')-9:cur_url.rindex('/')]
        ls = response.xpath('.//ul[@class="page-num"]/li')
        for i in ls:
            oriname = i.xpath('./a/text()').get()
            oriurl = i.xpath('./input/@value').get()
            url = self.pdf_url_prefix + oriurl[oriurl.index('attachment'):]
            name=date[:4]+'-'+date[4:6]+'-'+date[7:]+'-'+oriname+'.pdf'
            print(name,url)

            dirname = date[:4]+'-'+date[4:6]
            item = CeprojItem()
            item['dirname']=dirname
            item['name']=name
            item['url']=url

            yield item
