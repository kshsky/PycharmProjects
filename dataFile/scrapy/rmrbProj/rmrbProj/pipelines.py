# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.images import FilesPipeline

class RmrbprojPipeline(FilesPipeline):

    item =None

    # 获取文件url
    def get_media_requests(self, item, info):
        self.item = item
        yield scrapy.Request(item['url'])

    #文件名命
    def file_path(self, request, response=None, info=None, *, item=item):
        #scrapy会重建上级目录
        name ='//'+item['day'][:-3] +'//'+item['day']+'_'+item['name']+'.pdf'
        return name

    # 下载结束，item 释放【可以去掉】
    def item_completed(self, results, item, info):
        print('---------------->','item_completed')
        return item


