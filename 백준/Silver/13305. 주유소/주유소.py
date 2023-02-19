
n=int(input())
#도시 사이 거리
distance=list(map(int,input().split()))

#각 도시에서 사는 기름 가격
price=list(map(int,input().split()))

#총 합
ans=0
for i in range(len(price)-1):
    
    if price[i] ==min(price[i:-1]):
        ans+=sum(price[i]*distance[i:])
        
        break


    else: 
        ans+=price[i]*distance[i]

print(ans)