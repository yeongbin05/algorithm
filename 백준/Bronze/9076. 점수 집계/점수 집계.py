t=int(input())

for i in range(t):
    arr=list(map(int,input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    if max(arr)-min(arr)>=4:
        print('KIN')
        continue
    else:
        print(sum(arr))