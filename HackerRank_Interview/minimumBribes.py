# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:03:13 2019

@author: tyagi
"""

def minimumBribes(q):
    res = 0
    i = 1
    while i < len(q):
        c = q[i-1]
        if abs(q[i-1] - i) > 2:
            res = "Too chaotic"
            break
        else:
            if abs(q[i-1] - i) == 0:
                i += 1
            else:
                res += abs(q[i-1] - i)
                x = (i + abs(q[i-1] - i) +1)
                while i <= x  and i < len(q):
                    if abs(q[i-1] - i) > 2:
                        res = "Too chaotic"
                        break
                    i = i + 1
                i = x
                if res == "Too chaotic":
                    break
                
    
    print (res)
    
def minimumBribes1(q):
    res = 0
    i = 1
    count = 0
    res = 0
    while i < len(q)+ 1:
        r = abs(q[i-1] - i)
        if r> 2:
            res = "Too chaotic"
            break
        else:
            count += r
        i += 1
    if res == "Too chaotic":
        print(res)
    else:
        print(count//2)


if __name__ == '__main__':


    s =list(map(int,"1 2 5 3 4 7 8 6".split()))

    result = minimumBribes1(s)
