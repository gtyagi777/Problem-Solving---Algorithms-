<<<<<<< HEAD
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

=======
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

>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
print(lengthOfLongestSubstring("1qass"))