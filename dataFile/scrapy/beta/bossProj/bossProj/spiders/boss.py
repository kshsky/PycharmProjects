from __future__ import absolute_import
import scrapy

from ..items import BossprojItem
#############################################################
from datetime import datetime

def checkNone(target):
    if target is None:
        return '-'
    return target

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xx.com']
    #数据挖掘
    start_urls = ['https://www.zhipin.com/c101010100-p100509/?query=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&page=1']
    #数据分析
    # start_urls = ['https://www.zhipin.com/c101010100-p100509/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page=1']
    #爬虫
    # start_urls = ['https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page=1']
    model_url='https://www.zhipin.com/c101010100-p100509/?query=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&page={}'
    # model_url='https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page={}'
    page = 1
    day = datetime.now().date()
    tableName = 'boss_crawl' + str(day).replace('-', '_')
    columnList = ['job', 'jobTag', 'jobArea', 'salary', 'requirement', 'company', 'companyTag', 'jobDesc']
    def parse(self, response):

        ls = response.xpath("//div[@class='job-list']/ul/li")
        for i in ls:

            job = i.xpath(".//span[@class='job-name']/a/text()").get()
            jobTag =i.xpath('.//div[@class="tags"]').xpath('normalize-space(string(.))').get().replace(' ',';')
            jobArea = i.xpath('.//span[@class="job-area"]/text()').get()

            salary=i.xpath('.//div[@class="job-limit clearfix"]/span/text()').get()
            requirement=i.xpath('.//div[@class="job-limit clearfix"]/p').xpath('string(.)').get()

            company=i.xpath('.//div[@class="company-text"]/h3/a/text()').get()
            companyTag=i.xpath('.//div[@class="company-text"]/p').xpath('string(.)').get()
            jobDesc=i.xpath('.//div[@class="info-desc"]/text()').get()

            item = BossprojItem()
            item['job']=checkNone(job)
            item['jobTag']=checkNone(jobTag)
            item['jobArea']=checkNone(jobArea)
            item['salary']=checkNone(salary)
            item['requirement']=checkNone(requirement)
            item['company']=checkNone(company)
            item['companyTag']=checkNone(companyTag)
            item['jobDesc']=checkNone(jobDesc)

            yield item

        print('--- {} ---'.format(self.page))
        self.page +=1
        # 获取下一页的地址
        next_url = self.model_url.format(self.page)
        if self.page <= 11:
            print("下一页地址：", next_url)
            yield scrapy.Request(next_url,callback=self.parse)
        else:
            return
