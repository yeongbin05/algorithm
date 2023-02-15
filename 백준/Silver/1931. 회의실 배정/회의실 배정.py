n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))



arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

end=0
cnt=0
for i,j in arr:
    if i>=end:
        cnt+=1
        end=j

print(cnt)