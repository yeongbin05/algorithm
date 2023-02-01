from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())

dic={}


for i in range(1,n+1):
    a=sys.stdin.readline().rstrip()
    if a not in dic:   
        dic[a]=i
        dic[i]=a

for i in range(m):
    b=sys.stdin.readline().rstrip()
    try:
        print(dic[b])
    except:
        print(dic[int(b)])
        