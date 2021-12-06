# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import shutil
import os
class WangyiprojPipeline:


    def open_spider(self,spider):
        shutil.rmtree('txt2')
        os.mkdir('txt2')
        print('\n directory created successfully ... \n')
    def process_item(self, item, spider):

        spider.logger.info(' item>>>\n %s'%(item))

        return item
