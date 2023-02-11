import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)

n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
cnt=1

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph,v,visited):
    global cnt
    q=deque([v])
    visited[v]=cnt

    while q:
        v=q.popleft()

        for x in graph[v]:
            if visited[x]==0:
                cnt+=1
                visited[x]=cnt
                
                q.append(x)


#오름차순 정렬
for j in graph:
    j.sort()


bfs(graph,r,visited)

for i in range(1,n+1):
    print(visited[i])