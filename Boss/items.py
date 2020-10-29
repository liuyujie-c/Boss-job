# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()   # 岗位名称
    name_link = scrapy.Field()   # 详情页链接
    address = scrapy.Field()        # 所在地
    salary = scrapy.Field()       # 薪资
    company = scrapy.Field()       # 公司名称

