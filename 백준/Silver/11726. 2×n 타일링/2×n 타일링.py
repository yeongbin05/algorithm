# 점화식 새우면 피보나치
n=int(input())

if n<3:
    print(n)
else:
    arr=[0]*(n+1)
    arr[0]=0
    arr[1]=1
    arr[2]=2
    for i in range(3,n+1):
        arr[i]=arr[i-2]+arr[i-1]

    
    print(arr[n]%10007)