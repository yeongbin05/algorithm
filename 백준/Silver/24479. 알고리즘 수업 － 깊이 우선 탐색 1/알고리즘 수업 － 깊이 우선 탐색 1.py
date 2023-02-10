import sys

sys.setrecursionlimit(10 ** 8)

n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
cnt=1

def dfs(graph,v,visited):
   global cnt
   visited[v]=cnt
   for j in graph[v]:
      if visited[j]==0:
         
         cnt+=1
         dfs(graph,j,visited)

for i in range(m):
   u,v=map(int,sys.stdin.readline().split())
   graph[u].append(v)
   graph[v].append(u)

for i in graph:
   i.sort()


dfs(graph,r,visited)

for i in range(1,n+1):
   print(visited[i])
