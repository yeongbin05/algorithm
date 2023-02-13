n,k=map(int,input().split())

def bfs(s,e):
    q=[]
    visited=[0]*200000

    
    visited[s]=1
    q.append(s)

    while q:
        c=q.pop(0)
        if c==e:
            return visited[c]-1
        
        for n in (c-1,c+1,c*2):
            if 0<=n<200000 and visited[n]==0:
                q.append(n)
                visited[n]=visited[c]+1



print(bfs(n,k))


