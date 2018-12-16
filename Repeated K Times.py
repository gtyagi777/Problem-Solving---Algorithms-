a = input()
a = list(map(int,input().split()))
aa = int(input())
flist = []
bb = {}
for i in a:
    bb[i] = bb.get(i, 0)+1
for k,v in bb.items():
    if v == aa:
        flist.append(k)
print(min(flist))
