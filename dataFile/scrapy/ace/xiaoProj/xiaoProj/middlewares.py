import time
import random
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class XiaoprojDownloaderMiddleware:

    def __init__(self):

        print("初始化浏览器")
        # - desired_capabilities - A dictionary of capabilities to request when starting the browser session. Required parameter.
        # driver.get(url)
        # 方法要根据desired_capabilities的pageLoadStrategy字段的值，确定执行结束的时机：
        # （1）NONE：html下载完成，不等待解析完成即返回；
        # （2）EAGER：要等待整个dom树加载完成，即DOMContentLoaded这个事件完成，仅对html的内容进行下载解析；
        # （3）NORMAL: 等待整个界面加载完成（指对html和子资源的下载与解析, 如JS文件，图片等，不包括ajax）.

        # get直接返回，不再等待界面加载完成
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