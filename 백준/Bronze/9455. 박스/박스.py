t=int(input())

for i in range(t):
    result=0
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(n)]
    
    for x in range(m):
        for y in range(n):
            
            if arr[y][x]==1:
                
                for z in range(y,n):
                    
                    if arr[z][x]==0:
                        result+=1
                
    print(result)
                

