# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:24:19 2018

@author: tyagi
"""

def Bracket_swap(s):
    s = list(s)
    count = 0
    p = 0
    pos = []
    T_sum = 0
    for i in range(len(s)):
        if s[i] == '[':
            pos.append(i)
    
    for i in range(len(s)):
        print(" ".join(s))
        if s[i] == '[':
            count += 1
            p +=1
        elif s[i] == ']':
            count -= 1
        
        if count < 0:
            T_sum += pos[p] - i
            s[i], s[pos[p]] = s[pos[p]], s[i]
            p += 1
            
            count = 1
    
    return T_sum

print(Bracket_swap("[]]][[]["))           
            
            
            