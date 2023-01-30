from pprint import pprint
lst=[[0]*101 for i in range(101)]


for i in range(4):
    
    
    x1,y1,x2,y2=map(int,input().split())
    

    for x in range(11-y2,11-y1):
        for y in range(x1,x2):
            
            lst[x][y]=1

# for i in lst:
#     print(i)
cnt=0
for i in lst:
    cnt+=i.count(1)
print(cnt)