import scrapy


class BigpositionSpider(scrapy.Spider):
    name = 'bigPosition'
    # allowed_domains = ['www.sss.com']
    # start_urls = ['http://webapi.cninfo.com.cn/#/']
    start_urls = ['http://webapi.cninfo.com.cn/#/thematicStatistics']

    def parse(self, response):
        # print(response.text)

        ls = response.xpath('//table[@id="contentTable"]/tbody/tr')
        for i in ls:
            categoryNo=i.xpath('./td[1]/text()').get()
            categoryName=i.xpath('./td[2]/text()').get()
            report_date=i.xpath('./td[3]/text()').get()
            bund_cover=i.xpath('./td[4]/text()').get()
            industry_scale=i.xpath('./td[5]/text()').get()
            na_ratio=i.xpath('./td[6]/text()').get()

            print(categoryNo,categoryName,report_date,bund_cover,industry_scale,na_ratio)

