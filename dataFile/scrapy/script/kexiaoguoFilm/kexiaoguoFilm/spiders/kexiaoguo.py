import scrapy

class KexiaoguoSpider(scrapy.Spider):
    name = 'kexiaoguo'
    # allowed_domains = ['www.cc.com']
    # film的字幕下载
    start_urls = ['https://www.kexiaoguo.com/dianying101/1/']

    file_content_dict = {}
    base_url = 'https://www.kexiaoguo.com'
    film_name = 'mr-mrs-smith-2'
    file_path = 'F:\\PDF\\美剧字幕\\{}.pdf'.format(film_name)

    def parse(self, response):
        ls = response.xpath('.//div[@id="daohang"]/ul[1]/li')

        for i in ls:
            part_url = self.base_url + i.xpath('./p/a/@href').get()
            part_name = i.xpath('./p/a/text()').get().strip()

            print(part_name, part_url)

            yield scrapy.Request(url=part_url, callback=self.parse_detail, meta={'part_name': part_name})

    def parse_detail(self, response):
        part_name = response.meta['part_name']
        content = response.xpath('.//div[@id="neirong"]/p').get()
        c = '<h1>{}</h1>{}'.format(part_name, content)
        cc = c.replace('♥', '')
        self.file_content_dict.update({part_name[part_name.index('Part')+4:]: cc})


