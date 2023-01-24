import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))

dic={}
for i in n_list:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for j in m_list:
    if j in dic:
        print(dic[j],end=' ')
    else:
        print(0,end=' ')