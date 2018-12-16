# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 08:36:02 2018

@author: tyagi"""
import math
def getprime(z):
    c= z
    while c>1:
        if is_prime(c):
            return c
        c -= 1
    return 0
            
def is_prime(m):
    if m > 3:
        for i in range(3,m-1):
            if m%i == 0:
                return False
    elif m ==2 or m ==3:
        return True
    else:
        return False
    return True
        
        
n = 56207747913100119
x = int(math.pow(n,(1/3)))
d = getprime(x)
remainder = n - (d*d*d)
x = int(math.pow(remainder,(1/3)))
c = getprime(x)
remainder = remainder - (c*c*c)
x = int(math.pow(remainder,(1/3)))
b = getprime(x)
a = n - int(math.pow(b,3) + math.pow(c,3) + math.pow(d,3))
print(a,b,c,d,sep = ' ')