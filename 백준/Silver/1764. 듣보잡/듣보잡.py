import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
# n_list=deque()
# m_list=deque()
# nm_list=deque()
# for i in range(n):
#     n_list.append(sys.stdin.readline())

# for j in range(m):
#     m_list.append(sys.stdin.readline())

# for k in n_list:
#     if k in m_list:
#         nm_list.append(k)
# nm_list = list(map(lambda s : s.strip(), nm_list))
# print(len(nm_list))
# # print(nm_list)
# for i in sorted(nm_list):
#     print(i)
n_dic={}
m_dic={}
nm_dic={}
for i in range(n):
    n_dic[input()]=1
for j in range(m):
    m_dic[input()]=1

for i in m_dic:
    if i in n_dic:
        nm_dic[i]=1

print(len(nm_dic))
for i in sorted(nm_dic):
    print(i)