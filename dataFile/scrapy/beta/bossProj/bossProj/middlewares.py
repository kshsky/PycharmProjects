import random
import time
from scrapy.http import HtmlResponse
from selenium import webdriver

class BossprojDownloaderMiddleware:

    def __init__(self):
        print("初始化浏览器")
        self.driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe')

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):

        self.driver.get(request.url)

        time.sleep(random.randint(5,10))

        source = self.driver.page_source
        #获取页面的源码
        response = HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')
        # Response 对象用来描述一个HTTP响应
        return response
        # 这样我们就获取到了所有的信息，并返回response


