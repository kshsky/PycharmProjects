import scrapy

# 一月出生的人 1日 ./1.html
def getMonth(s):
    month = s[:s.index('月')]
    if month =='一':
        return '01'
    elif month =='二':
        return '02'
    elif month =='三':
        return '03'
    elif month =='四':
        return '04'
    elif month =='五':
        return '05'
    elif month =='六':
        return '06'
    elif month =='七':
        return '07'
    elif month =='八':
        return '08'
    elif month =='九':
        return '09'
    elif month =='十':
        return '10'
    elif month =='十一':
        return '11'
    elif month =='十二':
        return '12'
    return None
def getDay(s):
    day = s[:s.index('日')]
    if len(day)==1:
        return '0'+day
    else:
        return day
from ..items import BirthdayprojItem
class BirthdaySpider(scrapy.Spider):
    name = 'birthday'
    # allowed_domains = ['www.com.com']
    start_urls = ['https://birth.911cha.com/']
    columnList = ['date','birthdayUrl','huaUrl','shuUrl']
    tableName = 'bithdaySecret'
    base_url ='https://birth.911cha.com/'

    def parse(self, response):
        # print(response.text)
        ls = response.xpath('//div[@class="leftbox"]/div[3]/div[2]/table')
        # print(ls)
        for i in ls:
            # print(i)
            month = i.xpath('./caption/text()').get()
            strMonth = getMonth(month)
            date_tr = i.xpath('./tbody/tr')
            for j in date_tr:
                date_td = j.xpath('./td')
                for td in date_td:
                    date = td.xpath('./a/text()').get()
                    strDate = getDay(date)
                    dateUrl = td.xpath('./a/@href').get()
                    linkUrl = dateUrl[dateUrl.index('/')+1:]
                    birthdayUrl = self.base_url + linkUrl
                    huaUrl = self.base_url +'hua_'+ linkUrl
                    shuUrl = self.base_url +'shu_'+ linkUrl

                    item = BirthdayprojItem()
                    item['date']=strMonth+strDate
                    item['birthdayUrl']=birthdayUrl
                    item['huaUrl']=huaUrl
                    item['shuUrl']=shuUrl

                    print(strMonth,strDate,birthdayUrl,huaUrl,shuUrl)
                    yield item
