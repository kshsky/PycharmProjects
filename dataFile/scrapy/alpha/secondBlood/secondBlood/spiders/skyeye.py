import scrapy
from secondBlood.items import SecondbloodItem


class SkyeyeSpider(scrapy.Spider):
    name = 'skyeye'
    # allowed_domains = ['www.skyeye.com']
    start_urls = ['https://www.tianyancha.com/search?base=bj']

    def parse(self, response):

        # xpath方法返回的是Selector对象，里面是xpath值和data值,extract()可以读取data值

        div_list = response.xpath('//div[@class="result-list sv-search-container"]/div')

        for i in div_list:

            name = i.xpath('./div/div[1]/div[2]/div[2]/text()')[0].extract()
            img = i.xpath('./div/div[2]/div/div[2]/img/@data-src')[0].extract()

            # 详情
            normal = i.xpath('./div/div[3]/div[1]/div/text()')[0].extract()

            tagOri = i.xpath('./div/div[3]/div[2]/div')
            tag_list = tagOri.xpath('string(.)').extract()
            tag = ';'.join(tag_list)
            #legalPerson
            legalPersonOri = i.xpath('./div/div[3]/div[3]/div[1]/a/text()')

            if len(legalPersonOri) == 0:
                legalPerson = ' '
            else:
                legalPerson = legalPersonOri[0].get()

            #capital
            capital = i.xpath('./div/div[3]/div[3]/div[2]/span/text()')[0].extract()

            createTime = i.xpath('./div/div[3]/div[3]/div[3]/span/text()')[0].extract()

            # 联系方式
            telephoneOri = i.xpath('./div/div[3]/div[4]/div[1]/span[2]/text()')

            if len(telephoneOri) == 0:
                telephone = ' '
            else:
                telephone = telephoneOri[0].get()

            emailOri = i.xpath('./div/div[3]/div[4]/div[2]/span[2]/text()')


            if len(emailOri) == 0:
                email = ' '
            else:
                email = emailOri[0].get()

            addressOri = i.xpath('./div/div[3]/div[5]/div/span[2]/text()')

            if len(addressOri) == 0:
                address = ' '
            else:
                address = addressOri[0].get()
            itemStr = name + ',' + img + ',' + normal + ',' + tag + ',' + legalPerson + ',' + capital + ',' \
                      + createTime + ',' + telephone + ',' + email + ',' + address + '\n'
            print(itemStr)
            item= SecondbloodItem()

            item['name']=name
            item['img']=img
            item['normal']=normal
            item['tag']=tag
            item['legalPerson']=legalPerson
            item['capital']=capital
            item['createTime']=createTime
            item['telephone']=telephone
            item['email']=email
            item['address']=address
            # break
            #将item提交给管道
            yield item
