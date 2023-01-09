a=int(input())
cnt=0
b=list(map(int,input().split()))

for i in b:
    if i==1:
        cnt+=1
        continue
    for j in range(2,i):
        if i%j==0:
            
            cnt+=1
            break
print(a-cnt)