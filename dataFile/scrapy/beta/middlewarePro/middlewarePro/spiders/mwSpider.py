import scrapy


class MwspiderSpider(scrapy.Spider):
    name = 'mwSpider'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://ip.yqie.com/']

    def parse(self, response):
        page_text = response.text

        with open('./ip.html','w',encoding='utf8') as fp:
            fp.write(page_text)
