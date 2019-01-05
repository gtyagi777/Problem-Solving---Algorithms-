# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:20:13 2018

@author: tyagi
"""

def solution(arr):
    n = len(arr)
    c= 1
    
    for i in range(n-1):
        ind = i
        jump = 1
        boo = 1
        
        while(ind != n-1):
            val = 9999
            cidx = -1
            
            for k in range(ind + 1,n):
                if k%2 == 1:
                    if arr[k] > arr[ind] and arr[k] - arr[ind] < val:
                        val = arr[k] - arr[ind]
                        cidx = k
                else:
                    if arr[k] < arr[ind] and arr[ind] - arr[k] < val:
                        val = arr[ind] - arr[k]
                        cidx = k
            
            if val == 9999:
                boo = 0
                break
            
            jump += 1
            ind = cidx
        
        if boo ==1:
            c+= 1
        
    return c

print(solution([10,11,14,11,10]))
print(solution([10,13,12,14,15]))
            
        
            
                
                    
    
                