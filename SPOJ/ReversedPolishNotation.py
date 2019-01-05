# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 14:41:45 2018

@author: tyagi
"""

def reversedPolishedNotation(strng):
    string = list(strng)
    res = []
    response = ""
    
    for i in range(len(string)):
        if string[i] ==")":
            x = []
            b = True
            while b:
                c = res.pop()
                if c =="(":
                    b = False
                else:
                    x.append(c)
            res.append("".join(map(str,(x[2],x[0])))+ response + x[1])
        else:
            res.append(string[i])
        
    return res[0]
        
#driver Program
for _ in range(int(input())):
    print(reversedPolishedNotation(input()))
    