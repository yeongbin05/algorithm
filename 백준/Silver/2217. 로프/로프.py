a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))

arr=[]

b.sort(reverse=True)

for i in range(a):
    arr.append(b[i]*(i+1))

print(max(arr))