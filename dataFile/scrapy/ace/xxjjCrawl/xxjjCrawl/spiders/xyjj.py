import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class XyjjSpider(CrawlSpider):
    name = 'xyjj'
    # allowed_domains = ['www.ccc.com']
    start_urls = ['https://www.xyshjj.cn/list-1487-1489-0.html']
    #  page链接与其他链接相似度过高 rules不起作用，放弃。
    rules = (
        Rule(LinkExtractor(allow=r'">\d+</a>'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        ls = response.xpath('.//div[@class="article-list"]/div')
        print('---------')
        for i in ls:
            url = i.xpath('./div/a/@href').get()
            num = i.xpath('./div/a/text()').get()
            print(url,' - ',num)
        return item
