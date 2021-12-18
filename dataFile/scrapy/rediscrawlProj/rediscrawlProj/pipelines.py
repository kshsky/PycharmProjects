# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RediscrawlprojPipeline:
    def process_item(self, item, spider):
        print('scrapy pipeline ---> \n', item)

        with open('./sum.txt','a+',encoding='utf8') as fp:
            fp.write(item['id']+' '+item['detailTitle']+'-'+item['detailUrl']+'\n')

        return item
