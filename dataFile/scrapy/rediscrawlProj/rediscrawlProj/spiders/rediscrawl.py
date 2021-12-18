from __future__ import absolute_import

from rediscrawlProj.items import RediscrawlprojItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider

# from dataFile.scrapy.rediscrawlProj.rediscrawlProj.items import RediscrawlprojItem
# 普通爬虫父类：scrapy.Spider
# 自动爬虫父类：CrawlSpider
# 分布式爬虫父类：RedisCrawlSpider
# class RediscrawlSpider(CrawlSpider):
class RediscrawlSpider(RedisCrawlSpider):
    name = 'rediscrawl'
    # allowed_domains = ['www.xx.com']
    # start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=6']
    #在redis的客户端执行
    # lpush url_queue https://wz.sun0769.com/political/index/politicsNewest?id=1&page=6

    #项目执行： scrapy runspider rediscrawl.py
    redis_key = 'url_queue'

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print('response.url : {}'.format(response.url))

        #xpath表达式不能出现tbody否则不能正确定位
        ls = response.xpath('//ul[@class="title-state-ul"]/li')
        for i in ls:
            id = i.xpath('./span[1]/text()').get()
            detailUrl = i.xpath('./span[3]/a/@href').get()
            detailTitle = i.xpath('./span[3]/a/text()').get()
            print('id:{} , detailTitle:{} , detailUrl:{}'.format(id,detailTitle,detailUrl))
            item = RediscrawlprojItem()
            item['id']=id
            item['detailUrl']=detailUrl
            item['detailTitle']=detailTitle

            yield item
