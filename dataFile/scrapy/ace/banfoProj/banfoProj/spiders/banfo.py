import scrapy

from ..items import BanfoprojItem
class BanfoSpider(scrapy.Spider):
    name = 'banfo'
    start_urls = ['https://www.toutiao.com/c/user/token/MS4wLjABAAAA5X0VBPDBZMEMapObds7t3Z_5K6V61i3zNDYgSd6uPlM/?source=author_home&tab=article']
    columnList = ['title','url','id','public']
    tableName ='banfo'
    def parse(self, response):

        ls = response.xpath('//div[@class="feed-card-article-r"]')
        for i in ls:
            url_ori= i.xpath('./div[@class="feed-card-cover"]/a/@href').get()
            title= i.xpath('./div[@class="feed-card-cover"]/a/@title').get()
            clean_url=url_ori[:-1]
            id = clean_url[clean_url.rindex('/')+1:]
            item = BanfoprojItem()
            item['id']=id
            item['title']=title
            item['url']=clean_url
            item['public']='-'


            print(title,clean_url)
            yield item