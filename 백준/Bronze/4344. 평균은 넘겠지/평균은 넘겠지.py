a=int(input())
for num in range(a):
    list1=list(map(int, input().split()))
    
    average=(sum(list1[1:])/list1[0])

    
    cnt=0
    for i in list1[1:]:
        if i>average:
            cnt+=1
        
    sum1=(cnt/list1[0])*100
    print(str(f"{sum1:.3f}")+"%")