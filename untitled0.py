# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:53:05 2018

@author: tyagi
"""

# Write your code here
xx = int(input())
x = list(map(int,input().split()))
sums = 0
addi = []
for i in range(len(x)):
    sums = sums + x[i]
    addi.append(sums)
x = x[0:xx]
zz = int(input())
xx =[]
for a in range(zz):
    xx.append(int(input()))

def rec_binary_search(arr,ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        
        if (arr[mid-1] <= ele and arr[mid-1] <= ele) or arr[mid] ==ele :
            return True
        else :
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid],ele)

            else:
                return rec_binary_search(arr[mid+1:],ele)
    


for i in range(len(xx)):
    c = 0
    xxx = True
    for j in range(len(addi)):
        if xxx:
            if addi[j] >= xx[i]:
                xxx= False
                c = j +1
    print (c)
