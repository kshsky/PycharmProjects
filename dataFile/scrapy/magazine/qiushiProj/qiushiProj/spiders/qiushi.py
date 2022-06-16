import scrapy
import re

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.qiushi.com']

    #1
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-01/01/c_1128220424.htm']
    #2
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-01/16/c_1128261564.htm']
    #3
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-02/01/c_1128312697.htm']
    #4
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-02/16/c_1128367748.htm']
    #5
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-03/01/c_1128420157.htm']
    #6
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-03/16/c_1128467709.htm']
    #7
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-04/01/c_1128515384.htm']
    #8
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2022-04/16/c_1128558335.htm']
    #2021
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-01/01/c_1126935900.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-01/16/c_1126985598.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-02/01/c_1127044358.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-02/16/c_1127089890.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-03/01/c_1127146577.htm']

    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-03/16/c_1127209116.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-04/01/c_1127274774.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-04/16/c_1127330584.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-05/01/c_1127390111.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-05/16/c_1127446788.htm']

    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-06/01/c_1127509134.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-06/16/c_1127560998.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-07/03/c_1127618951.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-07/16/c_1127657515.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2021-08/01/c_1127715942.htm']

    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-08/16/c_1127760159.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-09/01/c_1127810348.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-09/16/c_1127863680.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-10/01/c_1127915744.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-10/16/c_1127960465.htm']

    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-11/01/c_1128014752.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-11/16/c_1128064222.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-12/01/c_1128111028.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2021-12/16/c_1128160977.htm']

    #2020总目录
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2020-01/01/c_1125412076.htm']
    # 各期
    start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-01/01/c_1125402910.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-01/16/c_1125459004.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-02/01/c_1125497464.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-02/16/c_1125572895.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-03/01/c_1125641590.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-03/16/c_1125710486.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-04/01/c_1125791649.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-04/16/c_1125858205.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-05/01/c_1125923760.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-05/16/c_1125990062.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-06/01/c_1126055626.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-06/16/c_1126112093.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-07/01/c_1126171718.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-07/16/c_1126234238.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-08/01/c_1126306005.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-08/30/c_1126365823.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-09/01/c_1126430289.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-09/16/c_1126495051.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-10/01/c_1126556694.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-10/16/c_1126614191.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-11/01/c_1126681992.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-11/16/c_1126739014.htm']
    #
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2020-12/01/c_1126799174.htm']
    # start_urls = ['http://www.qstheory.cn/dukan/qs/2014/2020-12/16/c_1126857096.htm']
    magazine={}
    filepath='F:\PDF\GOV\magazine/求是2020/'
    filename = ''
    content=''


    def parse(self, response):
        '''
        #年度总目录
        ls = response.xpath('.//div[@class="highlight"]//p[position()!=last()]')
        # print(ls)
        yearList=[]
        for i in ls:
            name = i.xpath('string(.)').get()
            url = i.xpath('.//a/@href').get()
            yearList.append([url])
            print(name,url)
        print(yearList)
        '''
        #2022+2021
        # ls = response.xpath('.//div[@class="highlight"]//p[position()>3][position()<last()-1]')
        #2020
        ls = response.xpath('.//div[@class="highlight"]//p[position()>2][position()<last()-2]')
        # 2020年
        #<h1>《求是》2020年第1期</h1>
        name = response.xpath('.//h1/text()').get().strip()
        #2021 + 2022
        # name = response.xpath('.//h1/text()').get().strip()[:-2]
        pubtime = response.xpath('.//div[@class="inner"]//span[@class="pubtime"]/text()').get().strip()[:10]

        print(name,pubtime)

        self.filename=pubtime+'-'+name

        k=0
        for i in ls:
            k+=1
            item = i.xpath('string(.)').get().replace('/','-').replace(' ','').strip()
            url = i.xpath('.//a/@href').get()
            print(item,url)
            # 序号和文章题目绑定
            yield scrapy.Request(url =url,callback=self.parse_item,meta={'title':(k,item)})

    def parse_item(self,response):

        item = response.meta['title']

        content = response.xpath('.//div[@class="clipboard_text"]').get()

        #照片链接替换
        url = response.url
        baseUrl = url[: url.rindex('/')+1]
        newUrl = 'src="'+baseUrl
        content = re.sub(r'(src="?)',newUrl,content)
        content = re.sub(r'(face="\w{2}")', 'face="FangSong"', content)
        self.magazine[item[0]] = '<h1>{}</h1>{}'.format(item[1],content)

        print('-----------------------------------> ',item)







