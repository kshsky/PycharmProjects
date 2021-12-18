BOT_NAME = 'wuyouProj'

SPIDER_MODULES = ['wuyouProj.spiders']
NEWSPIDER_MODULE = 'wuyouProj.spiders'

ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'

DEFAULT_REQUEST_HEADERS = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
   'Accept-Language': 'en',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

DOWNLOAD_DELAY = 3

COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
   'wuyouProj.middlewares.WuyouprojDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
   'wuyouProj.pipelines.WuyouprojPipeline': 300,
}


