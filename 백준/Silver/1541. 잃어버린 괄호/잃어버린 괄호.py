a=list(input().split('-'))
lst=[]
for i in a:
    cnt=0
    n=i.split('+')
    for j in n:
        cnt+=int(j)
    lst.append(cnt)
# print(lst)
first=lst[0]
for k in range(1,len(lst)):
    first-=lst[k]
print(first)