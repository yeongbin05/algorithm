n=int(input())

road=list(map(int,input().split()))
cnt=0 #자리 확인
start=0 #새로운 수열 처음 위치 확인
uphill=[]

for i in range(n-1):
    
    if road[i]<road[i+1]:
        cnt+=1
        if i+1==n-1:
            uphill.append(road[i+1]-road[start])
    else:
        uphill.append(road[i]-road[start])
        start=i+1

print(max(uphill))