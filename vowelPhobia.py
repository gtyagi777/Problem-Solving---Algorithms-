# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:44:15 2018

@author: tyagi
"""
"""
import collections
# Write your code here
for _ in range(1):
    llist = list("hashes".lower())
    dicts = collections.Counter(llist)
count = 0
for i in ['a','e','i','o','u']:
    count += dicts[i]

print(count)    
"""

for _ in range(1):
    
    c = list("zazabcdefghgfgfededededcdefghghijkjihihgfe".lower())
    res = "YES"
    for i in range(1, len(c)):
        if ord(c[i]) == 97 and ord(c[i-1]) == 122:
            continue
         if ord(c[i]) == 122 and ord(c[i-1]) == 97:
            continue
        elif abs(ord(c[i]) - ord(c[i-1])) == 1:
            continue
        else:
            res = "NO"
            break
    print(res)