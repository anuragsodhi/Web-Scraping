# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:46:14 2017

@author: Anurag
"""
import gdax
import pandas as pd

public_client = gdax.PublicClient()
order_book = public_client.get_product_order_book('BTC-USD', level=2)
current_price = public_client.get_product_ticker(product_id='BTC-USD')

dictList=[]
for key, value in order_book.items():
    dictList.append([key, value])


bid = dictList[1][1]
ask = dictList[2][1]

bid_ask = list(zip(bid,ask))

df = pd.DataFrame(bid_ask)
df.to_excel('outpu1t.xlsx', header=False, index=False)
print('Finished!')
    


