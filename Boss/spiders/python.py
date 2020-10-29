import scrapy
from Boss import items


class PythonSpider(scrapy.Spider):
    name = 'python'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://login.zhipin.com/?ka=header-login']

    def parse(self, response):
        # 获取用户名称判断已经登录
        flag = response.xpath('//*[@id="header"]/div[1]/div[3]/ul/li[5]/a/span/text()').extract_first()
        if flag == "张伟":
            el_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li/div/div[1]')
            for el in el_list:
                item = items.BossItem()

                item["name"] = el.xpath('./div[1]/div/div[1]/span[1]/a/text()').extract_first()
                item["name_link"] = "https://www.zhipin.com" + el.xpath('./div[1]/div/div[1]/span[1]/a/@href').extract_first()
                item["address"] = el.xpath('./div[1]/div/div[1]/span[2]/span/text()').extract_first()
                item["salary"] = el.xpath('./div[1]/div/div[2]/span/text()').extract_first()
                item["company"] = el.xpath('./div[2]/div/h3/a/text()').extract_first()
                yield item

