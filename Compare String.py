# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:28:26 2018

@author: tyagi
"""

x, y = map(int,input().split())
a = input()
b = input()
for _ in range(y):
    c = int(input())
    b = b[:c-1] + "1" + b[c:]
    if int(b[:c]) < int(a[:c]):
        print("No")
    elif int(b[:c]) > int(a[:c]):
        print('YES')
    elif int(b[c-1:]) >= int(a[c-1:]):
        print('YES')
    else:
        print('No')