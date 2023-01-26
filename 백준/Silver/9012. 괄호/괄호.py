t=int(input())


for case in range(t):
    arr=[]
    new_arr=[]
    a=input()
    for i in a:
        if i=='(':
            arr.append(i)
        
        if i==')' and '(' in arr:
            arr.pop()

        elif i==')' and '(' not in arr:
            new_arr.append(i)
            print('NO')
            break
        
    
    if len(arr)!=0:
        print('NO')
    elif len(new_arr)==0:
        print('YES')