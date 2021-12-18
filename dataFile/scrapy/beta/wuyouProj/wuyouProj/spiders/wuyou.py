from __future__ import absolute_import
import scrapy

from ..items import WuyouprojItem
class WuyouSpider(scrapy.Spider):
    name = 'wuyou'
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']
    model_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    page = 1

    def parse(self, response):

        listx = response.xpath('//div[@class="j_joblist"]/div')
        for i in listx:
            job= i.xpath('.//a[@class="el"]/p[1]/span[1]/text()').get()
            releaseDate=i.xpath('.//a[@class="el"]/p[1]/span[2]/text()').get()
            salary= i.xpath('.//a[@class="el"]/p[2]/span[1]/text()').get()

            info=i.xpath('.//a[@class="el"]/p[2]/span[2]/text()').get()
            company=i.xpath('.//div[@class="er"]/a/text()').get()
            companyType=i.xpath('.//div[@class="er"]//p').xpath('normalize-space(string(.))').get()

            # columnlist=['job','releaseDate','info','company','companyType']

            item = WuyouprojItem()
            item['job']=job
            item['releaseDate']=releaseDate
            item['salary']=salary
            item['info']=info
            item['company']=company
            item['companyType']=companyType

            # print(item)

            yield item

        self.page +=1
        if self.page <=8:

            url = self.model_url.format(self.page)
            print('正在加载第 {} 页 ... '.format(self.page))
            yield scrapy.Request(url=url,callback=self.parse)
        else:
            print('crawl done normally ... ')
            return