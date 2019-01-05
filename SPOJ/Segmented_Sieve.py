# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:36:00 2018

@author: tyagi
"""
from math import sqrt, floor
def simpleSieve(limit_, prime):
    limit = limit_ +1
    mark = [True for _ in range(limit)]
    p = 2
    while p*p <=limit_:
        
        if mark[p] == True:
            for i in range(p*2,limit,p):
                mark[i] = False
                
                
        p += 1
    i =2
    while i < limit:
        if mark[i] == True:
            prime.append(i)
        i += 1
        
        
    return prime

def segmentedSieve(n):
    limit = int(sqrt(n))+1
    prime = []
    prime = simpleSieve(limit,prime)
    
    low = limit
    high = 2 * limit
    
    while low < n:
        if high > n:
            high = n
        
        mark = [True for i in range(limit+1)]
        
        for i in prime:
            loLim = floor(low/i) * i
            if loLim < low:
                loLim += i
            
            for j in range(loLim,high,i):
                mark[j-low] = False
        i = low
        while i < high:
            if mark[i-low] == True:
                prime.append(i)
            i += 1
                
        low = low +limit
        high = high + limit
        
    return prime

#Driver Program
n = 10
res = segmentedSieve(49)
print(res)
        
            
        
    