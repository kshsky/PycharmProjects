import time
from scrapy.http import HtmlResponse
from selenium import webdriver
import random
class XiaoprojDownloaderMiddleware:

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):

        # if spider.status ==1:
        #     return response
        driver = spider.driver
        driver.get(request.url)

        time.sleep(random.randint(10,22))
        # 我们等待5秒钟，让其加载
        source = driver.page_source
        #获取页面的源码
        response = HtmlResponse(url=request.url,body=source,request=request,encoding='utf-8')
        # Response 对象用来描述一个HTTP响应
        return response
        # 这样我们就获取到了所有的信息，并返回response
# import time
# from scrapy.http import HtmlResponse
# from selenium import webdriver
# import random