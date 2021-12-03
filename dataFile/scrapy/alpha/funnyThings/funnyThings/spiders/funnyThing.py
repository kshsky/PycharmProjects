import scrapy


class FunnythingSpider(scrapy.Spider):
    name = 'funnyThing'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.tianyancha.com/search?base=bj']

    def parse(self, response):
        #作者名称+段子内容
        # xpath方法返回的是Selector对象，里面是xpath值和data值,extract()可以读取data值
        df = {}
        columns_list=[]
        data_list=[]
        div_list = response.xpath('//div[@class="result-list sv-search-container"]/div')
        for i in div_list:
            col_list = []
            record_list = []
            name = i.xpath('./div/div[1]/div[2]/div[2]/text()')[0].extract()
            img = i.xpath('./div/div[2]/div/div[2]/img/@data-src')[0].extract()
            col_list.append('名称')
            record_list.append(name)
            col_list.append('img')
            record_list.append(img)
            #详情
            normal = i.xpath('./div/div[3]/div[1]/div/text()')[0].extract()
            print(normal)
            col_list.append('状态')
            record_list.append(normal)
            # tag = i.xpath('./div/div[3]/div[2]/div')
            tag = i.xpath('./div/div[3]/div[2]/div')
            tag_list = tag.xpath('string(.)').extract()
            print(';'.join(tag_list))

            col_list.append('标签')
            record_list.append(';'.join(tag_list))

            info_legalPersonName_title  = i.xpath('./div/div[3]/div[3]/div[1]/text()')
            info_legalPersonName_name  = i.xpath('./div/div[3]/div[3]/div[1]/a/text()')

            if len(info_legalPersonName_title)==0:
                info_legalPersonName_k =' '
            else:
                info_legalPersonName_k = info_legalPersonName_title[0].get()
            if len(info_legalPersonName_name)==0:
                info_legalPersonName_v=' '
            else:
                info_legalPersonName_v = info_legalPersonName_name[0].get()

            col_list.append(info_legalPersonName_k)
            record_list.append(info_legalPersonName_v)

            print(info_legalPersonName_k,info_legalPersonName_v)

            info_capital_title  = i.xpath('./div/div[3]/div[3]/div[2]/text()')[0].extract()
            info_capital_name  = i.xpath('./div/div[3]/div[3]/div[2]/span/text()')[0].extract()

            col_list.append(info_capital_title)
            record_list.append(info_capital_name)

            info_create_key  = i.xpath('./div/div[3]/div[3]/div[3]/text()')[0].extract()
            info_create_value  = i.xpath('./div/div[3]/div[3]/div[3]/span/text()')[0].extract()
            print(info_create_key,info_create_value)

            col_list.append(info_create_key)
            record_list.append(info_create_value)
            #联系方式
            info_telephone_key = i.xpath('./div/div[3]/div[4]/div[1]/span[1]/text()')
            info_telephone_value = i.xpath('./div/div[3]/div[4]/div[1]/span[2]/text()')
            if len(info_telephone_key) == 0:
                info_telephone_k = ' '
            else:
                info_telephone_k = info_telephone_key[0].get()
            if len(info_telephone_value) == 0:
                info_telephone_v = ' '
            else:
                info_telephone_v = info_telephone_value[0].get()
            col_list.append(info_telephone_k)
            record_list.append(info_telephone_v)
            print(info_telephone_k, info_telephone_v)

            info_email_key = i.xpath('./div/div[3]/div[4]/div[2]/span[1]/text()')
            info_email_value = i.xpath('./div/div[3]/div[4]/div[2]/span[2]/text()')

            if len(info_email_key) == 0:
                info_email_k = ' '
            else:
                info_email_k = info_email_key[0].get()
            if len(info_email_value) == 0:
                info_email_v = ' '
            else:
                info_email_v = info_email_value[0].get()
            print(info_email_k, info_email_v)
            col_list.append(info_email_k)
            record_list.append(info_email_v)

            info_address_key = i.xpath('./div/div[3]/div[5]/div/span[1]/text()')
            info_address_value = i.xpath('./div/div[3]/div[5]/div/span[2]/text()')

            if len(info_address_key) == 0:
                info_address_k = ' '
            else:
                info_address_k = info_address_key[0].get()
            if len(info_address_value) == 0:
                info_address_v = ' '
            else:
                info_address_v = info_address_value[0].get()
            print(info_address_k, info_address_v)
            col_list.append(info_address_k)
            record_list.append(info_address_v)
            columns_list.append(col_list)
            data_list.append(record_list)
        df.update({'column':columns_list[0]})
        df.update({'data':data_list})
        return df