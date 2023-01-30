a=246912
arr=[True for i in range(a+1)]

for i in range(2,123456+1):
    if arr[i]==True:
        j=2
        while i*j<=a:
            arr[i*j]=False
            j+=1

arr[0]=False
arr[1]=False

while True:
    b=int(input())
    if b==0:
        break
    cnt=0
    for i in range(b+1,(b*2)+1):
        if arr[i]==True:
            cnt+=1

    print(cnt)