# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:48:28 2018

@author: tyagi
"""
# your code goes here

def solution(n):
    count =n//5
    x = n//5
    while x >4:
        count += x//5
        x = x//5
        
    print(count)


for _ in range(int(input())):
	n = int(input())
	solution(n)
