import sys
n=int(sys.stdin.readline())
dic={}
for i in range(n):
    a=sys.stdin.readline().rstrip()
    if a in dic:
        pass
    else:
        dic[a]=1
sorted_dic=sorted(dic)

sorsorted_dic=sorted(sorted_dic,key=len)
print(*sorsorted_dic,sep='\n')