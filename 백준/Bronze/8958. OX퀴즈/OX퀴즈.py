a=int(input())
for num in range(a):
    list1=list(input())
    k=0

    for i in list1:
        
        if list1[k]=='O':
            list1[k]=1
        if k>=1:
            if list1[k-1]!='X' and list1[k]==1:
                list1[k]=list1[k]+list1[k-1]
        k+=1
    while 'X' in list1:
        list1.remove('X')
    print(sum(list1))

