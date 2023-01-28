arr=[ int(input()) for i in range(9)]


for i in arr:
    for j in arr:
        if i!=j and  i +j==sum(arr)-100:
            arr.remove(i)
            arr.remove(j)

arr.sort()
for k in arr:
    print(k)