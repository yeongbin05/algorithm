dic={}
for i in range(10):
    n=int(input())
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1

dic_sum=0
mode=0

for i in dic:
    dic_sum+=i*dic[i]

mode=max(dic,key=dic.get)
print(int(dic_sum/10))
print(mode)



