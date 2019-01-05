# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:43:33 2019

@author: tyagi
"""

# Complete the countingValleys function below.
def jumpingOnClouds(c):
    i = len(c)-1
    count,j = 0,0
    while j < i:
        count += 1
        if j == i-2 or j == i-1:
            j = i
        elif c[j+2] == 0:
            j = j+2
        else:
            j = j+1
            
    return count
            
        
        
        
    

if __name__ == '__main__':


    s =list(map(int,"0 0 0 1 0 0".split()))

    result = jumpingOnClouds(s)
