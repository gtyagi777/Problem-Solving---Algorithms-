<<<<<<< HEAD
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
=======
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
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
