
lst=[[0]*101 for i in range(101)]
n=int(input())

for i in range(n):
    
    
    x1,y1=map(int,input().split())
    

    for x in range(101-y1-10,101-y1):
        for y in range(x1,x1+10):
            
            lst[x][y]=1

# for i in lst:
#     print(i)
cnt=0
for i in lst:
    cnt+=i.count(1)
print(cnt)