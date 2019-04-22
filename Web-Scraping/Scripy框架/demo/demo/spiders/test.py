# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem


class TestSpider(scrapy.Spider):
    # 唯一必须参数，爬虫名
    name = 'test'
    # 界定url，只有该url域下的url才会被爬取
    allowed_domains = ['xinli001.com']
    base_url='https://www.xinli001.com/info?is_ajax=1&page='
    page=0
    # 起始url，爬虫将从此开始爬取
    start_urls = [base_url+str(page)]


    def parse(self, response):
        div_list=response.xpath('//div[@class="item"]')
        for div in div_list:
            item = DemoItem()
            # extract序列化
            item['title']=div.xpath('./div[@class="right"]/a[@target="_blank"]/text()')[0].extract()
            item['link'] = div.xpath('./a[@target="_blank"]/@href')[0].extract()
            item['img_link']=div.xpath('./a[@target="_blank"]/img/@src')[0].extract()
            # 返回给管道
            yield item
        if self.page<200:
            self.page+=1
            url=self.base_url+str(self.page)
            # 回调到parse
            yield scrapy.Request(url,callback=self.parse)





