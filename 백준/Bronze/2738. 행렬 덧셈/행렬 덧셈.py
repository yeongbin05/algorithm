a,b=[],[]


row_num,col_num=map(int,(input().split()))
for row in range(row_num):
    a.append(list(map(int,input().split())))
    
for row2 in range(row_num):
    b.append(list(map(int,input().split())))

for i in range(row_num):
    for j in range(col_num):
        print(a[i][j]+b[i][j],end=' ')
    print()
    


