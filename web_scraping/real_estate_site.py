#!/usr/bin/env python

'''
This code aims to get the price and description of estates in the city
of Rio Grande, RS, Brazil. 

Author: Thiago Teixeira
'''

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.procuraseimovel.com.br/portal/imoveis/rs/rio-grande/venda?pagina='


def main():
  max_pages = 20
  page = 1
  while page < max_pages:
    res = requests.get(url + str(page) + '_2_0')
    if res.status_code != 200:
      break
    
    so = BeautifulSoup(res.text, "lxml")
    titles = so.findAll('p', {'class': 'descricao'})
    prices = so.findAll('div', {'class': 'direita'})
    
    for p, t in zip(prices, titles):
      price = re.sub("[^0-9|,]", "", p.text).replace(",", ".")
      if len(price) > 0:
        if float(price) > 400000:
          print(float(price), t.text)
      
    page += 1  

  
if __name__ == "__main__":
  main()
