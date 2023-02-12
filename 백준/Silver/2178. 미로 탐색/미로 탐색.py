import sys
sys.setrecursionlimit(10**7)

def bfs(si,sj):
    global cnt
    
    q=[]
    q.append((si,sj))

    while q:

        ci,cj=q.pop(0)

        if (ci,cj)==(n-1,m-1):
            return visited[ci][cj]

        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and visited[ni][nj]==0:
                q.append((ni,nj))
                #현재거리 +1
                visited[ni][nj]=visited[ci][cj]+1
                

n,m=map(int, input().split())

arr=[list(map(int,input()))for i in range(n)]
visited=[[0]*m for i in range(n)]
si,sj=0,0
visited[si][sj]=1
ans=bfs(si,sj)
print(ans)
