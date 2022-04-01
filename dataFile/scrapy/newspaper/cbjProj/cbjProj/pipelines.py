
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import FilesPipeline
class CbjprojPipeline(FilesPipeline):
    item  = None
    # Overridable Interface
    def get_media_requests(self, item, info):
        self.item = item
        url = item['url']
        yield scrapy.Request(url)

    def file_path(self, request, response=None, info=None, *, item=item):

        url = item['url']
        name = item['name']
        # ../../../images/2022-03/07/03/2445A03C.pdf
        index = url.index('images')+7
        time = url[index:index+10].replace('/','-')
        name = time+'_'+item['name']
        path = '//CBJ//{}//{}.pdf'.format(time[:-3],name)
        print(path)

        return path
