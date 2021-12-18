import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ..items import CrawlprojItem,CrawlprojDetailItem
class SunSpider(CrawlSpider):

    name = 'sun'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=6']
    # LinkExtractor 链接提取器 ：根据指定规则(allow='正则')进行指定链接的提取
    # Rule规则解析器：将链接提取器提取到的链接进行指定规则(callback)的解析操作
    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/politics/index\?id=\d+'), callback='parse_detail')
    )
    k = 0
    def parse_item(self, response):
        self.k+=1
        print('---{}---'.format(self.k))
        #xpath表达式不能出现tbody否则不能正确定位
        ls = response.xpath('//ul[@class="title-state-ul"]/li')
        for i in ls:
            id = i.xpath('./span[1]/text()').get()
            detailUrl = i.xpath('./span[3]/a/@href').get()
            detailTitle = i.xpath('./span[3]/a/text()').get()
            print(id,detailTitle,detailUrl)
            item = CrawlprojItem()
            item['id']=id
            item['detailUrl']=detailUrl
            item['detailTitle']=detailTitle

            yield item

    def parse_detail(self,response):

        num = response.xpath('//div[@class="mr-three"]/div[1]/span[4]/text()').get()
        detailTitle = response.xpath('//div[@class="mr-three"]/p/text()').get()
        detailContent = response.xpath('//div[@class="mr-three"]/div[2]/pre/text()').get()

        # print(num,'-',detailTitle,'\n',detailContent)

        item = CrawlprojDetailItem()
        item['num']=num
        item['detailTitle']=detailTitle
        item['detailContent']=detailContent
        yield item


