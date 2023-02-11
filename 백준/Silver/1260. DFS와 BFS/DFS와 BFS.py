from collections import deque
n,m,r=map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
visited_1=[0 for i in range(n+1)]
cnt=1
cnt_1=1

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort()
def dfs(graph,v,visited):
    global cnt
    visited[v]=cnt
    
    for i in graph[v]:
        if visited[i] ==0:
            cnt+=1
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    global cnt_1
    visited_1[v]=cnt_1
    q=deque([v])

    while q :
        v=q.popleft()
        for i in graph[v]:
            if visited_1[i]==0:
                cnt_1+=1
                visited_1[i]=cnt_1
                q.append(i)

dfs(graph,r,visited)
bfs(graph,r,visited_1)

for i in range(1,n+1):
    try:
        print(visited.index(i),end=' ')
    except:
        pass
print()
for i in range(1,n+1):
    try:
        print(visited_1.index(i),end=' ')
    except:
        pass