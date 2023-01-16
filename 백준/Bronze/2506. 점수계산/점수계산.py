a=int(input())
array=list(map(int,input().split()))
cnt=0
total=0
for i in array:
    

    if i==0:
        cnt=0
    elif i==1:
        if cnt>0:
            cnt+=1
            total+=cnt
        else:
            cnt+=1
            total+=1
print(total)