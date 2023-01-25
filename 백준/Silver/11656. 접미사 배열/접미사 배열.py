a=input()
arr=[]
for i in range(len(a)):
    arr.append(a[i:])

arr.sort()
for j in arr:
    print(j)