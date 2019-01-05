# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:39:16 2018

@author: tyagi
"""
def solution(S, E):
    # write your code in Python 3.6
    S.sort()
    E.sort()
    
    n = len(S)
    
    chairs = 1
    result = 1
    i =1
    #check previous
    j =0
    
    while(i<n and j <n) :
        
        if (S[i] < E[j]):
            
            chairs += 1
            i += 1
            
            result = max(result,chairs)
            
        else:
            chairs -= 1
            j+= 1
        
    return result
            
            
arr=[1,2,3,4,6] 
dep=[3,6,5,4,7] 
n = len(arr) 

print("Minimum Number of Platforms Required = ", 
		solution(arr, dep))  
