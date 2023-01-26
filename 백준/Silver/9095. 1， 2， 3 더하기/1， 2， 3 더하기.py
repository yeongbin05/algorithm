#인터넷 풀이 이해
t=int(input())
for i in range(t):
    
    a=int(input())
    arr=[0]*11
    arr[1]=1
    arr[2]=2
    arr[3]=4
    for i in range(4,11):
        arr[i]=arr[i-3]+arr[i-2]+arr[i-1]

    print(arr[a])
