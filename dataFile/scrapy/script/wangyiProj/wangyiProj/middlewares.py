# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from time import sleep

from scrapy.http import HtmlResponse


class WangyiprojDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.


    def process_request(self, request, spider):
        #每个请求都会经过这里
        print('{} ---> {}'.format(request.url,spider.flag))

        if spider.status == 1:
            #测试selenium的请求是否经过这里
            print('{}--- REQ - status --->{}'.format(request.url,spider.status))
            spider.status = 2
        return None

    def process_response(self, request, response, spider):
        #每个response都会经过这里
        print('{} ---> {}'.format(request.url,spider.flag))

        if spider.flag == 0:
            return response

        elif spider.flag == 1:
            driver = spider.driver
            #模拟浏览器发出请求
            driver.get(request.url)
            spider.status=1
            sleep(1)
            #获得返回数据
            page_text = driver.page_source
            print('{}--- RES - status --->{}'.format(request.url,spider.status))
            new_response = HtmlResponse(url=request.url,body = page_text,encoding='utf8',request = request)
            return new_response
        else:
            return response


    def process_exception(self, request, exception, spider):

        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
