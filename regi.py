# -*- coding: utf-8 -*-
from urllib.parse import urljoin


import scrapy


class RegafiSpider(scrapy.Spider):
    name = 'regafi'
    allowed_domains = ['www.regafi.fr']
    start_urls = ['https://www.regafi.fr/spip.php?page=results&type=advanced&id_secteur=3&lang=en&denomination=&siren=954509741&cib=&bic=&nom=&siren_agent=&num=&cat=0&retrait=0']

    def parse(self, response):
        url = response.xpath('/html/body/div/div[5]/table/tr[2]/td[1]/a/@href').extract_first()
        print(url)
        url = urljoin(response.url, url)
        print(url)
        yield scrapy.Request(url, callback=self.parse_company_info)
        
    def parse_company_info(self, response):
        company_name = response.xpath('//*[@id="zone_description"]/ul[1]/li[1]/span/text()').extract_first()
        lei = response.xpath('//*[@id="zone_description"]/ul[1]/li[6]/span/text()').extract_first()
        legal_status = response.xpath('//*[@id="zone_description"]/ul[2]/li[2]/span/text()').extract_first()
        print("Company Name: " + company_name + " LEI:" + lei + " Legal Status: " + legal_status)
        
