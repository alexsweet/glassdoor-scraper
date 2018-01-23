# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:01:40 2017

@author: alexs
"""

import scrapy
import pandas as pd
import time
class QuotesSpider(scrapy.Spider):
    name = "glassdoor"
    
    def start_requests(self):
    
        #data = pd.read_csv('fortune500_companies.csv')
        
        urls = ['https://www.glassdoor.com/Reviews/3M-Reviews-E446.htm',    \      
        'https://www.glassdoor.com/Reviews/3M-Reviews-E446_P2.htm']
        
        
#        base_urls = retrieve_base_urls()
#        urls = url_page_maker(base_urls,10)
        
        
        for url in urls:
            time.sleep(.5)
            yield scrapy.Request(url=url, callback=self.parse)
           
            
            
    def parse(self,response):
               
        for review in response.xpath("//*/div[@id='ReviewsFeed']/*/li[@class=' empReview cf ']/*"):
            yield {
                'review_id': review.xpath(".//@id").extract_first(),
                'comp_name':response.xpath("//*/div[@class='buttons cell showDesk alignRt']/*/@data-emp-name").extract_first(),
                'comp_id':response.xpath("//*/div[@class='buttons cell showDesk alignRt']/*/@data-emp-id").extract_first(),
                 'pro': review.xpath(".//*/p[@class=' pros mainText truncateThis wrapToggleStr']/text()").extract_first(),
                 'con': review.xpath(".//*/p[@class=' cons mainText truncateThis wrapToggleStr']/text()").extract_first(),
                 'advice':review.xpath(".//*/p[@class=' adviceMgmt mainText truncateThis wrapToggleStr']/text()").extract_first(),
                 'date':review.xpath(".//*/time/@datetime").extract_first(),
                 'loc':review.xpath(".//*/span[@class='authorLocation middle']/text()").extract_first(),
                 'rt_total':review.xpath(".//*/span[@class='rating']/*/@title").extract_first(),
                 'num_helpful':review.xpath(".//*/div[@class='floatRt helpfulBtn margRtMd tightVert']/*/@data-count").extract_first(),
                 'rt_work_life':review.xpath(".//*/div[@class='subRatings module']/ul[@class='undecorated']/li[div/text() = 'Work/Life Balance']/*/@title").extract_first(),
                 'rt_values':review.xpath(".//*/div[@class='subRatings module']/ul[@class='undecorated']/li[div/text() = 'Culture & Values']/*/@title").extract_first(),
                 'rt_opp':review.xpath(".//*/div[@class='subRatings module']/ul[@class='undecorated']/li[div/text() = 'Career Opportunities']/*/@title").extract_first(),
                 'rt_comp':review.xpath(".//*/div[@class='subRatings module']/ul[@class='undecorated']/li[div/text() = 'Comp & Benefits']/*/@title").extract_first(),
                 'rt_mgmt':review.xpath(".//*/div[@class='subRatings module']/ul[@class='undecorated']/li[div/text() = 'Senior Management']/*/@title").extract_first(),
 
                }

def retrieve_base_urls():
    base_urls =[]
    with open('company_urls.txt','r') as f:
        for line in f.readlines():
            base_urls.append(line.strip())
        return base_urls

def url_page_maker(urls,n):
    url_list = []
    for url in urls:
        index = url.find(".htm")
        for i in range(2,n+1):
            url_nxt_page = url[0:index]+"_P"+str(i)+".htm"
            url_list.append(url_nxt_page)
    
    return url_list
        