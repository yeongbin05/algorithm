a=int(input())

arr=[]
new_arr=[]
for i in range(a):
    arr.append(i+1)

while len(arr)!=0:
    
    new_arr.append(arr.pop(0))
    if len(arr)==0:
        break
    arr.append(arr.pop(0))
   

for j in new_arr:
    print(j,end=' ')