# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:41:14 2017

@author: Anurag
"""

import math

parameters,knots,t = ([0.0282,-0.7587,-1.1631,0.8958,-2.2002,1.0815,1.2169,0.5667,-0.5866], [1,3,3,10,20], 5)
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
    
vf_discount_function(parameters,knots,t)