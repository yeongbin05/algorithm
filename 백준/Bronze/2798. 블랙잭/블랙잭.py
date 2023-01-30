from itertools import combinations
n,m=map(int,input().split())
card=list(map(int,input().split()))
max=0

comb=combinations(card,3)

for x,y,z in comb:
    a=x+y+z
    if a<=m and max<a:
        max=a


print(max)

