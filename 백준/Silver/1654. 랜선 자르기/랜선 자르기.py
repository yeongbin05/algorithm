#이분탐색
import sys
k,n=map(int,input().split())
arr=[int(sys.stdin.readline()) for _ in range(k)]



start,end=1,max(arr)

while start<=end:
    
    mid=(start+end)//2
    cnt=0
    for i in arr:
        cnt+=i//mid
    
    if cnt>=n:
        start=mid+1
    else:
        end=mid-1
print(end)