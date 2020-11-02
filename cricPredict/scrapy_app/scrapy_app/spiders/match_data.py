import scrapy


class MatchDataSpider(scrapy.Spider):
    name = 'match_data'
    allowed_domains = ['www.espncricinfo.com']
    start_urls = ['https://www.espncricinfo.com/ci/content/match/fixtures_futures.html']

    def parse(self, response):

        list = response.xpath('//div[@id="second"]/div[1]/ul/li/a/text()').extract()
        print("NOW CHECK")
        for element in list:
            print(element.split(',')[0])
            print(element.split(',')[1])
            pass

