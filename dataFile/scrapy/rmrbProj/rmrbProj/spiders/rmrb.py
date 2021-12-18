import scrapy
from redis import Redis
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from rmrbProj.items import RmrbprojItem
import time
from scrapy.utils.project import get_project_settings
class RmrbSpider(CrawlSpider):
    name = 'rmrb'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://paper.people.com.cn/rmrb/html/2021-10/06/nbs.D110000renmrb_01.htm']

    start_urls = []

    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    year_month = str(year) + '-' + str(month)

    redis = Redis(host='192.168.10.108',port=6379)

    #构造起始url列表
    for i in range(0,day):
        dayStr =''
        if i <=8:
            dayStr +='0'+str(i+1)
        else:
            dayStr += str(i+1)
        url = 'http://paper.people.com.cn/rmrb/html/' + year_month +'/'+dayStr+'/nbs.D110000renmrb_01.htm'
        start_urls.append(url)


    rules = (
        Rule(LinkExtractor(allow=r'renmrb_\d+\.htm'), callback='parse_item'), #匹配各个板块:pageLink
    )
    base_url = 'http://paper.people.com.cn/rmrb/'
    def parse_item(self, response):

        name = response.xpath('//div[@class="paper-bot"]/p[1]/text()').get().replace(':','-')

        # ../../../ images / 2021 - 10 / 06 / 07 / rmrb2021100607.pdf
        # 从报纸首页第一版进入，tempUrl即是下一版的url
        tempUrl = response.xpath('//div[@class="paper-bot"]/p[2]/a/@href').get()

        # http: // paper.people.com.cn / rmrb / images / 2021 - 10 / 06 / 01 / rmrb2021100601.pdf
        url = self.base_url +tempUrl[tempUrl.index('images') :]
        #将爬取过的url放入redis中，使用set集合存储，
        # 放入成功-第一次放入：返回1
        # 放入失败-非第一次放入：返回0
        flag = self.redis.sadd('rmrb_url',url)
        idx = tempUrl.index(self.year_month)
        day = tempUrl[idx:idx + 10].replace('/', '-')
        if flag == 0:
            print('{} : 数据已经采集过了，无需重复采集'.format(tempUrl[idx:idx + 13]))
        else:
            print('{} : 开始采集数据 ... '.format(tempUrl[idx:idx + 13]))

            item = RmrbprojItem()
            item['name']=name
            item['day']=day
            item['url']= url

            yield item



