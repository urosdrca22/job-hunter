import scrapy
from ..items import JobhunterItem

class JobsSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'https://www.helloworld.rs/oglasi-za-posao'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        items = JobhunterItem()
        jobs = response.css('.mb-4.w-full')
        
        for job in jobs:
            title = job.css('.font-bold.text-lg::text').get().replace('\n', '').strip()
            company = job.css('.opacity-75 a::text').get()
            location = job.css('.items-center.gap-1 .gap-1 p::text').get()
            job_url = job.css('.font-bold.text-lg::attr(href)').get()
            details = 'www.helloworld.rs' + job_url

            items['title'] = title
            items['company'] = company
            items['location'] = location
            items['details'] = details
             
            yield items
            
           
        