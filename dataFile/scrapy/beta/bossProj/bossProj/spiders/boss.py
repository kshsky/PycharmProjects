from __future__ import absolute_import
import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&page=1']
    url = 'https://www.zhipin.com/c101010100/?query=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&page='
    page = 1

    def parse(self, response):
        print('___parse___')
        print(response.text)
        # job_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        # job_list = response.xpath('//div[@class="job-list"]')
        job_list = response.xpath('//div[@id="main"]/div/div[3]/ul/li')
        print(job_list)
        for i in job_list:
            print(i)