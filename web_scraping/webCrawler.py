#!/usr/bin/python

'''
Get all apartments listing in the Boston's Craigslist by value
and only print the listings below $2,000.

Author: Thiago Teixeira

'''

import sys
import requests
from bs4 import BeautifulSoup

myUrl = 'https://boston.craigslist.org/search/aap'

def crawler(max_pages):
  max_pages *= 120
  page = 0
  while page < max_pages:
    url = myUrl + '?s=' + str(page)
    r = requests.get(url)
    print '***********************'
    print 'GET method received ' + str(r.status_code)
    print '***********************\n'
        
    # converts to Beautiful Soup object
    so = BeautifulSoup(r.text, "lxml")
    
    #titles = so.findAll('a', {'class': 'result-title'})
    prices = so.findAll('span', {'class': 'result-price'})
    
    for price in prices:       
       pr = price.text
       priceInt = int(pr.replace('$',''))
       
       if (priceInt < 2000):
           print pr
           print '--'
        
    page += 120

crawler(1) # <-- Number of pages to be crawled
