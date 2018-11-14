
from sys import stdin,stdout
n  = int(stdin.readline())
for _ in range(n):
    N,A,B = map(int,stdin.readline().split())
    i = (N*B)/(A+B)
    if i - int(i) < 0.5:
        i = int(i)
    else:
        i = int(i) + 1 
    j = N - i
    stdout.write(str((i * i * A) + (j * j * B)) + "\n")