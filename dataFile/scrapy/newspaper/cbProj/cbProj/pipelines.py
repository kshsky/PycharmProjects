from itemadapter import ItemAdapter
from scrapy.pipelines.images import FilesPipeline
import scrapy
import datetime
class CbprojPipeline(FilesPipeline):

    item =None

    # 获取文件url
    def get_media_requests(self, item, info):
        self.item = item
        yield scrapy.Request(item['url'])

    #文件名命
    def file_path(self, request, response=None, info=None, *, item=item):

        name ='//'+item['dirname'] +'//'+item['name']

        return name

    # 下载结束，item 释放【可以去掉】
    def item_completed(self, results, item, info):
        print(datetime.datetime.now(),item['name'])
        return item
