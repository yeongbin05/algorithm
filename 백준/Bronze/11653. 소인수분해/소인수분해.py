a=int(input())
b=[]

for i in range(2,a+1):
    if a==1:
        break
    if a%i==0:
        while a%i==0:
            a=a/i
            b.append(i)
    
    
for i in b:
    print(i)