BOT_NAME = "flashscore_bot"
SPIDER_MODULES = ["scrapy_app.spiders"]
NEWSPIDER_MODULE = "scrapy_app.spiders"
LOG_LEVEL = "INFO"
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    "scrapy_app.pipelines.FlashscorePipeline": 300,
}