import scrapy

from ..items import SinglepageItem
class SingleSpider(scrapy.Spider):
    name = 'single'
    # allowed_domains = ['www.ccc.com']
    base_url = 'https://chriszheng.science/pua-books/'
    start_urls = []
    start_urls.append(base_url)
    def parse(self, response):
        #/html/body/pre
        # print(response.text)
        ls = response.xpath('.//pre/a[position()>1]')
        for i in ls:
            url = i.xpath('./@href').get()
            name = i.xpath('./text()').get()

            print(name,url)

            item = SinglepageItem()
            item['url']=self.base_url + url
            item['name']=name

            yield item
