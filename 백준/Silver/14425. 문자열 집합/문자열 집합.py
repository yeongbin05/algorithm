n,m=map(int,input().split())
n_arr=[]
m_arr=[]

for i in range(n):
    n_arr.append(input())
for i in range(m):
    m_arr.append(input())
cnt=0
for i in m_arr:
    if i in n_arr:
        cnt+=1

print(cnt)