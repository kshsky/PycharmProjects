# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep
# Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
class WangyiproSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        print('spiderMiddleware --- spider_open >>>  flag:{}'.format(spider.flag))
class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):
        #scrapy的每个请求都会经过这里
        print('url:{} status:{} flag:{}'.format(request.url,spider.status,spider.flag))

        if spider.status == 1:
            #测试selenium的请求是否经过这里
            print('REQ selenium >>> url:{} status:{} flag:{}'.format(request.url, spider.status, spider.flag))
            spider.status = 2
        return None
    def process_response(self, request, response, spider):
        #scrapy的每个response都会经过这里
        print('at the beginning of process_response >>> url:{} status:{} flag:{}'.format(request.url, spider.status, spider.flag))

        if spider.flag == 0:
            return response

        elif spider.flag == 1:
            driver = spider.driver
            #模拟浏览器发出请求
            spider.status = 1
            print('before selenium >>> url:{} status:{} flag:{}'.format(request.url, spider.status, spider.flag))
            driver.get(request.url)
            sleep(1)
            #获得返回数据
            page_text = driver.page_source
            print('RES >>> url:{} status:{} flag:{}'.format(request.url, spider.status, spider.flag))
            # 实例化新的响应对象，能够满足需求，替换原来的response
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        elif spider.flag == 2:
            print('------------------>',spider.flag)
            driver = spider.driver
            driver.get(request.url)
            #模拟页面向下滚动加载全部页面
            js = 'return document.body.scrollHeight;'
            height = 0
            while True:
                new_height = driver.execute_script(js)
                if new_height > height:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    height = new_height
                    sleep(5)
                else:
                    print("滚动条已经处于页面最下方!")
                    driver.execute_script('window.scrollTo(0, 0)')  # 页面滚动到顶部
                    break
            sleep(2)
            # #包含动态加载的新闻数据
            page_text = driver.page_source
            with open('./wangyi/air-a.txt', 'w', encoding='utf8') as fp:
                fp.write(page_text.text)
                # 实例化新的响应对象，能够满足需求，替换原来的response
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        else:
            return response


    def process_exception(self, request, exception, spider):

        pass
