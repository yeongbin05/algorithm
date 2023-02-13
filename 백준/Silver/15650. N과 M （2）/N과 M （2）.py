from itertools import combinations
n,m=map(int,input().split())

ans=list(combinations(range(1,n+1),m))

for i in ans:
    print(*i)