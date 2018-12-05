#code
from collections import permutation
def fuc(x,y):
    if x == y:
        return 0
    else:
        z = x ^ y
    z = list("{0:b}".format(z))
    return z.count(1)

for _ in range(int(input())):
    dict = {}
    n - int(input()
    arr = list(map(int,input().split()))
    z = list(permutation(arr,2)
    count = 0
    for i in z:
        x,y = i
        cc =".".join(i)
        c = 0
        if cc not in dict:
            c = func(x,y)
            dict[cc] = c
        else:
            c = dict[cc]
        count += c
    print(count)
    