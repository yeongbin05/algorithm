import sys
t=int(sys.stdin.readline())

for i in range(t):
    result=0
    n,m=map(int,sys.stdin.readline().split())
    arr=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
    
    for x in range(m):
        for y in range(n):
            
            if arr[y][x]==1:
                
                for z in range(y,n):
                    
                    if arr[z][x]==0:
                        result+=1
                
    print(result)
                

