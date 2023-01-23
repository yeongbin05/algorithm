a=int(input())
summ=1
for i in range(1,a+1):
    summ=summ*i

fact=str(summ)[::-1]
cnt=0

for i in fact:
    if i=='0':
        cnt+=1
        
    else:
        print(cnt)
        break