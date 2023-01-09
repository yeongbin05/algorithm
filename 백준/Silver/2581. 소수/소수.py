
a=int(input())
b=int(input())
cnt=0
list=[]
for i in range(a,b+1):
    list.append(i)
    if i==1:
        cnt+=1
        list.remove(i)
        continue
    for j in range(2,i):
        if i%j==0:
            list.remove(i)
            cnt+=1
            break


if cnt==b-a+1:
    print(-1)
    
else :
    print(sum(list))
    print(list[0])

