# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import os
class FemmefatalesPipeline:
    def open_spider(self,spider):
        cur_path = os.getcwd()
        os.mkdir('No Time to Die')


    def process_item(self, item, spider):

        file_name = item['name']+'_'+str(item['page'])
        content = item['content']
        with open('./'+item['name']+'/'+file_name+'.txt','w',encoding='utf8') as fp:
            fp.write(content)
        return item
