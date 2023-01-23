case=int(input())
arr=[]
for i in range(case):
    arr.append(list(map(int,input().split())))


dic={}
for i in range(len(arr)):
    cnt=0
    for j in range(len(arr)):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            cnt+=1
    dic[i]=cnt+1

for value in dic:
    print(dic[value],end=' ')