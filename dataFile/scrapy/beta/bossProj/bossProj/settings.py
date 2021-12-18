BOT_NAME = 'bossProj'

SPIDER_MODULES = ['bossProj.spiders']
NEWSPIDER_MODULE = 'bossProj.spiders'

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
   'bossProj.middlewares.BossprojDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
   'bossProj.pipelines.BossprojPipeline': 300,
}
