# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:08:00 2017

@author: Anurag
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time



import string
import random
random.choice(string.ascii_uppercase)




driver = webdriver.Chrome(executable_path='C:/Users/Anurag/Downloads/chromedriver_win32/chromedriver.exe')

driver.get("https://www.sierratradingpost.com/chippewa-homestead-boots-leather-6-for-men~p~297xn/?merch=prod-sim-prod297XN")


driver.get("https://www.sierratradingpost.com/cart/")

try:
    a = driver.find_element_by_id("enterKeycodeLink")
    a.click()
except:
    a = driver.find_element_by_id("editKeycodeLink")
    a.click()
time.sleep(2)
b = driver.find_element_by_id("keycodeInput")

b.send_keys(Keys.CONTROL + "a")
b.send_keys(Keys.DELETE)

b.send_keys('XYZ21421')
time.sleep(1)
b.send_keys(Keys.RETURN)

g = driver.find_element_by_id("orderTotal").text
if float(g[1:]) 




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