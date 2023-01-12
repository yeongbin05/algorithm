from sys import stdin
a=int(stdin.readline())
b=[]
for i in range(a):
    b.append(int(stdin.readline()))

print(round(sum(b)/a)) # 산술평균
b.sort()

print(b[a//2]) #중앙값
dic={}
for i in b:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
max_dic=0
cnt=0
for j in dic:
    if cnt==0:
        max_dic=j
    
    else: 
        if dic[j]>dic[max_dic]:
            max_dic=j
    cnt+=1

c=[]

for k in dic:
    
    if dic[max_dic]==dic[k] :
        c.append(k)
    
c.sort()

if len(c)>=2:
    print(c[1])
else:
    print(c[0])
print(max(b)-min(b))