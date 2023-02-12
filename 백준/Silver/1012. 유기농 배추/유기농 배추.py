import sys
sys.setrecursionlimit(10**7)
t=int(input())

def dfs(sy,sx):
    visited[sy][sx]=1
    arr[sy][sx]=0

    for dy,dx in ((1,0),(0,1),(0,-1),(-1,0)):
        ny,nx=sy+dy,sx+dx
        if 0<=ny<n and 0<=nx<m and visited[ny][nx]==0 and arr[ny][nx]==1:
            dfs(ny,nx)

for _ in range(t):
    m,n,k=map(int,input().split())
    arr=[[0]*(m) for i in range(n)]
    visited=[[0]*(m) for i in range(n)]
    for i in range(k):
        x,y=map(int,input().split())
        arr[y][x]=1
    cnt=0
    for x in range(m):
        for y in range(n):
            if arr[y][x]==1 and visited[y][x]==0:
                dfs(y,x)
                cnt+=1

    print(cnt)