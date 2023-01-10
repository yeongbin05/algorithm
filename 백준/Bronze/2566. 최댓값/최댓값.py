a=[]



for row in range(9):
    a.append(list(map(int,input().split())))
    
max=0
row=0
col=0
for i in range(9):
    for j in range(9):
        if a[i][j]>=max:
            max=a[i][j]
            
            row=i
            col=j
            
print(max)
print(row+1,col+1)
    
