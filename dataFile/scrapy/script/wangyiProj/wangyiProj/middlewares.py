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
        spider.logger.info('REQ >>> %s  - %s' %(request.url,spider.flag))
        spider.flag = 4
        return None

    def process_response(self, request, response, spider):
        spider.logger.info('RES >>> %s - %s' % (request.url, spider.flag))

        if spider.flag == 5:
            return response

        if request.url in spider.section_url_list:
            driver = spider.driver
            driver.get(request.url)
            sleep(1)
            page_text = driver.page_source
            spider.flag=1
            new_response = HtmlResponse(url=request.url,body = page_text,encoding='utf8',request = request)
            return new_response



        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
