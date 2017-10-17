# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 00:20:14 2017

@author: Anurag
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path='C:/Users/Anurag/Downloads/chromedriver_win32/chromedriver.exe')
search_keyword= ['exercise equipment']

##start loop for all search items
for keyword in search_keyword:
    driver.get("http://www.amazon.com")
    inputElement = driver.find_element_by_name("field-keywords")
    inputElement.send_keys(keyword)
    inputElement.send_keys(Keys.RETURN)
    sauce = driver.page_source
    soup = BeautifulSoup(sauce, "lxml")
    links_soup = soup.find_all("a", class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")    
    links=[]
    for i in links_soup:
        if i.get("href")[0:4] == "http":
            links.append(i.get("href"))
        else:
            links.append("https://www.amazon.com"+i.get("href"))
    product=[]
    price =[]
    weight=[]        
    for link in links:
        try:
            driver.get(link)
            product.append(driver.find_element_by_id("productTitle").text)
            try:
                price.append(driver.find_element_by_id("priceblock_ourprice").text)
            except:
                price.append(driver.find_element_by_id("priceblock_saleprice").text)
            shp = driver.find_element_by_id("detail-bullets").text
            if shp.find('Shipping Weight:') == -1:
                weight.append('Shipping weight missing')
            else:
                weight.append(shp[shp.find('Shipping Weight:')+len('Shipping Weight:')+1:shp.find('(View shipping rates and policies)')-1])
            print('done one of the links')
        except:
            pass
    
    final_list = list(zip(product,price,weight))
    df = pd.DataFrame(final_list)
    df.to_excel('output.xlsx', header=False, index=False)
    print('Finished!!')
    
