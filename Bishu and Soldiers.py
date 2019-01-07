<<<<<<< HEAD

def binarySearch(ar,l,r,x):
    while l <= r:
        m = (r + l)//2
      
        if ar[m] == x :
            return m
        elif ar[m] > x and ar[m-1] < x:
            return m-1
        elif ar[m] < x:
            l = m+1
        else:
            r = m-1
    return -1

def all_occurance(ar, m):
    c = m
    x = ar[m]
    while (x == ar[c]):
        c +=1
    return c

xx = int(input())
arr = []
for _ in range(xx):
    arr.append(int(input()))
#arr = list(map(int,input().split()))
arr.sort()
z = int(input())
for _ in range(z):
    x = int(input())
    if x < max(arr):
        d = binarySearch(arr,0,xx-1,x)
        c = all_occurance(arr, d)
        print(c  , sum(arr[0:(c)]), sep = ' ')
    else:
       print(xx, sum(arr), sep = ' ') 

    
    
    
from collections import defaultdict
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
 
di = defaultdict(int)
pn = defaultdict(int)
ps = defaultdict(int)
for i in arr: di[i] += 1
pt, pp = 0, 0
for i in range(1,101):
    pt += di[i]
    pp += di[i]*i 
    pn[i] = pt
    ps[i] = pp
 
for i in range(int(input())):
    curr = int(input())
=======

def binarySearch(ar,l,r,x):
    while l <= r:
        m = (r + l)//2
      
        if ar[m] == x :
            return m
        elif ar[m] > x and ar[m-1] < x:
            return m-1
        elif ar[m] < x:
            l = m+1
        else:
            r = m-1
    return -1

def all_occurance(ar, m):
    c = m
    x = ar[m]
    while (x == ar[c]):
        c +=1
    return c

xx = int(input())
arr = []
for _ in range(xx):
    arr.append(int(input()))
#arr = list(map(int,input().split()))
arr.sort()
z = int(input())
for _ in range(z):
    x = int(input())
    if x < max(arr):
        d = binarySearch(arr,0,xx-1,x)
        c = all_occurance(arr, d)
        print(c  , sum(arr[0:(c)]), sep = ' ')
    else:
       print(xx, sum(arr), sep = ' ') 

    
    
    
from collections import defaultdict
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
 
di = defaultdict(int)
pn = defaultdict(int)
ps = defaultdict(int)
for i in arr: di[i] += 1
pt, pp = 0, 0
for i in range(1,101):
    pt += di[i]
    pp += di[i]*i 
    pn[i] = pt
    ps[i] = pp
 
for i in range(int(input())):
    curr = int(input())
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
    print(pn[curr], ps[curr])