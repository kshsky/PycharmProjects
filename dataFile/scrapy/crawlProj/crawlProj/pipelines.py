# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# from ..items import CrawlprojItem,CrawlprojDetailItem
class CrawlprojPipeline:
    def process_item(self, item, spider):

        if item.__class__.__name__ =='CrawlprojItem':
            print('CrawlprojItem ---> \n',item)

        if item.__class__.__name__ =='CrawlprojDetailItem':
            print('CrawlprojDetailItem ---> \n',item)

        return item
