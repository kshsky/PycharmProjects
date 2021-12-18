# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import shutil
import os

class WangyiproPipeline:

    def open_spider(self,spider):

        if os.path.exists('txt'):
            shutil.rmtree('txt')
        os.mkdir('txt')

        print(' ctarted ok ')



    def process_item(self, item, spider):
        print('----pipeline  item ------------------')
        print(item)
        return item

    def close_spider(self,spider):
        print('=========pipe spider close================')

