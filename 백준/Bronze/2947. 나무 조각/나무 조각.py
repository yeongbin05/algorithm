a=list(map(int,input().split()))
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            b=a[j]
            a[j]=a[j+1]
            a[j+1]=b
            for k in a:
                print(k,end=' ')
            print()