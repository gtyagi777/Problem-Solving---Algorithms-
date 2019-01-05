# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:24:56 2018

@author: tyagi
"""

import math 
  
# define a function egyptianFraction  
# which receive parameter nr as 
# numerator and dr as denominator 
def egyptianFraction(nr, dr): 
  
    # empty list ef to store 
    # denominator 
    ef = [] 
  
    # while loop runs until  
    # fraction becomes 0 i.e, 
    # numerator becomes 0 
    while nr != 0: 
  
        # taking ceiling 
        x = math.ceil(dr / nr) 
  
        # storing value in ef list 
        ef.append(x) 
  
        # updating new nr and dr 
        nr = x * nr - dr 
        dr = dr * x 
  
    # printing the values 
    for i in range(len(ef)): 
        if i != len(ef) - 1: 
            print(" 1/{0} +" .  
                    format(ef[i]), end = " ") 
        else: 
            print(" 1/{0}" . 
                    format(ef[i]), end = " ") 
  
# calling the function 
egyptianFraction(5,8) 