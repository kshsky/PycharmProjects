import time
import random
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class XiaoprojDownloaderMiddleware:

    def __init__(self):

        print("初始化浏览器")
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "normal"
        self.driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe',
                                       desired_capabilities = desired_capabilities)


    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):

        # if spider.status ==1:
        #     return response
        self.driver.get(request.url)
        # time.sleep(random.randint(10,22))
        source = self.driver.page_source
        # self.driver.close()
        #获取页面的源码
        response = HtmlResponse(url=request.url,body=source,request=request,encoding='utf-8')
        # Response 对象用来描述一个HTTP响应
        return response
        # 这样我们就获取到了所有的信息，并返回response
        # import time
        # from scrapy.http import HtmlResponse
        # from selenium import webdriver
        # import random