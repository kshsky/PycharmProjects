import scrapy


class WuyouSpider(scrapy.Spider):
    name = 'wuyou'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']
    start_urls = ['https://www.zhipin.com/c101010100/?query=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&page=1']
    url_b ='https://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,'
    url_a ='.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    page = 1
    def parse(self, response):
        print(response)
        listx = response.xpath('//div[@class="j_result"]/div/div[2]/div[4]/div/div')
        for x in listx:
            title= x.xpath('./div/a/p/span[1].text')

            print(title)
