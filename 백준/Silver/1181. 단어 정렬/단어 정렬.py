n=int(input())
dic={}
for i in range(n):
    a=input()
    if a in dic:
        pass
    else:
        dic[a]=1
sorted_dic=sorted(dic)

sorsorted_dic=sorted(sorted_dic,key=len)
print(*sorsorted_dic)