a=int(input())
array=[]
for i in range(a):
    array.append(input().split())


array.sort(key=lambda x: int(x[0]))

for i in array:
    print(i[0],i[1])