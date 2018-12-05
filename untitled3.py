#code
for _ in range(int(input())):
    n = int(input())
    ints = list(map(int,"4 49 1 59 19 81 97 99 82 90 99 10 58 73 23".split()))
    ints.sort()
    sqrs = {}
    sql_list = []
    for i in  ints:
        sql_list.append(i*i)
    flag = "No"
    for i in range(n-1):
        boo = 0
        for j in range(i,n):
            if (sql_list[i] + sql_list[j]) in sql_list:
                flag = "Yes"
                boo = 1
                break
            elif (sql_list[i] + sql_list[j]) > max(sql_list):
                break
        if boo == 1:
            break
    print(flag)
        