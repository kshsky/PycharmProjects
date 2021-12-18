import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from filmProj.items import FilmItem
class FilmSpider(CrawlSpider):
    name = 'film'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.xuan131.top/search.asp?page=3&searchword=%C9%B4%C9%B4%D4%AD%B0%D9%BA%CF&searchtype=-1']

    rules = (
        Rule(LinkExtractor(allow=r'\?page=\d+&searchword='), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/N/\d+\.html'), callback='parse_detail'),
    )

    def parse_item(self, response):
        print('------------------')

        itemlist = response.xpath('//div[@class="channel-content"]/ul/li')
        for i in itemlist:

            name = i.xpath('./h2/a/text()').get().strip()
            dUrl = i.xpath('./h2/a/@href').get()
            item = FilmItem()
            item['name']=name
            url = 'https://www.xuan131.top'+dUrl
            item['url']=url
            yield scrapy.Request(url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self, response):
        item = response.meta['item']
        print(response.url)
        n = response.url.index('N')
        url = response.url[n-1:]

        section = response.xpath('//div[@class="map l"]//a[2]/text()').get()
        detailName = response.xpath('//div[@class="title"]/h1/text()').get()
        actor = response.xpath('//div[@class="alex"]/li[1]/a/text()').get()
        designation = response.xpath('//div[@class="alex"]/li[2]/text()').get()
        language = response.xpath('//div[@class="alex"]/li[4]/text()').get()
        typeOri = response.xpath('//div[@class="alex"]/li[6]')
        type = typeOri.xpath('normalize-space(string(.))').get()
        new = ';'.join(type.split())

        item ['section']=section
        item ['detailName']=detailName
        item ['actor']=actor if actor is not None else '-'
        item ['designation']=designation
        item ['language']=language
        item ['type']=new
        item ['detailUrl']=url

        print(section,detailName,actor,designation,language,type,url)

        yield item
