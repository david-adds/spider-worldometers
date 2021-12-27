import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            name = response.xpath('.//text()').get()
            link = response.xpath('.//@href').get()
            
            yield{
                'country_name': name,
                'country_link': link
            }
        
