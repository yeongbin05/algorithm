#컴퓨터 개수
n=int(input())
# 연결된 쌍 개수
m=int(input())
arr=[[] for i in range(n+1)]
# 정점 방문했는지 체크
visited=[False for i in range(n+1)]


#연결된 쌍 입력받음
for i in range(m):
    #a와 b연결됨
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start):
    #마지막 정점 체크
    stack=[start]
    visited[start]=True
    #stack이 빌 때까지
    while stack:
        #현재 위치
        current=stack.pop()

        for adj in arr[current]:
            if visited[adj]==False:
                visited[adj]=True
                stack.append(adj)

dfs(1)
print(visited.count(True)-1)