import scrapy


class AceSpider(scrapy.Spider):
    name = 'ace'
    #允许的域名：用来限定start_urls中哪些url可以进行请求发送
    # allowed_domains accepts only domains, not URLs.Ignoring URL entry  http: // www.mi.com / in allowed_domains.
    allowed_domains = ['http://www.baidu.com']
    #起始的url列表：该列表中存放的url会被srapy自动进行请求的发送
    #start_urls必须以http://开头
    start_urls = ['http://www.sogou.com/','http://www.bilibili.com','http://www.baidu.com']

    #用于数据解析，response参数表示请求成功之后对应的响应对象。
    def parse(self, response):
        print(response)
        print('==================')
