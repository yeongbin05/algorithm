import sys
n,m=map(int,sys.stdin.readline().split())
n_arr=[]
m_arr=[]

for i in range(n):
    n_arr.append(sys.stdin.readline())
for i in range(m):
    m_arr.append(sys.stdin.readline())
cnt=0
for i in m_arr:
    if i in n_arr:
        cnt+=1
        

print(cnt)