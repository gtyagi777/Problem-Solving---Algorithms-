# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:38:24 2019

@author: tyagi
"""

# Complete the countingValleys function below.
def countingValleys(n, s):
    dict_ = {'U': 1, 'D':-1}
    s = list(s)
    level = 0
    count = 0
    valley = 0
    for i in s:
        if level < 0:
            valley = 1
        level += dict_[i]
        if level == 0 and valley == 1:
            count += 1
            valley = 0
    
    return count
        
    

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.close()
