import scrapy


class MatchDataSpider(scrapy.Spider):
    name = 'match_data'
    allowed_domains = ['www.espncricinfo.com']
    start_urls = ['https://www.espncricinfo.com/ci/content/match/fixtures_futures.html']

    def parse(self, response):

        list = response.xpath('//div[@id="second"]/div[1]/ul/li/a/text()').extract()
        months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
                       'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

        for element in list:

            tokens = element.split(',')
            dates = tokens[1].split('-')
            start_date = dates[0].split()

            if len(start_date) > 1:
                start_year = start_date[1]

            if len(dates) > 1:
                end_date = dates[1].split()
                end_month = months_dict[end_date[0]]
                end_year = end_date[1]
                if not start_year:
                    start_year = end_year
            else:
                end_month = 0
                end_year = 0
                start_year = 0

            yield {
                'series_name': tokens[0],
                'series_start_month': months_dict[start_date[0]],
                'series_start_year': start_year,
                'series_end_month': end_month,
                'series_end_year': end_year,
            }
'''''
        links = response.xpath('//div[@id="second"]/div[1]/ul/li/a/@href').extract()
        
        for link in links:
            yield response.follow(url=link, callback= self.parse2)


    def parse2(self, response):
'''''