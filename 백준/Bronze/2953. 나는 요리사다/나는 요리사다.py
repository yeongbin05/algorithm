arr=[]
for i in range(5):
    arr.append(list(map(int,input().split())))

max=0 # max값
num=0 # 몇번째 사람
for i in range(5):
    if sum(arr[i])>max:
        max=sum(arr[i])
        num=i+1

print(num,max)