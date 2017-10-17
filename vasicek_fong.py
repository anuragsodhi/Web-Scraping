# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:41:14 2017

@author: Anurag
"""

import math
#from datetime import datetime
import QuantLib as ql

def vf_discount_function(parameters,knots,t):
    sum_df = 1
    a = parameters[0]
    b = parameters[1:]
    num_b = len(b)-len(knots)
    for i, beta in enumerate(b):
        if i < num_b:
            sum_df += beta*(1-math.e**(-(i+1)*a*t))
        else:
            k_t = knots[i-num_b]
            if t >= k_t:
                sum_df += beta*((1-math.e**(-a*(t-k_t))) 
                                - (1-math.e**(-2*a*(t-k_t))) 
                                    + (1/3)*(1-math.e**(-3*a*(t-k_t))))
    return(sum_df)
    
parameters = [0.0304,-0.5577,-0.8063,0.5342,-2.5088,0.6706,0.7541,0.3981,0.1756]
knots = [0.5,2,5,10,30]
t=2
vf_discount_function(parameters,knots,t)

## Input settlement date in 'mm/dd/yyyy' format
settlement_date = '10/3/2017'
next_coupon = ['2/28/2018','1/31/2018', '2/15/2018']
maturity_date = ['8/31/2019', '7/31/2020', '8/15/2028']

#sd  = datetime.strptime(settlement_date, '%m/%d/%Y')

sd_split = list(map(int,settlement_date.split('/')))
sd = ql.Date(sd_split[1] , sd_split[0] , sd_split[2])

tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates()

cp=[1, 1.625, 5.5]
p =100

for i, maturity in enumerate(maturity_date):
    md_split = list(map(int,maturity_date[i].split('/')))
    md = ql.Date(md_split[1] , md_split[0] , md_split[2])
    schedule = ql.Schedule(sd, md, tenor, calendar, ql.Following,
                           ql.Following, ql.DateGeneration.Backward, False)
    k =list(schedule)
    t=0
    c=0
    for j in range(1,len(k)):
        if j==1:
            t = t + (k[j] - k[j-1])/360
        else:
            t = t + 181/360
        df = vf_discount_function(parameters,knots,t)
        c= c + (cp[i]/2)*df
        if j == len(k) -1:
            c = c + p*df
    print(c)


