from itertools import permutations
n,m=map(int,input().split())
a=permutations(range(1,n+1),m)
for i in a:
  print(*i)