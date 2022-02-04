import time
import random
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class StockprojDownloaderMiddleware:

    def __init__(self):

        print("初始化浏览器")
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "normal"
        self.driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe',
                                       desired_capabilities = desired_capabilities)

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):

        self.driver.get(request.url)
        time.sleep(10)
        # 清楚默认显示
        the_elem_1 = self.driver.find_element_by_xpath('//div[@class="nav-row level-1"]/div/div/ul/li[@data-pos="1"]')
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", the_elem_1, 'class', 'has-child')
        the_elem_2 = self.driver.find_element_by_xpath('//div[@class="nav-row level-2"]/div/div/ul[@data-pos="1"]')
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", the_elem_2, 'class', 'hide')
        # 基金报表
        the_elem=self.driver.find_element_by_xpath('//div[@class="nav-row level-1"]/div/div/ul/li[@data-pos="a"]')
        # has-child
        print(the_elem.get_attribute('class'))
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", the_elem, 'class', 'has-child active')
        print(the_elem.get_attribute('class'))
        #显示二级主题
        the_elem_ul2=self.driver.find_element_by_xpath('//div[@class="nav-row level-2"]/div/div/ul[@data-pos="a"]')
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", the_elem_ul2, 'class', '')
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", the_elem_ul2, 'style', '"left: 0px;"')
        time.sleep(2)
        the_elem_li=self.driver.find_element_by_xpath('//div[@class="nav-row level-2"]/div/div/ul[@data-pos="a"]/li[4]')
        print(the_elem_li.get_attribute('class'))
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", the_elem_li, 'class', 'active')
        print(the_elem_li.get_attribute('class'))
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="nav-row level-2"]/div/div/ul[@data-pos="a"]/li[@data-pos="a4"]/a').click()
        # year=['2017','2018','2019','2020','2021']
        time.sleep(5)

        year_sele = self.driver.find_element_by_id('seee1')
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", year_sele, 'value', '2017')

        # report_type_sele = self.driver.find_element_by_xpath('//div[@class="box-filter filter-condition condition1"]/select')
        # report_type_sele.send_keys('年报')

        search_button = self.driver.find_element_by_xpath('//button[@class="box-filter stock-search btn thematicStatisticsBtn btn-primary"]')
        search_button.click()
        #
        page_record_elem = self.driver.find_element_by_xpath('//button[@class="btn btn-default dropdown-toggle"]/span[1]')
        # page_record_elem.send_keys('20')
        # js = "document.getElementByClass('page-size').innerHTML('20')"
        # self.driver.execute_script(js)
        print(page_record_elem.xpath('./text()').get())
        time.sleep(10)
        source = self.driver.page_source
        response = HtmlResponse(url=request.url,body=source,request=request,encoding='utf-8')
        return response
