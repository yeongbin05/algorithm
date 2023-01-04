list=[]
a=1

for i in range(30):
    list.append(a)
    a=a+1

for i in range(28):
    
    b=int(input())
    
    for j in range(30):
        if b==list[j]:
            list[j]=0
  
while 0 in list:
    list.remove(0)

print(min(list))
print(max(list))
