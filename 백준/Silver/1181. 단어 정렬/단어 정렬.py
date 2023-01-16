a=int(input())
b=[]
for i in range(a):
    b.append(input())

b_set=list(set(b))

b_set.sort()
b_set.sort(key=len)


for j in b_set:
    print(j)