# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:30:38 2018

@author: tyagi
"""
# generate prime number array
def primeAlgo(n):
    prime = [True for _ in range(n+1)]
    
    prime[0] = False
    prime[1] = False
    p = 2
    while p*p <= n:
        
        if prime[p] == True:
            for i in range(p*p,n+1,p):
                prime[i] = False
                
        p += 1
        
    return prime


#driver Program
tc = int(input())

xx = []
for _ in range(tc):
    start, end = map(int,input().split())
    xx.append(start)
    xx.append(end)
prime = primeAlgo(max(xx))
i = 0
for _ in range(tc):
    start = i
    i += 1
    end = i
    i += 1
    x, y = xx[start],xx[end]
    for a,b in enumerate(prime):
        if a>= x and a<= y:
            if b == True:
                print(a)
        elif a > y:
            break
    print()
