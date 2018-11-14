from sys import stdin
X,Y,s,T  = map(int,stdin.readline().split())
count = 0
t = T
for i in range(0,T+1):
    if(t>=Y and t<= Y+ s):
        count += min(max(0,i-X+1),s+1)
    t -= 1
print (count)