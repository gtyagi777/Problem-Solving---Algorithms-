'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import bisect
from collections import defaultdict
x, y = map(int,input().split())
a = list(map(int,input().split()))
pivot = defaultdict(list)
for i in range(len(a)):
    pivot[a[i]].append(i+1)
    
for _ in range(y):
    c,d = (map(int,input().split()))
    if c==d:
        print(0)
        continue
    v = pivot.get(c)
    w = pivot.get(d)
    if w[0] >v[0]:
        v,w = w,v
        
    coun = len(a)
    for i in v:
        k=bisect.bisect_left(w,i)
        
        if k>0 and k<len(w):
            aa = w[k]
            bb = w[k-1]
            if aa-i < i-bb:
                ccc = aa
            else:
                ccc= bb
        elif k ==len(w):
            aa = w[-1]
            bb = w[0]
            if i -aa < bb+x - i:
                ccc = aa
            else:
                ccc= bb
        elif k ==0 :
            ccc= w[0]
        else:
            ccc = w[-1]
        
        if abs(ccc-i)> (x//2):
            _ccc = ccc
            _i = i
            if i > ccc:
                _ccc = ccc + x
            else:
                _i = i + x
            coun = min(coun,abs(_ccc -_i))
        else:
            coun = min(coun,abs(ccc-i))

    if coun %2 == 0:
        print(coun//2)
    else:
        print((coun-1)//2)
        