<<<<<<< HEAD
from sys import stdin,stdout
import itertools
import bisect
num  = (stdin.readline())
x = list(map(int,stdin.readline().split()))
y = tuple(itertools.accumulate(x))
num  = int(stdin.readline())
for _ in range(num):
    xx = int(input())
    if xx > y[-1]:
        print ("-1")
    else:
        c = bisect.bisect_left(y,xx)
=======
from sys import stdin,stdout
import itertools
import bisect
num  = (stdin.readline())
x = list(map(int,stdin.readline().split()))
y = tuple(itertools.accumulate(x))
num  = int(stdin.readline())
for _ in range(num):
    xx = int(input())
    if xx > y[-1]:
        print ("-1")
    else:
        c = bisect.bisect_left(y,xx)
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
        print(c+1)