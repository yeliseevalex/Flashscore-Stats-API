import asyncio
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.scrapy_app.spiders.flashscore_spider import FlashscoreSpider

async def run_scrapy():
    loop = asyncio.get_event_loop()
    process = CrawlerProcess(get_project_settings())
    process.crawl(FlashscoreSpider)
    process.start()
