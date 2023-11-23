import scrapy
from ..page_objects.pages import CarPage
from cars.items import CarItem
from scrapy.loader import ItemLoader
from scrapy_playwright.page import PageMethod
import re
from scrapy import signals
import pandas as pd


class Cars(scrapy.Spider):
    name = 'cars_spider'
    playwright_args = {
        "playwright": True,
        "playwright_include_page": True,
        "playwright_context_kwargs": {
            "ignore_https_errors": True,
        },
    }

    def start_requests(self):
        for url in self.links:
            if 'autotrader.com' in url:
                match = re.search("\d{9}", url)
                if match:
                    url = f'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId={match.group()}'
                    yield scrapy.Request(url, callback=self.parse_car)
            elif 'cargurus.com' in url:
                match = re.search("\d{9}", url)
                if match:
                    url = f"https://www.cargurus.com/Cars/detailListingJson.action?inventoryListing={match.group()}"
                    yield scrapy.Request(url, callback=self.parse_car)
            elif 'carsandbids.com' in url:
                yield scrapy.Request(url, callback=self.parse_car, meta={
                **self.playwright_args,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "//div[@class='quick-facts']"),
                ]
            })
            else:
                yield scrapy.Request(url, callback=self.parse_car)


    async def parse_car(self, response, page: CarPage):
        item = await page.to_item()
        item['source_page'] = response.url
        loader = ItemLoader(item=CarItem())
        for k, v in item.items():
            loader.add_value(k, v)
        yield loader.load_item()


    async def close_context_on_error(self, failure):
        page = failure.request.meta.get("playwright_page")
        if page:
            await page.close()


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Cars, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        return spider


    def spider_opened(self, spider):
        df = pd.read_csv("urls.csv")
        self.links = [row['link'] for idx, row in df.iterrows()]
