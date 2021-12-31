import random
import time
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class BirthdayprojDownloaderMiddleware:

    def __init__(self):

        print("初始化浏览器")
        desired_capabilities = DesiredCapabilities.CHROME
        # normal :  等待整个界面加载完成（指对html和子资源的下载与解析, 如JS文件，图片等，不包括ajax
        desired_capabilities["pageLoadStrategy"] = "normal"
        self.browser = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe',
                                       desired_capabilities = desired_capabilities)


    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):

        # if spider.status ==1:
        #     return response
        print(request.url)
        self.browser.get(request.url)

        # page = 0
        # while True:
        #     page +=1
        #     #滚动到底部
        #     print('----------{}-------------'.format(page))
        #     time.sleep(1)
        #     # scroll 到指定位置
        #     self.browser.execute_script('window.scrollTo(0,{})'.format(0))
        #     time.sleep(3)
        #     self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        #     time.sleep(2)
        #     newHeight = self.browser.execute_script("return document.body.scrollHeight")
        #     self.browser.execute_script('window.scrollTo(0,{})'.format(newHeight+100))
        #
        #     print('newHeight------------> ',newHeight)
        #     stopElem = self.browser.find_elements_by_xpath('//div[@class="profile-feed-no-more show"]/p')
        #     if len(stopElem) == 1:
        #         # '无更多内容'
        #         text = stopElem[0].text
        #         self.browser.execute_script("arguments[0].scrollIntoView();", stopElem[0])  # 拖动到可见的元素去
        #         newHeight = self.browser.execute_script("return document.body.scrollHeight")
        #         print('close newHeight---------> ', newHeight)
        #         print('\n\n\n--- {} ---\n\n\n\n\n'.format(text))
        #         break

        source = self.browser.page_source
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
