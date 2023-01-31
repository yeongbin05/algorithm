k=int(input())
arr=[]
row=[]
col=[]
for i in range(6):
    x=list(map(int,input().split()))
    
    arr.append(x)
    if x[0]==1 or x[0]==2:
        row.append(x[1])
    else:
        col.append(x[1])

new_arr=[]
for i in range(1,5):
    if arr[i-1][0]==arr[i+1][0]:
        new_arr.append(arr[i][1])
if len(new_arr)!=2:
    if arr[5][0]==arr[1][0]:
        new_arr.append(arr[0][1])
    
    if arr[4][0]==arr[0][0]:
        new_arr.append(arr[5][1])
# print(new_arr)
if len(new_arr)==2:
    print(k*(max(row)*max(col)-new_arr[0]*new_arr[1]))
