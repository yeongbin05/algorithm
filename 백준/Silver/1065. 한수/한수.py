a=int(input())
cnt=0

b=1
for i in range(1,a+1):
    
    if len(str(b))==1:
        cnt+=1
    if len(str(b))==2:
        cnt+=1
    if len(str(b))==3:
        if int(str(b)[2])-int(str(b)[1])==int(str(b)[1])-int(str(b)[0]):

            cnt+=1
    b+=1
print(cnt)    
