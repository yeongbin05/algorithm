import sys
sys.setrecursionlimit(10000)
dx=[1,1,0,-1,-1,-1,0,1]
dy=[0,1,1,1,0,-1,-1,-1]
def dfs(a,b):
    

    arr[a][b]=0
    for i in range(8):
        if 0 <= a+dx[i] < h and 0 <= b+dy[i] < w:
            if arr[a+dx[i]][b+dy[i]]==1:
                dfs(a+dx[i],b+dy[i])


while True:
    w,h=map(int,input().split())
    

    if w==0 and h==0:
        break
    
    arr=[list(map(int,input().split())) for i in range(h)]
    cnt=0
    for x in range(h):
        for y in range(w):
            
            if arr[x][y]==1:
                dfs(x,y)
                cnt+=1
    print(cnt)