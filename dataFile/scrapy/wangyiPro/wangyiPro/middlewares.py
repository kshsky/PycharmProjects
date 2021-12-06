# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response
        # print(spider.section_url_list)
        #
        # print('--- response midelleware ---')
        #
        # # 国内 https://news.163.com/domestic/
        # # 国际 https://news.163.com/world/
        # # 军事 https://war.163.com/
        # # 航空 https://news.163.com/air/
        #
        # # with open('./wangyi/domestic-b.txt', 'w', encoding='utf8') as fp:
        # #     fp.write(response.text)
        # if request.url in spider.section_url_list:
        #     driver = spider.driver
        #     print('--- middleware load ----')
        #
        #     driver.get(request.url)
        #     sleep(1)
        #     page_text = driver.page_source
        #     # with open('./wangyi/domestic-a.txt', 'w', encoding='utf8') as fp:
        #     #     fp.write(page_text.text)
        #
        #     # 实例化新的响应对象，能够满足需求，替换原来的response
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response
        # else:
        #     return response

#######################################################################
        # if 'world' in request.url or 'war' in request.url:
        #
        #     print('section : ',request.url)
        #     return response
        #
        # if 'air' in request.url:
        #     print('section : ',request.url)
        #     with open('./wangyi/air-b.txt','w',encoding='utf8') as fp:
        #         fp.write(response.text)
        #     #browse 是selenium建立的浏览器对象，可以模拟下拉操作，获取完整数据
        #     bro = spider.bro
        #
        #     print('--- middleware : modify url ----')
        #     print(request.url)
        #     bro.get(request.url)
        #     #模拟页面向下滚动加载全部页面
        #     # js = 'return document.body.scrollHeight;'
        #     # height = 0
        #     # while True:
        #     #     new_height = bro.execute_script(js)
        #     #     if new_height > height:
        #     #         bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        #     #         height = new_height
        #     #         sleep(5)
        #     #     else:
        #     #         print("滚动条已经处于页面最下方!")
        #     #         bro.execute_script('window.scrollTo(0, 0)')  # 页面滚动到顶部
        #     #         break
        #     sleep(2)
        #     # #包含动态加载的新闻数据
        #     page_text = bro.page_source
        #     with open('./wangyi/air-a.txt','w',encoding='utf8') as fp:
        #         fp.write(page_text.text)
        #     #实例化新的响应对象，能够满足需求，替换原来的response
        #     new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
        #     return new_response
        #
        # if 'domestic' in request.url:
        #
        #     print('section : ',' domestic ',  request.url)
        #
        #     with open('./wangyi/domestic-b.txt','w',encoding='utf8') as fp:
        #         fp.write(response.text)
        #
        #     bro = spider.bro
        #
        #     print('--- domestic load ----')
        #     print(request.url)
        #     bro.get(request.url)
        #     sleep(1)
        #     page_text = bro.page_source
        #     with open('./wangyi/domestic-a.txt','w',encoding='utf8') as fp:
        #         fp.write(page_text.text)
        #
        #
        #     # 实例化新的响应对象，能够满足需求，替换原来的response
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response
        #
        # return response




    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
