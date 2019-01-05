# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:08:37 2018

@author: tyagi
"""

import math

def solution(n,k):
    n = int(n)
    k = int(k)
    if k ==1:
        if n%2 == 0:
            print("Bob")
        else:
            print("Alice")
    elif k <1:
        print("Alice")
        return
    else:        
        if n<k:
            print("Bob")
            return
        if n > (k+k):
            i = int(math.floor((math.log(n//2,k))))

            
            rem_ = n - (2 * k*((math.pow(k,i) - 1)/(k-1)))
            while rem_ < 0:
                i = i-1
                rem_ = n - (2 * k*((math.pow(k,i) - 1)/(k-1)))
            print(i)
            print(rem_)
            if rem_ >= math.pow(k,i+1):
                print("Alice")
            else:
                print("Bob")
        else:
            if n-k< k:
                print("Alice")
            else:
                print("Bob")  
              

'''
for _ in range(int(input())):
    x,y = map(int,input().split())
    solution(x,y)
'''
solution(10**18,2)    