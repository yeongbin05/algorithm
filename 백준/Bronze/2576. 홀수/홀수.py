list1=[]
for i in range(7):
    list1.append(int(input()))
new_list=[]
for i in list1:
    
    if i%2!=0:
        new_list.append(i)
        
if len(new_list)>0:
    print(sum(new_list))
    print(min(new_list))
else:
    print(-1)