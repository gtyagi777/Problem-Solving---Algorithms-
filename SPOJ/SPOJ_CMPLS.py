# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:11:31 2018

@author: tyagi
"""

def solution(arr,n,k):
    res = [['X' for i in range(n+k)] for j in range(n)]
    max_ = 0
    for i in range(n):
        max_ += 1
        if i == 0:
            for j in range(n):
                res[i][j] = arr[j]
        else:
            prev = set()
            for j in range(n-i):
                res[i][j] = res[i-1][j+1] - res[i-1][j]
                prev.add(res[i][j])
            
            if len(prev) == 1:
                break

    for i in range(max_-1,-1,-1):
        if i == max_-1:
            x = res[i][0]
            for j in range(1,n+k):
                res[i][j] = x
        else:
            for j in range(n+k-max_-1, n+k) :
               res[i][j] = res[i][j-1] + res[i+1][j-1]
    
    print(" ".join(map(str,res[0][n:])))
            

    
for _ in range(int(input())):
    n,k = map(int,input().split())
    
    arr = list(map(int,input().split()))
    solution(arr,n,k)

