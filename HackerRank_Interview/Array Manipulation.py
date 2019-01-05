# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:20:46 2019

@author: tyagi
"""

def solution(n, queries):
    arr = [0] * n
    max_ = 0

    for i in queries:
        a,b = i[0], i[1]
        c = i[2]
        for j in range(a-1,b):
            arr[j] += c
            max_ = max(max_,arr[j])
    
    return max_
            

if __name__ == '__main__':

    n = 5
    m = 3

    queries = []
    queries.append(list(map(int, "1 2 100".rstrip().split())))

    result = solution(n, queries)
