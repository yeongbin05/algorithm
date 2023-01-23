from itertools import combinations
case=int(input())
for i in range(case):
    a=1
    b=1
    n,m=map(int,input().split())

    for j in range(n):  
        a=a*m
        b=b*n
        m-=1
        n-=1
    print(int(a/b))

