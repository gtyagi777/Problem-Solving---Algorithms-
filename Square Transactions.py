
x = list([1, 2, 1, 3, 4])
y = sum(x)
xx =[4,2,10]


# Write your code here
num= int(input())
x = list(map(int,input().split()))
sums = sum(x)
zz = int(input())
for _ in range(zz):
    xx = int(input())
    if xx > sums:
        print ("-1")
    else:
        sumz = 0
        for j in range(num):
            sumz = x[j] + sumz
            if sumz >= xx:
                print (j+1)
                break
            


