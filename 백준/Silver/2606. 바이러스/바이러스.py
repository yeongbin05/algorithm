a=int(input())
b=int(input())
arr=[[] for i in range(a+1)]
visited=[False]*(a+1)
for i in range(b):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

def dfs(start):
    stack=[start]
    visited[start]=True

    while stack:
        current=stack.pop()
        
        for adj in arr[current]:
            if visited[adj]==False:
                visited[adj]=True
                stack. append(adj)
dfs(1)
print(visited.count(True)-1)

