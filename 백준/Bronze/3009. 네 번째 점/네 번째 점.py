x_arr=[0]*3
y_arr=[0]*3

for i in range(3):
    x_arr[i],y_arr[i]=map(int,input().split())

dic_x={}
dic_y={}

for i in x_arr:
    if i in dic_x:
        dic_x[i]+=1
    else:
        dic_x[i]=1
for i in y_arr:
    if i in dic_y:
        dic_y[i]+=1
    else:
        dic_y[i]=1

for i in dic_x:
    if dic_x[i]==1:
        print(i,end=' ')

for i in dic_y:
    if dic_y[i]==1:
        print(i,end=' ')