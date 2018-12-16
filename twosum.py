# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:48:11 2018

@author: tyagi
"""

def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    if s == " ":
        return (1)
    k = 0
    ss = list(s)
    xx = []
    cur = 0
    i = 0
    while i < len(ss):
        if ss[i] in xx:
            k = max(k,len(xx))
            xx = []
            i = i - cur + 1
            cur = 0
        else:
            cur += 1
            xx.append(ss[i])
            k = max(k,len(xx))
            i += 1
    return (k)

print(lengthOfLongestSubstring("1qass"))